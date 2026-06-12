# name="karan"
# print(name[-6:])    # See magic print(name[-5:-1])just think how you can print to "n" also in karan
# print("Hello world")
# name_checking=" helo World "
# print(name_checking.capitalize())
# print(name_checking.startswith(" hello"))
# print(name_checking.rstrip())
# print(name_checking.strip())
# print(name_checking.upper())

# print(name_checking.isalnum())
# print(name_checking.isdigit())
# print(name_checking.isascii())
# print(name_checking.encode())
# print(name_checking.lstrip())
# print(name_checking.split("  "))
# print(name_checking.isalpha())


#practice set 4 
# student1=input("Enter your marks studeent1: ")
# student2=input("Enter your marks studeent2: ")
# student3=input("Enter your marks studeent3: ")
# student4=input("Enter your marks studeent4: ")
# student5=input("Enter your marks studeent5: ")
# student6=input("Enter your marks studeent6: ")
# A=[student1,student2,student3,student4,student5,student6]
# A.sort()
# print(A)
# sum1=[4864]
# sum2=[4589]
# print("your sum of 2 list having 4 digitss number: ",sum1+sum2)
   
# list=[4,6,5,3]
# total=0
# for i in list:
#     total+=i
# print("your sum of the numbers in the list: ",total)


#dictonaries shortcut:


# A="krishna dubey"
# total="0"
# for i in A:
#     total+=i
#     print(total)



# A="93748495485638"

# total=" "
# for i in A:
#     total+=i
#     print(total.split("-"))

# translation={
#     "hindi":"English",
#     "naam" : "name",
#     "Nhi pata": "Don't Know",

#     "Kaise ho!": "How are you?"

# }
# print(translation.items())
# number=""
# while len(number)!=8:
#  number=(input("Enter youn eight digit number"))
#  number=str(number)
# for i in number:
#  print(i)

# sets={18,"18"}
# print(sets)
# print(sets.intersection({18,"18"}))
# print(sets)

# s= set()

# s.add(20.0)   #float or int same if it comes then it is req to check which number comes first is allow in sets
# s.add(20)
# s.add(19.0)
# s.add("20")
# print(s)
# print(len(s))

s={}  #it is dict not set be carefull!
# key1=input("Enter your first student: ")
# language1=input("Enter your fav language: ")
# key2=input("Enter your second student: ")
# language2=input("Enter your fav language: ")
# key3=input("Enter your third student: ")
# language3=input("Enter your fav language: ")
# key4=input("Enter your fourth student: ")
# language4=input("Enter your fav language: ")


# Fav_language={
#     key1:language1,
#    [ key2]:language2,
#    ( key3,): language3,
#    key4 + "Last name": language4}
# print(Fav_language.items())







# Create an empty dictionary
# fruit_counts = {}

# # Add fruits and their quantities
# fruit_counts["apple"] = 3
# fruit_counts["banana"] = 2
# fruit_counts["orange"] = 5

# # Print the fruit counts
# print("Fruit Counts:")
# for fruit, count in fruit_counts.items():
#     print(f"{fruit}: {count}")


# only non-mutable or mutable thing can added in mutable attributes type
#and non- mutable thing canoot enter in non-mutable things




#chapter 6- practice set
# list=[,]

# while len(list)==4:
#  list=(input("Enter your number:" ))
#  print("To check the biggest numbers donot enter 4 numbers")

# list.sort()
# print(list[])

# student=input("Enter your name: ")
# marks_1=int(input("Enter your english percentage: "))
# marks_2=int(input("Enter your math percentage: "))
# marks_3=int(input("Enter your social science percentage: "))
# marks_4=int(input("Enter your physics percentage: "))
# percentage=((marks_1+marks_2+marks_3+marks_4)/400)*100
# percentage=int(percentage)
# if (percentage>=40) and (marks_1>=33) and (marks_2 >=33) and( marks_3>=33) and (marks_4)>=33:
#     print()
#     print("hey! you full name is: ",student)
#     print("you passed in all subject")
#     print(f"congratualtions on score as you score: {percentage}%")
#     print(f"""english: {marks_1}
#               Math: {marks_2}
#               Social science: {marks_3}
#               physics: {marks_4}""")
# else:
#     print()
#     print("hey! you full name is: ",student)
#     print(f"you failed! as you scored: {percentage}%")
#     print(f"""english: {marks_1}
#               Math: {marks_2}
#               Social science: {marks_3}
#               physics: {marks_4}""")
# if marks_1<33:
#     print("you failed in english with this percentage",marks_1)
# else:
#     pass
# if marks_2<33:
#     print("you failed in Math with this percentage",marks_2)
# else:
#     pass
# if marks_3<33:
#     print("you failed in Social Science with this percentage",marks_3)
# else:
#     pass
# if marks_4<33:
#     print("you failed in Physics with this percentage",marks_4)
# else:
#     pass




#2
# if len(user_name)<=10:
#     print(user_name)
# else:
#      print("sorry! your username cannot exceed more than 10\"letters\"")



name=input("Enter yourr name: ")
name=list(name)
print(type(name))
