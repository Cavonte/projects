package utils

import info.debatty.java.stringsimilarity.CharacterSubstitutionInterface

class WordSimilarityUtil {

    fun getCharInterface(): CharacterSubstitutionInterface {
        return CharacterSubstitutionInterface { c, c2 -> cost(c, c2) }
    }

    private fun cost(c1: Char, c2: Char): Double {
        return if (c1 == 'e' && c2 == 'r' ||
                c1 == 'e' && c2 == 'w' ||
                c1 == 'r' && c2 == 'e' ||
                c1 == 'w' && c2 == 'e' ||
                c1 == 't' && c2 == 'r' ||
                c1 == 'r' && c2 == 't' ||
                c1 == 't' && c2 == 'y' ||
                c1 == 'y' && c2 == 't' ||
                c1 == 'a' && c2 == 's' ||
                c1 == 's' && c2 == 'a' ||
                c1 == 'i' && c2 == 'o' ||
                c1 == 'o' && c2 == 'i' ||
                c1 == 'i' && c2 == 'u' ||
                c1 == 'u' && c2 == 'i') {
            0.8
        }
        else 1.0
    }
}