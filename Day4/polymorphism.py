class Payment:
    def pay(self,amount):
        pass
class CashPayment(Payment):
    def pay(self,amount):
        print("Paid",amount,"in Cash")
    
class CardPayment(Payment):
    def pay(self,amount):
        print("Paid",amount,"using Credit/Debit Card")

class UPIPayment(Payment):
    def pay(self,amount):
        print("Paid",amount,"using UPI")

payments=[CashPayment(),CardPayment(),UPIPayment()]
for i in payments:
    i.pay(1000)