import random

def scramble_word(word):
   return "".join(random.sample(word, len(word)))

words = ["python", "developer", "programming", "challenge"]
word = random.choice(words)
scrambled = scramble_word(word)

print("Scrambled word:", scrambled)
