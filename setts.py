utensil={"knife","hat","kitchen"}
# (utensil.add("spoon"))
# (utensil.clear())
# utensil={"knife","hat","kitchen"}
# print(utensil)
b={8,"dv"}
b.add("pop")
# print(b.difference(utensil))
# for key in utensil:
#     print(key)
print(utensil.intersection(b))
print(b.isdisjoint(utensil))
print(utensil)
# (utensil.discard("knife"))
print(utensil.issuperset(utensil))
(utensil.intersection_update(b))
print(utensil)