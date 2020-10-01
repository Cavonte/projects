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
import service.SuggestionScoreService

@RestController
class SuggestionController constructor(val suggestionScoreService: SuggestionScoreService) {

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
                                @RequestParam(name = "limit", required = false) limit: Int?): ResponseEntity<String>? {

        val finalLimit = if (limit == null || limit < 1) 20 else limit
        val request = (RequestContextHolder.getRequestAttributes() as ServletRequestAttributes?)!!.request

        require(query.isNotEmpty() && !Regex("\\d+").containsMatchIn(query)) {
            return ResponseEntity.badRequest().body("Invalid Parameters. Given: " + request.queryString)
        }

        val location = Coordinate(longitude, latitude)
        val result: JSONArray = suggestionScoreService.sortSuggestion(location, query, finalLimit)
        println("$result . Request Ended.")
        return ResponseEntity.ok(result.toString())
    }

    /**
     * Alternated endpoint. Result are filtered by figuring out the country of the request using the coordinates.
     *
     * @param query     for suggestion
     * @param longitude of request
     * @param latitude  request
     * @return JSON Array with suggestion
     * @throws JSONException At response creation
     */
    @RequestMapping(value = ["/suggestionsByCountry"], method = [RequestMethod.GET], produces = [MediaType.APPLICATION_JSON_VALUE])
    @Throws(JSONException::class)
    fun autoCompleteSuggestionsCountry(@RequestParam(name = "q") query: String,
                                       @RequestParam(name = "longitude") longitude: Double,
                                       @RequestParam(name = "latitude") latitude: Double,
                                       @RequestParam(name = "limit", required = false) limit: Int?): ResponseEntity<String>?
    {
        val finalLimit = if (limit == null || limit < 1) 20 else limit
        val request = (RequestContextHolder.getRequestAttributes() as ServletRequestAttributes?)!!.request

        require(query.isNotEmpty() && !Regex("\\d+").containsMatchIn(query)) {
            return ResponseEntity.badRequest().body("Invalid Parameters. Given: " + request.queryString)
        }

        val location = Coordinate(longitude, latitude)

        val result: JSONArray = suggestionScoreService.sortSuggestion(location, query, finalLimit, filterByCountry = true)
        println("$result . Request Ended.")
        return ResponseEntity.ok(result.toString())
    }
}