def new_func():
    for i in range(1,10):
     print(i)
     i=sum(range(1,10))
    print(i)
    def a(*many):
     many=list(many)
     many[0]= 45
     sum=0
     for i in many:
      sum+=i
     return sum
    b=a(2,4,5,44,64,4,6)
    print(b)
new_func()

