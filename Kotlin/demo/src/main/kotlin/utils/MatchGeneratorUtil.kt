package utils

import entity.Coordinate
import entity.GeoNameCity
import info.debatty.java.stringsimilarity.WeightedLevenshtein
import service.DataManagerService
import java.util.stream.Collectors
import kotlin.math.asin
import kotlin.math.cos
import kotlin.math.sin
import kotlin.math.sqrt

class MatchGeneratorUtil(private val wordSimilarityUtil: WordSimilarityUtil) {
    /**
     * Filter the list of cities based on the query.
     * @param cities untouched list of cities
     * @param query query passed by user.
     * @return list of cities that are eligible
     */
    fun reducedList(cities: List<GeoNameCity>, query: String): List<GeoNameCity> {
        require(query.isNotEmpty()) { "Invalid query. $query" }
        require(cities.isNotEmpty()) { "Invalid city list. $cities" }

        return cities.stream()
                .filter { e: GeoNameCity -> eligibleCity(query, e.name) }
                .collect(Collectors.toList())
    }

    /**
     * Filter the suggestion by country.
     *
     * @param filteredCities list of cities
     * @param location       coordinate
     * @return list of filter
     */
    fun filterByCountry(filteredCities: List<GeoNameCity>, location: Coordinate): MutableList<GeoNameCity> {
        val currentCity: GeoNameCity = identifyClosestCity(location, DataManagerService.cities)
        return filteredCities.stream()
                .filter { e: GeoNameCity -> currentCity.country.contentEquals(e.country) }
                .collect(Collectors.toList<GeoNameCity>())
    }


    /**
     * Calculate the score of the suggestion based on the position in the array.
     *
     * @param scoredList  list of the suggested cities
     * @param currentCity city entity in the list.
     * @return double score
     */
    fun calculateScore(scoredList: List<GeoNameCity>, currentCity: GeoNameCity): Double {
        require(scoredList.isNotEmpty())
        if (scoredList.size == 1)
            return 1.toDouble()

        val index = scoredList.indexOf(currentCity) + 1.toDouble()
        val adjustedSize = scoredList.size.toDouble() + 1
        return 1 - index / adjustedSize
    }


    /**
     * Calculate the distance between the current location and the target City
     * Credit: http://www.codecodex.com/wiki/Calculate_Distance_Between_Two_Points_on_a_Globe#Java
     *
     * @param location  of the request
     * @param targetCity target of the calculation
     * @return distance in kilometers
     */
    fun calculateDistance(location: Coordinate, targetCity: GeoNameCity): Double {
        val earthRadius = 6371.0
        val lat2: Double = targetCity.latitude.toDouble()
        val lon2: Double = targetCity.longitude.toDouble()
        val lat1: Double = location.latitude ?: 0.0
        val lon1: Double = location.longitude ?: 0.0
        val dLat = Math.toRadians(lat2 - lat1)
        val dLon = Math.toRadians(lon2 - lon1)
        val a = sin(dLat / 2) * sin(dLat / 2) +
                cos(Math.toRadians(lat1)) * cos(Math.toRadians(lat2)) *
                sin(dLon / 2) * sin(dLon / 2)
        val c = 2 * asin(sqrt(a))
        return earthRadius * c
    }

    /**
     * Identify the closest city.
     *
     * @param location  of the request
     * @param allCities found in the tsv file
     * @return the name of the city closest to the coordinate passed.
     */
    private fun identifyClosestCity(location: Coordinate, allCities: List<GeoNameCity>): GeoNameCity {
        val closestCity: GeoNameCity

        closestCity = allCities.stream().reduce { closestCity, city ->
            if (calculateDistance(location, city) < calculateDistance(location, closestCity))
                city
            else
                closestCity

        }.get()

        return closestCity
    }

    /**
     * Use string comparison and string similarity tools to filter eligible cities.
     * WeightedLevenshtein -- Word Similarity Tool https://github.com/tdebatty/java-string-similarity
     *
     * @param query from the request
     * @param cityName cityName being compared
     * @return a boolean for the filter method
     */
    private fun eligibleCity(query: String, cityName: String): Boolean {
        require(query.isNotEmpty()) {
            "Invalid query: $query"
        }
        require(cityName.isNotEmpty()) {
            "Invalid city name: $cityName"
        }

        val weightedLevenshtein = WeightedLevenshtein(wordSimilarityUtil.getCharInterface())
        val minimalChangeTolerance = 2.0
        val sanitizedQuery = query.trim { it <= ' ' }.replace("\\s+".toRegex(), " ").toLowerCase()
        val lowerCityName = cityName.toLowerCase()
        return (sanitizedQuery.contentEquals(lowerCityName)
                || cityName.contains(sanitizedQuery)
                || weightedLevenshtein.distance(lowerCityName, sanitizedQuery) < minimalChangeTolerance)
    }
}