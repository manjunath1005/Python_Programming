class BankAccount:
    __balance=0
    def amount(self,amt):
        self.__balance+=amt
        print("Amount Deposited:",amt)
    def withdraw(self,amt):
        if amt>self.__balance:
            print("Insufficient Balnce")
        else:
            self.__balance-=amt
            print("Amount Withdrawn:",amt)
    def get_balance(self):
        return self.__balance

B1=BankAccount()
B1.amount(5000)
B1.withdraw(2000)
print("Balance:",B1.get_balance())