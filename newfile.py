import random
n=random.randint(1,100)
guesses=0
a=0
while a!=n:
    a=int(input("Enter your prediction:  "))
    guesses+=1
    if a>n:
        print("guess your number lower to this")
    elif a-n==1 or a-n==2 or a-n==3 or a-n==4 or a-n==5:
        print("You are really very much close just guess slighter lower")
    elif -n-a==1 or n-a==2 or n-a==3 or n-a==4 or n-a==5:
        print("You are really very much close just guess slighter higher")
    elif n-a==5 or n-a==6 or n-a==7 or n-a==8 or n-a==9 or n-a==10:
        print("You are really closer just guess slighter higher")
    elif a-n==5 or a-n==6 or a-n==7 or a-n==8 or a-n==9 or a-n==10:
        print("You are really closer just guess slighter lower")
    
    else:
        print("Predict your number higher to this")
    
print(f"You Cracked it Really in just {guesses} guesses")