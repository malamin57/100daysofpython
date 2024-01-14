print("Welcome to Treasure Island.Your mission is to find the treasure.")
path=input('Do you want to go left or right')
if path == 'right' or '':
    print('Game Over')
elif path == 'left':
    next=input('swim or wait')
    if next == 'swim' or '':
        print('Attacked by trout Game Over')
    elif next == 'wait':
        next_step = input('which door do you want - Red,Blue,Yellow')
        if next_step == 'Red':
            print('Burned by Fire Game Over')
        elif next_step == 'Blue':
            print('Eaten by beats Game Over')
        elif next_step == 'Yellow':
            print('You Win')
        else:
            print('Game Over')
