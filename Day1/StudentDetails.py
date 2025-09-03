sno=int(input("Enter Student Number:"))
sname=input("Enter Student Name:")
smarks=map(int,input("Enter 3 Subjects Marks:").split())
total=sum(smarks)
avg=total/3
print("Total Marks=",total,"\nAverage of Student=",round(avg,2))