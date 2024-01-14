import random 
import string

hands = ["rock","paper", "scissors"]
hands_len = len(hands)

random_hand = random.randint(0, hands_len -1)

nh = hands[random_hand]

user_hands = input('Enter your selection rock, paper, scissors   ')
print(user_hands)
print(nh)

if user_hands == 'rock' and nh == 'rock':
    print("It's a draw")
elif user_hands == 'rock' and nh == 'scissors':
    print("You win ")
elif user_hands == 'rock' and nh == 'paper':
    print("You lose")
elif user_hands == 'paper' and nh == 'scissors': 
    print("You Lose")
elif user_hands == 'paper' and nh == 'paper':
    print("It's a draw")
elif user_hands == 'paper' and nh == 'rock':
    print ('You win')
elif user_hands == 'scissors' and nh == 'scissors':
    print("It's draw")
elif user_hands == 'scissors' and nh == 'paper':
    print('You Win')
elif user_hands == 'scissors' and nh == 'rock':
    print('you looe')
else:
    print(" start the game again")