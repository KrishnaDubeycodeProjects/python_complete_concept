
# try:
#  age=input("enter your age:")
#  age=int(age)
#  name=input("enter your name:")
#  name=str(name)
#  print("hello buddy 'congratulation' on signup {} and your age is {}".format(name,age))
# except ValueError or NameError:
#   print("idiot! you are doing wrong step recorrent by entering restart")

try:
    age = input("Enter your age: ")
    age = int(age)  # Convert age to integer

    name = input("Enter your name: ")
    if not name.isalpha():
        raise ValueError("Name must contain only letters.")  # Raise an error if name is not valid

    print("Hello buddy, 'congratulations' on signup {} and your age is {}".format(name, age))

except ValueError as e:
    print(f"Idiot! You are doing wrong step. Please restart and enter valid information. Error: {e}")
    