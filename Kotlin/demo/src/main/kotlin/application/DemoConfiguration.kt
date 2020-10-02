package application

import controller.SuggestionController
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import service.SuggestionScoreService
import utils.MatchGeneratorUtil
import utils.WordSimilarityUtil

@Configuration
class DemoConfiguration {
    @Bean
    fun wordSimUtil(): WordSimilarityUtil {
        return WordSimilarityUtil()
    }

    @Bean
    fun matchGenerator(): MatchGeneratorUtil {
        return MatchGeneratorUtil(wordSimUtil())
    }

    @Bean
    fun suggestionScore(): SuggestionScoreService {
        return SuggestionScoreService(wordSimUtil(), matchGenerator())
    }

    @Bean
    fun suggestionController(): SuggestionController {
        return SuggestionController(suggestionScore())
    }
}