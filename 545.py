import random
x=random.randint(1,6)
print(x)
my_place=["tails","heads"]
x=random.choices(my_place)
print(x)
cards=[1,2,3,4,5,6,7,8,9,10,"j","k","a","q"]
A=random.shuffle(cards)
print(cards)
# read tuples
# Exception
try:
 age=(input("your age is:"))
 age=int(age)
 print(age)                                 #very good question you did
except Exception :                           
 print("something went wrong:(\n\t try again later")
age=str(age)
print(type(age))
print(f"you have entered:'{age}' " )
print("instead of <class>int type chooses string")

