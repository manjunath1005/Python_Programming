cno=int(input("Enter Consumer Number:"))
cname=input("Enter Consumer Name:")
lmr=int(input("Enter Last Month Reading:"))
pmr=int(input("Enter Present Month Reading:"))
cpu=3.8
Total_Units=pmr-lmr
cost=Total_Units*cpu
print("Customer Details:\nCustomer No. :",cno,"\nCustomer Name :",cname,"\nLast Month Reading :",lmr,"\nPresent Month Reading :",pmr)
print("Total Units :",Total_Units,"\nTotal Cost=",cost)