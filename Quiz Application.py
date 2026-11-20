name = input("enter name : ")
year_of_study  = input("enter year of college : ")
college = input("enter college : ")
import time
timer = 5
for x in range(0,timer):
    print(x)
    time.sleep(1)
print("Start the Quiz")
score = 0
print("1 " + "which is the largest continent of the world ?")
print("a " + "Japan")
print("b " + "India")
print("c " + "Asia")
print("d " + "Africa")
answer = input("enter your answer : ")
correct = "c"
if answer == correct:
   print("Right answer")
   score += 1
   print("You score +1")
else:
    print("Wrong answer")
print("2 " + "which is the smallest state of India ?")
print("a " + "Goa")
print("b " + "Rajasthan")
print("c " + "bihar")
print("d " + "Himachal")
answer = input("enter your answer : ")
correct = "a"
if answer == correct:
   print("Right answer")
   score += 1
   print("You score +1")
else:
    print("Wrong answer")
print("3 " + "which is the longest river of india ?")
print("a " + "Tapti")
print("b " + "Ganga")
print("c " + "Yamuna")
print("d " + "Narmada")
answer = input("enter your answer : ")
correct = "b"
if answer == correct:
   print("Right answer")
   score += 1
   print("You score +1")
else:
    print("Wrong answer")
print("4 " + "who is the capital of India ?")
print("a " + "Bihar")
print("b " + "Delhi")
print("c " + "Indore")
print("d " + "Mumbai")
answer = input("enter your answer : ")
correct = "b"
if answer == correct:
   print("Right answer")
   score += 1
   print("You score +1")
else:
    print("Wrong answer")
print("5 " + "india's pink city is ?")
print("a " + "Bihar")
print("b " + "Delhi")
print("c " + "Indore")
print("d " + "jaipur")
answer = input("enter your answer : ")
correct = "d"
if answer == correct:
   print("Right answer")
   score += 1
   print("You score +1")
else:
    print("Wrong answer")
print("You completed the Quiz")
print("------------Wait for 5 sec for you quiz report--------------")
import time
timer = 5
for x in range(0,timer):
    print(x)
    time.sleep(1)
print("Your Quiz report is completed")
print(f"Name : {name}")
print(f" Year of college : {year_of_study}")
print(f"College name : {college}")
print("This is Certified that you completed the quiz 🎉🎉🎉")
print(f"-------YOUR SCORE IS {score}")


    
  
  
   
  

    
        
    
