import random_string_gen.util as util
import random as r

CONSONANTS = util.generate_consonants()
VOWELS = util.generate_vowels()

def generate_char(prob: int, char_last_was_vowel: bool):
    sample = util.generate_chance(prob)
    choice = r.choice(sample)

    if choice == util.VOWEL_CHANCE:
        if char_last_was_vowel:
            prob = 10
        else:
            prob = 5
        char_last_was_vowel = True

        return r.choice(VOWELS), char_last_was_vowel, prob

    prob = 2
    return r.choice(CONSONANTS), char_last_was_vowel, prob