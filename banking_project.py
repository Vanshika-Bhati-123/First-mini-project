# we created a small project of banking in which a person can see how much money is credited or debited from the bank and in last is ahows the exact balance
class account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
    def debit(self ,amount):
        self.balance -= amount
        print("Rs", amount,"was debited")
        print("Total balance = ",self.get_balance())
    def credit(self ,amount):
            self.balance += amount
            print("Rs", amount,"was credited")
            print("Total balance = ",self.get_balance())
    def get_balance(self):
         return self.balance
acc1 = account(10000,12456)
acc1.debit(500)
acc1.credit(900)