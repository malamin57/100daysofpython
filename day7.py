import random
word_list = ['hey', 'december','october']

chosen_word  = random.choice(word_list)

guess = input("Guess the word: ").lower

if guess == word_list:
    print('you are right')
else:
    print('nope')
    print(chosen_word)
