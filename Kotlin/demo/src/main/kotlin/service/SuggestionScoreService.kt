package service

import entity.Coordinate
import entity.GeoNameCity
import info.debatty.java.stringsimilarity.WeightedLevenshtein
import org.springframework.boot.configurationprocessor.json.JSONArray
import org.springframework.boot.configurationprocessor.json.JSONObject
import org.springframework.stereotype.Service
import utils.MatchGeneratorUtil
import utils.WordSimilarityUtil
import java.util.*
import java.util.stream.Collectors

@Service
class SuggestionScoreService constructor(private val matchGenerator: MatchGeneratorUtil) {

    /**
     * Sort the suggestions based on the similarity with the city names and secondly based on the distance
     * https://stackoverflow.com/questions/369512/how-to-compare-objects-by-multiple-fields
     * https://github.com/tdebatty/java-string-similarity
     * WeightedLevenshtein
     *
     * @param location       location of the request
     * @param query          initial query
     * @return list of sorted suggestions
     */
    fun sortSuggestion(location: Coordinate, query: String, limit: Int?, filterByCountry: Boolean = false): JSONArray {
        require(query.isNotEmpty() || Regex("\\d+").containsMatchIn(query)) {
            "Validate query. Given $query"
        }

        val filteredCities: List<GeoNameCity> = matchGenerator.reducedList(DataManagerService.cities, query)
        val helper = WordSimilarityUtil()
        val weightedLevenshtein = WeightedLevenshtein(helper.getCharInterface())
        var comparator: Comparator<GeoNameCity> = Comparator.comparing { city: GeoNameCity ->
            weightedLevenshtein.distance(query.trim { it <= ' ' }.toLowerCase(), city.name.toLowerCase())
        }
        comparator = comparator.thenComparing { city: GeoNameCity -> matchGenerator.calculateDistance(location, city) }

        var cityStream: MutableList<GeoNameCity> = filteredCities.stream().sorted(comparator).collect(Collectors.toList())

        if (filterByCountry) {
            cityStream = matchGenerator.filterByCountry(cityStream, location)
        }

        return prepareResultArray(cityStream, location, limit)
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
    private fun prepareResultArray(sortedList: MutableList<GeoNameCity>, coordinate: Coordinate, limit: Int?): JSONArray {
        val result = JSONArray()
        for (geoNameCity in sortedList) {
            val cityJson = JSONObject()
            cityJson.put("name", geoNameCity.name + ", " + geoNameCity.timeZone + ", " + geoNameCity.country)
            cityJson.put("distance (in km)", String.format("%.3f", matchGenerator.calculateDistance(coordinate, geoNameCity)))
            cityJson.put("score", String.format("%.2f", matchGenerator.calculateScore(sortedList, geoNameCity)).toDouble())
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