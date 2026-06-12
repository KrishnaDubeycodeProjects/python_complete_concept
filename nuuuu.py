# num = 13
#   # You can change this value
# flag = False

# if num <= 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num,"This is not prime number")
#             break
        
   
#     else:
#         print(num, "is a prime number")

def prime(n):
    pro=[]
    noob=[]
    num=2
   
    while n:
        is_prime=True
    
        for i in range(2,num):
          if  num%i==0:
            noob.append(num)
        # num+=1
        # print(num,"is not a prime number")
        # n-=1
            is_prime=False
        
            break
    
        if is_prime:
            pro.append(num)
        num+=1
        n-=1
       
   
      
    return pro,noob

a,b=prime(100)
print("prime numbers:",a)
print(len(a))
print("Non-prime numbers:",b)
print(len(b))