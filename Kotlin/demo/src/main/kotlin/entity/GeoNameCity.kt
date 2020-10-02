package entity

class GeoNameCity (
        val id: Int,
        val name: String,
        val ascii: String,
        val altName: String? = "",
        val longitude: String,
        val latitude: String,
        val country: String,
        private val altCountryCode: String? = "",
        val timeZone: String,
        val population: Int
)