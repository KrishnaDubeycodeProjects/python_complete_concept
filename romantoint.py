number=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
roman=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
num=int(input("Enter your number to get its romman number: "))
i=12
res=" "
while num:
    if num//roman[i]:
        num%=roman[i]
        res+=number[i]
    i-=1
      
print(res)


