import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

options[0] 

while True:
    user_move = input("Please Enter Rock/Paper/Scissors or Q to quit: ").lower()
    if user_move == 'q':
        break
    
    if user_move not in ['rock', 'paper', 'scissors']:
        print('Please enter Rock, Paper or Scissors')
        continue

    
    rand_num = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    comp_pick = options[rand_num]
    print(f'Computer picked {comp_pick}. ')

    if user_move == 'rock' and comp_pick == 'scissors':
        print("You have won! ")
        user_wins +=1
        
    if user_move == 'paper' and comp_pick == 'rock':
        print('You have won! ')
        user_wins +=1
        
    if user_move == 'scissors' and comp_pick == 'paper':
        print('You have won! ')
        user_wins +=1

    else:
        print('You lost! ')
        computer_wins+=1

print(f'You won {user_wins} times. ')
print(f'The computer won {computer_wins} times. ')
print('Goodbye! ')

        

    

