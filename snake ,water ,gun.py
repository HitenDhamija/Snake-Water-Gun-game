import random
print('Snake - Water - Gun')
n = int(input('Enter number of rounds: '))
options = ['s', 'w', 'g']
rounds = 1
comp_win = 0
user_win = 0
while rounds <= n:
    print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")

    try:
        player = input("Choose your option: ")
    except EOFError as e:
        print(e)
 
    # Control of bad inputs
    if player != 's' and player != 'w' and player != 'g':
        print("Invalid input, try again\n")
        continue
 
    computer = random.choice(options)
    cw=False
    uw=False
    print(computer)
    if computer == 's':
        if player == 'w':
            comp_win += 1
            cw=True

        elif player == 'g':
            user_win += 1
            uw=True
 
    elif computer == 'w':
        if player == 'g':
            comp_win += 1
            cw=True
        elif player == 's':
            user_win += 1
            uw=True
 
    elif computer == 'g':
        if player == 's':
            comp_win += 1
            cw=True
        elif player == 'w':
            user_win += 1
            uw=True

    if cw==True:
        print("Computer Won this round")
    elif uw==True:
        print("You Won this round")
    else:
        print("Draw")
    
    print(f"Total Point:\nUser Point:{user_win}\nComputer Point:{comp_win}")

    rounds += 1
 
 
# Final winner based on the number of wons
if user_win > comp_win:
    print("Congratulations!! You Won",user_win)
elif comp_win > user_win:
    print("You lose!!",comp_win)
else:
    print("Match Draw!!")