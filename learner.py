#global scope and local scope
#LEGB
"""L=local    E=ENCLOSING 
   G=GLOBAL   B=BUILT-IN"""
A="you are good boy"
def thunder_blast(data):
    A="you are a bad boy"
    print(A)
    

thunder_blast(A)
print(A)
def a(*args):
    sum=2
    for i in args:
        sum+=i
        return(sum)
print(a(3,4,8))


