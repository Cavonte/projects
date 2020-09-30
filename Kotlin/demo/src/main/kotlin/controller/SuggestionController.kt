package controller

import entity.Coordinate
import entity.GeoNameCity
import org.springframework.boot.configurationprocessor.json.JSONArray
import org.springframework.boot.configurationprocessor.json.JSONException
import org.springframework.http.MediaType
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*
import org.springframework.web.context.request.RequestContextHolder
import org.springframework.web.context.request.ServletRequestAttributes
import service.DataManagerService
import service.SuggestionScoreService
import utils.MatchGeneratorUtil

@RestController
class SuggestionController {

    /**
     * Main endpoint. Handles request with and without a location.
     *
     * @param query     for suggestion
     * @param longitude of request
     * @param latitude  request
     * @return JSON Array with suggestion
     * @throws JSONException At response creation
     */
    @GetMapping("/suggestions", produces = [MediaType.APPLICATION_JSON_VALUE])
    @RequestMapping(value = ["/suggestions"], method = [RequestMethod.GET], produces = [MediaType.APPLICATION_JSON_VALUE])
    @Throws(JSONException::class)
    fun autoCompleteSuggestions(@RequestParam(name = "q") query: String,
                                @RequestParam(name = "longitude", required = false) longitude: Double?,
                                @RequestParam(name = "latitude", required = false) latitude: Double?,
                                @RequestParam(name = "limit", required = false) limit: Int?): ResponseEntity<*>? {

        val finalLimit = if (limit == null || limit < 1) 20 else limit

        require(query.isNotEmpty()) {
            val request = (RequestContextHolder.getRequestAttributes() as ServletRequestAttributes?)!!.request
            return ResponseEntity.badRequest().body("Invalid Parameters. Given: " + request.queryString)
        }

        if (invalidGetParameters(query, longitude, latitude)) {
            val request = (RequestContextHolder.getRequestAttributes() as ServletRequestAttributes?)!!.request
            return ResponseEntity.badRequest().body("Invalid Parameters. Given: " + request.queryString)
        }

        val matchGenerator = MatchGeneratorUtil()
        val filteredCities: List<GeoNameCity> = matchGenerator.reducedList(DataManagerService.cities, query)
        val location = Coordinate()
        val suggestionScore = SuggestionScoreService()
        val storedSuggestion: MutableList<GeoNameCity> = suggestionScore.sortSuggestion(filteredCities, location, query)
        val result: JSONArray = suggestionScore.prepareResultArray(storedSuggestion, location, finalLimit)
        println(result.toString())
        println("Request Ended.")
        return ResponseEntity.ok(result.toString())
    }


    /**
     * Returns true if one of the parameters is invalid, e.g. empty string
     *
     * @param query     from request
     * @param longitude of request
     * @param latitude  of request
     * @return boolean is the request invalid
     */
    private fun invalidGetParameters(query: String, longitude: Double?, latitude: Double?): Boolean {
        if (longitude == null && latitude == null) {
            return (Regex("\\d+").containsMatchIn(query))
        } else {
            return longitude == null || latitude == null || Regex("\\d+").containsMatchIn(query)
        }
    }
}