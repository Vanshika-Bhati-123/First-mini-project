print("------------Banking Management system-------------")
bank_details = []
Transaction_history = []
while True :
 print("Create account")
 print("Check balance")
 print("Deposit money")
 print("Withdraw money")
 print("Transaction history")
 print("Exit")
 User = int(input("enter your choice : "))
 if User == 1:
   Name = input("enter name : ")
   Acc_no = int(input("enter acc no : "))
   deposit = int(input("enter initial deposit amount : "))
   bank_details.append([Name,Acc_no,deposit])
 if User == 2:
      Acc_no_enter = int(input("enter acc_no : "))
      for item in bank_details:
       if Acc_no_enter == Acc_no:
        print("Current balance is :" + str(deposit))
       else:
        print("no record")
 if User == 3:
    Acc_no_enter = int(input("enter acc_no : "))
    deposit_amount = int(input("enter deposit amount : "))
    if Acc_no_enter == item[1]:
     for item in bank_details:
      item[2] = item[2] + deposit_amount
     Transaction_history.append(["Deposit", Acc_no_enter,deposit_amount])
     print("Updated balance After deposit is is : " + str(item[2]))
 if User == 4:
    Acc_no_enter = int(input("enter acc_no : "))
    withdraw_amount = int(input("enter withdraw amount : "))
    for item in bank_details:
      if Acc_no_enter == item[1]:
       if item[2] >= withdraw_amount : 
         item[2] = item[2] - withdraw_amount
      Transaction_history.append(["withdraw", Acc_no_enter,withdraw_amount])
      print("Updated balance After withdraw is : " + str(item[2]))
 if User == 5:
    if len(Transaction_history) == 0 :
     print("No Transaction history")
    else:
      for item in Transaction_history:
       print("Type : ", item[0])
       print("Account : ", item[1])
       print("Amount : ", item[2])
 if User == 6:
    print("Exit")
    break

    
       

    
  
   
  

    
        
    
