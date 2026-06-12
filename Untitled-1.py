# A= "qzqzqzqzqzqzqdzqzqzqzqszqzqzzqzqzqzqzqdzqzqzzqzqzqszqszqzqzqzqzqzsqazqzqzqqzqzqzwqzqzqzaqzqzzzqzqwqzqzqzqzqazqzqzqzsqwzqzqzqzqzssqzqzqzqzqzsqzqzqzqzqzqzqzqzqzqzqzqzszqzqzqzqzqzqzqzqzqz"
# print(A.count("z"))

# #positional arguments
# def multiplier(num1,num2):
#     print(num1*num2)

# multiplier(6,8)


# #addvance
# def multiplier(num1,num2):
#     ffinal_edit=num1*num2
#     return ffinal_edit
# A=multiplier(7,16)
# print(A)
# #keyword arguments has every key has unique identifier
# name=input("enter your name:")
# age=int(input("enter your age:"))
# job=input("whats you do:")
# def intro(name,age,job):
#  print("hi "+" "+name+" "+str(age)+" "+job)
# intro(name,age,job)

#     #nested keywords
# num=input("enter your number:")
# num=float(num)
# num=abs(num)
# num=round(num)
# print(num)
# print(round(float(input("enter you first any number"))))
def check_age(age):
    if age >= 18:
        return True
    else:
        return False

print(check_age(20))  # Prints True
