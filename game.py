import random

name=input("enter your full name:")
A=["rock","paper","scissors"]
B=random.choice(A)
user=input("enter your move from rock,paper,scissors only:-  ").lower()

while user not in A:
    user=input("enter your move from rock,paper,scissors only:-  ").lower()

print("computer input:",B)
print("{}  input: {}".format(name,user))
if (user=="rock" and B=="paper") or (user=="scissors" and B=="rock") or (user=="paper" and B=="scissors"):
    print("hey! congratulation you los ;) ):")
elif user==B:
    print("It's a tie!")
else:
    print("hey! you won")
