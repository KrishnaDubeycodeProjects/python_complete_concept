

# with open("cetcell.py") as p:
#    A= p.read()
#    print(A)
Af = []
listed_values = [3, 5, 6, 2, "f", "Hate"]
for i in range(0, 6):
    D = listed_values[i]
    if isinstance(D,int):
        Af.append(D)
print(Af)

print(listed_values)
