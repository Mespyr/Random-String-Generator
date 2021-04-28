import random as r

VOWEL_CHANCE = 0
CONSONANT_CHANCE = 1


def generate_vowels() -> list: 
    return ['a', 'e', 'i', 'o', 'u', 'y']


def generate_chance(cchance: int) -> list:
    """
        cchance is an integer from 0-10 showing how likely a consonant is to occur.
    """
    chance_sample = []

    for i in range(cchance):
        chance_sample.append(CONSONANT_CHANCE)

    while len(chance_sample) < 10:
        chance_sample.append(VOWEL_CHANCE)
    
    return chance_sample

def generate_consonants() -> list:
    i = 96
    res = []
    vowels = generate_vowels()
    
    while i != 122:
        i += 1
        if chr(i) not in vowels:
            res.append(chr(i))

    return res
