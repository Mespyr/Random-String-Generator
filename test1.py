import sys
sys.path.append("..")

import random_string_gen

print(random_string_gen.alpha.CONSONANTS)
print(random_string_gen.alpha.VOWELS)

print(random_string_gen.util.generate_chance(5))
print(random_string_gen.util.generate_chance(2))
print(random_string_gen.util.generate_chance(7))
print(random_string_gen.util.generate_chance(10))