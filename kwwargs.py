# file detection
# import os
# paths="C:\\Users\\Krishana dubey\\OneDrive\문서\\Document1.docx"
# if os.path.exists(paths):
#     print("your File exist")
# else:
#     print("YOur file does not exist")
# if os.path.isfile(paths):
#     print("Your file is a file not a folder")
# if os.path.isdir(paths):
#     print("YOur file is a folder")
    
# with open("text.txt") as file:
#  print(file.read())
#  file.close()
text="HEY BRO I MUST BORED PASSWORD + LOL"
with open("text.txt","w") as file:
 file.write(text)