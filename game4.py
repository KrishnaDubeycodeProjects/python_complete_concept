#snake water gun game
import random

Name=""
user_input=int(input("Enter your number 1='snake , 2='water' 3='gun': "))
if user_input==1:
   Name="snake"
elif user_input==2:
    Name="water"
elif user_input==3:
    Name="gun"
A=["snake","water","gun"]
computer=random.choice(A)




print("computer choice: ", computer)
if Name=="water":
    if computer=="snake":
        print("You lose")
    if computer=="gun":
        print("You won!")
elif computer=="gun":
    if Name=="snake":
        print("You lose!")
elif Name=="gun":
    if computer=="snake":
        print("You won!")
    if computer=="water": 
        print("You lose!")
if Name=="snake":
    if computer=="water":
        print("You won!")
elif Name==computer:
    print("Tie! let's play again")





