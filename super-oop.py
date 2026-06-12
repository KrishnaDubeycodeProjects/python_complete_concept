# class cube:
#  def __init__(self,length):
#     self.length=length
#     return length**3
# class square(cube):

#   def __init__(self,breadth,length):
#    super().__init__(length)
#    self.breadth=breadth
#    return 6*length*breadth**2
# b=cube(5)
# A=square(4,5)
class Cube:
    def __init__(self, length):
        self.length = length

class Square(Cube):
    def __init__(self, breadth, length):
        super().__init__(length)
        self.breadth = breadth

b = Cube(5)
A = Square(4, 5)
print(b.length**3, 6 * A.length*A.breadth*2)



# print(A)

