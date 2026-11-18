list = []
while True:
 print("---------------Student Management system---------------")
 print("Add student")
 print("View students")
 print("Search student")
 print("Delete student")
 print("Exit")
 User = input("enter your choice : ")
 if User == "1":
  Student_name = input("enter student name : ")
  Roll_no = int(input("enter roll no. : "))
  Student_marks = int(input("enter marks : "))
  list.append([Student_name,Roll_no,Student_marks])
 elif User == "2":
  if len(list) == 0:
   print("No student record found")
  else:
   for item in list:
    print("Student name = ", item[0])
    print("Roll no = " , item[1])
    print("Student marks = ",item[2])
 elif User == "3":
  Enter_Roll_no = int(input("enetr roll no : "))
  for item in list :
   if Enter_Roll_no == item[1]:
      print(item)
   else:
    print("No student record")
 elif User == "4":
     Enter_Roll_no = int(input("enetr roll no : "))
     for item in list:
       if Enter_Roll_no == item[1]:
         list.remove(item)
         print("Record Deleted")
       else:
        print("No record")
 elif User == "5":
      print("exit")
 break
   
  

    
        
    
