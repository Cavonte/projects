package service

import entity.GeoNameCity
import org.junit.jupiter.params.shadow.com.univocity.parsers.tsv.TsvParser
import org.junit.jupiter.params.shadow.com.univocity.parsers.tsv.TsvParserSettings
import java.io.InputStreamReader
import java.io.Reader
import java.io.UnsupportedEncodingException

/**
 * Class which parses the tsv file.
 */
object DataManagerService {
    private const val CITY_FILE_PATH = "/cities_canada-usa.tsv"
    val cities: MutableList<GeoNameCity> = ArrayList()

    /**
     * Private Constructor
     * TSV Parser
     * TSV content for ref http://download.geonames.org/export/dump/readme.txt
     */
    init {
        val settings = TsvParserSettings()
        settings.format.setLineSeparator("\n")
        settings.isHeaderExtractionEnabled = true
        val parser = TsvParser(settings)
        val allRecords = parser.parseAllRecords(getReader())
        for (record in allRecords) {
            val tempCity = GeoNameCity(record.getInt("id"),
                    record.getString("name"),
                    record.getString("ascii"),
                    record.getString("alt_name"),
                    record.getString("long"),
                    record.getString("lat"),
                    record.getString("country"),
                    record.getString("cc2"),
                    record.getString("tz"),
                    record.getInt("population"))
            cities.add(tempCity)
        }
    }

    /**
     * Credits https://github.com/uniVocity/univocity-parsers/blob/master/src/test/java/com/univocity/parsers/examples/Example.java
     * Creates a reader for a resource in the relative path
     *
     * @return a reader of the resource
     */
    private fun getReader(): Reader {
        return try {
            val stream = javaClass.getResourceAsStream(CITY_FILE_PATH)
            InputStreamReader(stream, "UTF-8")
        } catch (e: UnsupportedEncodingException) {
            throw IllegalStateException("Unable to read input", e)
        }
    }
}