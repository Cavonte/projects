package application

import controller.SuggestionController
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import service.SuggestionScoreService
import utils.MatchGeneratorUtil

@Configuration
class DemoConfiguration {
    @Bean
    fun matchGenerator(): MatchGeneratorUtil {
        return MatchGeneratorUtil()
    }

    @Bean
    fun suggestionScore(): SuggestionScoreService {
        return SuggestionScoreService(matchGenerator())
    }

    @Bean
    fun suggestionController(): SuggestionController {
        return SuggestionController(suggestionScore())
    }
}