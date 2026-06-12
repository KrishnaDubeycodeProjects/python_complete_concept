question={"1.who invented pyton:": "A",
          "2.In which year python was invented:":"A",
          "3.For which comedy group python tributed them": "A"
          
          
          }
options=[("1:A.guido van rossum\n", "B.M.s Dhoni\n", "C.Yuzi bhai\n", "D.Ashish vinchi\n"),
         ("2:A.1991\n","B.1776\n","C.1999\n","D.2000\n"),
         ("3:A.Monty python\n","B.Comedy group\n","C.Dil ki batein\n","D.Charlie chaplin\n")
         
         ]
guess=[]
segregate= 0
guesses=[]
letter=["A","B","C","D"]
ANSWERSET=["A","A","A"]
count=0
for k in question:
 print(k)
 print("#-------------------")
 for i in options[segregate]:
  print(i)

 segregate+=1
 
 guess=input("enter your option in letter only: ").upper()
 guesses.append(guess)
 print("HEY! user you have entered this: ",guess) 
 if guess== question.get(k):
    print("Hurray!,congratulation you won 1 point.")
    count+=1
    print("your total point is",count)

 else: 
    print("you lost try again to win next question")
    count+=0
print("congratulations! you have made it by scoring  '{}' points".format(count))
print("your answer sheet:  ",guesses)

print("correct answer key is:",ANSWERSET) 


    

 