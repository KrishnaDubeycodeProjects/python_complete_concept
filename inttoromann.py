# num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
# sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
# number=int(input("Enter your love  number :  "))
# res=""
# i=12
# while number:
#     if number//num[i]==1:
     
#         number%=num[i]
#         res+= sym[i]
#     i-=1
# print(res)
    # roman to int
num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
roman=input("Enter your roman number: ")
key=0
total=0
add=0

for i in range(len(roman)-1):
    if  num[sym.index(roman[i])] < num[sym.index(roman[i+1])]:
        x=sym.index(roman[i])
        
        total-=num[x]
        i+=1
    else:
        x=sym.index(roman[i])
        add+=num[x]
        i+=1
add+=num[sym.index(roman[-1])]
print(f"Your number is: {add+total}")








