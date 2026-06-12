import random

name=input("enter your full name:")
A=["rock","paper","scissors"]
B=random.choice(A)
N1="rock"
N2="paper"
N3="stone"
user=input("enter your move from rock,paper,scissors only:-  ").lower()
if user[0].lower()==N1[0]:
    
    user=N1
elif user[0].lower()==N2[0]:
    user=N2
    
elif user[0].lower()==N3[0]:
    user=N3


while user not in A:
    user=input("enter your move from rock,paper,scissors only:-  ").lower()

print("computer input:",B)
print("{}  input: {}".format(name,user))

if user == "scissors":
    if B == "paper":
        print(f"hey! {name} you won")
    elif B == "rock":
        print(f"hey!\{name} congratulation you los ;) ):")
elif B == "scissors":
    if user == "paper":
        print(f"hey! {name} congratulation you los ;) ):")
    elif user ==  "rock":
        print(f"hey!{user}  you won")
elif  user == "paper":
    if B == "rock":
        print(f"hey!{name}  you won")
elif B == "paper":
    if user == "rock":
        print(f"hey!{name} congratulation you los ;) ):")
elif user == B:
    print(f"HEY! {name} it's a tie!")

