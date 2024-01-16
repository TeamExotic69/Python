import random
score_player , score_computer = 0 ,0

while score_computer!=5 and score_player!=5:
    print("rock = 0, paper = 1, scice = 2")
    player = int(input("Choose:"))

    c = ["rock", "paper", "scice"]              
    computer = random.choice(c) 

    #draw
    if player == 0 and computer == "rock":
        print("Draw!")
        print(f"You:{score_player} - computer:{score_computer}")
        
    if player == 1 and computer == "paper":
        print("Draw!")
        print(f"You:{score_player} - computer:{score_computer}")
        
    if player == 2 and computer == "scice":
        print("Draw!")
        print(f"You:{score_player} - computer:{score_computer}")
        
    
    #player win
    if player == 0 and computer == "scice":
        score_player +=1
        print("Good!")
        print(f"You:{score_player} - computer:{score_computer}")
    if player == 1 and computer == "rock":
        score_player +=1
        print("Good!")
        print(f"You:{score_player} - computer:{score_computer}")
    if player == 2 and computer == "paper":
        score_player +=1
        print("Good!")
        print(f"You:{score_player} - computer:{score_computer}")

    #computer win
    if computer == "rock" and player == 2:
        score_computer +=1
        print("haha loser!")
        print(f"You:{score_player} - computer:{score_computer}")
    
    if computer == "paper" and player ==0:
        score_computer +=1
        print("haha loser!")
        print(f"You:{score_player} - computer:{score_computer}")
    
    if computer == "scice" and player == 1:
        score_computer +=1
        print("haha loser!")
        print(f"You:{score_player} - computer:{score_computer}")

if score_player == 5:
    print("You Win!")
else:
    print("computer Win :")
    

import calendar     