package utils

import entity.GeoNameCity
import info.debatty.java.stringsimilarity.WeightedLevenshtein
import java.util.stream.Collectors

class MatchGeneratorUtil {
    /**
     * Filter the list of cities based on the query.
     * @param cities untouched list of cities
     * @param query query passed by user.
     * @return list of cities that are eligible
     */
    fun reducedList(cities: List<GeoNameCity>, query: String): List<GeoNameCity> {
        require(query.isNotEmpty()) { "Invalid query. $query" }
        require(cities.isNotEmpty()) {"Invalid city list. $cities"}

        return cities.stream()
                .filter { e: GeoNameCity -> eligibleCity(query, e.name) }
                .collect(Collectors.toList())
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

        val helper = WordSimilarityUtil()
        val weightedLevenshtein = WeightedLevenshtein(helper.getCharInterface())
        val minimalChangeTolerance = 1.5
        val sanitizedQuery = query.trim { it <= ' ' }.replace("\\s+".toRegex(), " ").toLowerCase()
        val lowerCityName = cityName.toLowerCase()
        return (sanitizedQuery.contentEquals(lowerCityName)
                || cityName.contains(sanitizedQuery)
                || weightedLevenshtein.distance(cityName, sanitizedQuery) < minimalChangeTolerance)
    }
}