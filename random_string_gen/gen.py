import random_string_gen.alpha as alpha
from random_string_gen.util import CONSONANT_CHANCE, VOWEL_CHANCE
import random as r

def generate_string(length: int, starter: int):
    s: str = ""
    idx_len = 1

    if starter == CONSONANT_CHANCE:
        char_last_was_vowel = False
        s += r.choice(alpha.CONSONANTS)
        prob = 2
    else:
        char_last_was_vowel = True
        s += r.choice(alpha.VOWELS)
        prob = 8

    while idx_len != length:
        # print(s)

        char, char_last_was_vowel, prob = alpha.generate_char(prob, char_last_was_vowel)
        s += char

        idx_len += 1

    return s
