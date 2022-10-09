import random

while True:
    choices = ("rock", "paper", "scissors")
    computer = random.choice(choices)
    player=None
    while player not in choices:
        player = input("enter rock,scissors,paper: ").lower()
    if player==computer:
        print("player :",player)
        print("computer :",computer)
        print("It's is a tie")
    elif player=="rock":
        if computer=="paper":
            print("player :", player)
            print("computer :", computer)
            print("you won")
        if computer == "scissors":
            print("player :", player)
            print("computer :", computer)
            print("you lose")
    elif player=="paper":
        if computer=="rock":
            print("player :", player)
            print("computer :", computer)
            print("you won")
        if computer=="scissors":
            print("player :", player)
            print("computer :", computer)
            print("you lose")
    elif player=="scissors":
        if computer=="rock":
            print("player :", player)
            print("computer :", computer)
            print("you lose")
        if computer=="paper":
            print("player :", player)
            print("computer :", computer)
            print("you win")
    play_again=input("You want to play again yes or no :" ).lower()
    if play_again!="yes":
        break
print("Thank you for playing the game")
