# def func(*stuff):
#     summ=0
#     for i in stuff:
#         summ+=i
#     return summ

        
# func(2,4,45,6,6,3,2,54)
# print(func)
#   args are tuple
# def func(*stuff):
#     summ = 0
#     for i in stuff:
#         summ += i
#     return summ

# add two list and reverse them
def funci(l1,l2):
    l1=[2,4,56,6,4,3]
    l2=[3,4,6,7,34]

    min_length=min(len(l1),len(l2))
    c=[]
    for i in range (min_length):
        A=l1[i]+l2[i]
        c.append(A)
    # a=len(l1)
    # b=len(l2)
    if min_length<len(l1):
        c.append(l1[min_length])
    if min_length<len(l2):
        c.append(l2[min_length])
    c.reverse()
    print(c)
    # l1=[35,46]
    # l2=[3,5,7,7]
funci([],[])


        



    