class Animal:
    def sleep(self):
        print("ALL ARE SLEEPING FOR TOMORROW FIGHT")
    def passs(self):
        print("ALL WERE PASSIG SAFELY IN ROAD")

class Dear(Animal):
    pass
class Fish(Animal): 
    pass
 
fish=Fish()
dear=Dear()
(fish.sleep())
(fish.passs())
dear.sleep()

dear.passs()
Animal().sleep()