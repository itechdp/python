# take a input from the user as an integer like for snake press 1 water press 2 gun press 3
# if user = 1 comp = 2 user win
# if user = 2 comp = 3 user win
# if user = 3 comp = 1 user win
# if user = 1 comp = 3 comp win
# if user = 3 comp = 2 comp win
# if user = 2 comp = 1 comp win

import random

print("********** Snake Water Gun **********")
player_name = input("Enter Player name: ")

random_no = random.randint(1, 3)

choice = 0

for i in range(1,6):    
    print("Snake(1) Water(2) Gun(3)")
    choice = int(input("Your Choice: "))

    if random_no == 3 and choice == 1:
        print(player_name+" Choice: "+str(choice))
        print("Computer Choice: "+str(random_no))
        print("Gun kill the snake: Computer win")

    elif random_no == 2 and choice == 3:
        print(player_name+" Choice: "+str(choice))
        print("Computer Choice: "+str(random_no))
        print("Gun is in the water: Computer win")

    elif random_no == 1 and choice == 2:
        print(player_name+" Choice: "+str(choice))
        print("Computer Choice: "+str(random_no))
        print("Snake drinking the water: Computer win")

    elif random_no == 2 and choice == 1:
        print(player_name+" Choice: "+str(choice))
        print("Computer Choice: "+str(random_no))
        print(f"Snake drinking the water: {player_name} win")

    elif random_no == 3 and choice == 2:
        print(player_name+" Choice: "+str(choice))
        print("Computer Choice: "+str(random_no))
        print(f"Gun is in the water: {player_name} win")

    elif random_no == 1 and choice == 3:
        print(player_name+" Choice: "+str(choice))
        print("Computer Choice: "+str(random_no))
        print(f"Gun kill the snake: {player_name} win")

    else:
        print("Game tie")
