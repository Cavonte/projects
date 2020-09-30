package service

import entity.Coordinate
import entity.GeoNameCity
import info.debatty.java.stringsimilarity.WeightedLevenshtein
import org.springframework.boot.configurationprocessor.json.JSONArray
import org.springframework.boot.configurationprocessor.json.JSONObject
import utils.WordSimilarityUtil
import java.security.InvalidParameterException
import java.util.*
import java.util.stream.Collectors
import java.util.stream.Stream
import kotlin.math.asin
import kotlin.math.cos
import kotlin.math.sin
import kotlin.math.sqrt

class SuggestionScoreService {
    /**
     * Sort the suggestions based on the similarity with the city names and secondly based on the distance
     * https://stackoverflow.com/questions/369512/how-to-compare-objects-by-multiple-fields
     * https://github.com/tdebatty/java-string-similarity
     * WeightedLevenshtein
     *
     * @param filteredCities list of already reduced cities
     * @param location       location of the request
     * @param query          initial query
     * @return list of sorted suggestions
     */
    fun sortSuggestion(filteredCities: List<GeoNameCity>, location: Coordinate, query: String): MutableList<GeoNameCity> {
        require(query.isNotEmpty() || Regex("\\d+").containsMatchIn(query)) {
            "Validate query. Given $query"
        }

        val helper = WordSimilarityUtil()
        val weightedLevenshtein = WeightedLevenshtein(helper.getCharInterface())
        var comparator: Comparator<GeoNameCity> = Comparator.comparing { city: GeoNameCity ->
            weightedLevenshtein.distance(query.trim { it <= ' ' }.toLowerCase(), city.name.toLowerCase())
        }
        comparator = comparator.thenComparing { city: GeoNameCity -> calculateDistance(location, city) }

        val cityStream: Stream<GeoNameCity> = filteredCities.stream().sorted(comparator)
        return cityStream.collect(Collectors.toList<GeoNameCity>())
    }


    /**
     * Calculate the distance between the current location and the target City
     * Credit: http://www.codecodex.com/wiki/Calculate_Distance_Between_Two_Points_on_a_Globe#Java
     *
     * @param location  of the request
     * @param targetCity target of the calculation
     * @return distance in kilometers
     */
    private fun calculateDistance(location: Coordinate, targetCity: GeoNameCity): Double {
        val earthRadius = 6371.0
        val lat2: Double = targetCity.latitude.toDouble()
        val lon2: Double = targetCity.longitude.toDouble()
        val lat1: Double = location.latitude
        val lon1: Double = location.longitude
        val dLat = Math.toRadians(lat2 - lat1)
        val dLon = Math.toRadians(lon2 - lon1)
        val a = sin(dLat / 2) * sin(dLat / 2) +
                cos(Math.toRadians(lat1)) * cos(Math.toRadians(lat2)) *
                sin(dLon / 2) * sin(dLon / 2)
        val c = 2 * asin(sqrt(a))
        return earthRadius * c
    }

    /**
     * Filter the suggestion by country.
     *
     * @param filteredCities list of cities
     * @param location       coordinate
     * @param allCities      initial list from the data manager
     * @return list of filter
     */
    fun filterByCountry(filteredCities: List<GeoNameCity>, location: Coordinate, allCities: List<GeoNameCity>): MutableList<Any>? {
        require(allCities.isEmpty()) {
            "Validate input parameters. Initial list of cities is invalid."
        }

        val currentCity: GeoNameCity = identifyClosestCity(location, allCities)
        return filteredCities.stream()
                .filter { e: GeoNameCity -> currentCity.country.contentEquals(e.country)}
                .collect(Collectors.toList<Any>())
    }

    /**
     * Identify the closest city.
     *
     * @param location  of the request
     * @param allCities found in the tsv file
     * @return the name of the city closest to the coordinate passed.
     */
    private fun identifyClosestCity(location: Coordinate, allCities: List<GeoNameCity>): GeoNameCity {
        var smallestDistance = 3000000.0
        var closestCity = allCities[0]
        for (city in allCities) {
            val distance = calculateDistance(location, city)
            if (distance < smallestDistance) {
                smallestDistance = distance
                closestCity = city
            }
        }
        return closestCity
    }

    /**
     * Calculate the score of the suggestion based on the position in the array.
     *
     * @param scoredList  list of the suggested cities
     * @param currentCity city entity in the list.
     * @return double score
     */
    private fun calculateScore(scoredList: List<GeoNameCity>, currentCity: GeoNameCity): Double {
        if (scoredList.isEmpty()) throw InvalidParameterException("Invalid list of scored cities.")
        val index = scoredList.indexOf(currentCity) + 1.toDouble()
        val adjustedSize = scoredList.size.toDouble() + 1
        return 1 - index / adjustedSize
    }

    /**
     * Creates the json array to be returned.
     * //name : city/timezone/ country
     * //distance(in kilometers) : distance
     * //score :  score
     * //id : id of the city
     * //longitude: longitude
     * //latitude: latitude
     *
     * @param sortedList list of sorted list
     * @param coordinate used to calculate the distance
     * @return JSONArray
     */
    fun prepareResultArray(sortedList: MutableList<GeoNameCity>, coordinate: Coordinate, limit: Int?): JSONArray {
        val result = JSONArray()
        for (geoNameCity in sortedList) {
            val cityJson = JSONObject()
            cityJson.put("name", geoNameCity.name + ", " + geoNameCity.timeZone + ", " + geoNameCity.country)
            cityJson.put("distance (in km)", String.format("%.3f", calculateDistance(coordinate, geoNameCity)))
            cityJson.put("score", String.format("%.2f", calculateScore(sortedList, geoNameCity)).toDouble())
            cityJson.put("id", geoNameCity.id)
            cityJson.put("longitude", geoNameCity.longitude)
            cityJson.put("latitude", geoNameCity.latitude)
            result.put(cityJson)
            if (result.length() == limit) {
                break
            }
        }
        return result
    }

}