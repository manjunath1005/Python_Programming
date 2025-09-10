def add(dic,key,val):
    dic[key]=val
    return dic
def remove(dic,key):
    if key in dic:
        del dic[key]
    else:
        print("Key not found")
    return dic
def search(dic,key):
    if key in dic:
        return dic.get(key)
    else:
        print("Key not found")
def update(dic,key,val):
    if key in dic.keys():
        dic[key]=val
    else:
        print("Key not found")
    return dic
def display(dic):
    for key,val in dic.items():
        print(f"{key}: {val}")
def count(dic):
    print("Number of books:",len(dic))
def check(dic,val):
    if val in dic.values():
        print("Book is available")
    else:
        print("Book is not available")

library=eval(input("Enter the initial library dictionary:"))
while True:
    print("\n1.Add Book\n2.Remove Book\n3.Search Book\n4.Update Book\n5.Display Books\n6.Count Books\n7.Check Book Availability\n8.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        key=input("Enter book ID:")
        val=input("Enter book name:")
        library=add(library,key,val)
    elif choice==2:
        key=input("Enter book ID to remove:")
        library=remove(library,key)
    elif choice==3:
        key=input("Enter book ID to search:")
        result=search(library,key)
        if result:
            print(f"Book found: {result}")
    elif choice==4:
        key=int(input("Enter book ID to update:"))
        val=input("Enter new book name:")
        library=update(library,key,val)
    elif choice==5:
        display(library)
    elif choice==6:
        count(library)
    elif choice==7:
        val=input("Enter book name to check availability:")
        check(library,val)
    elif choice==8:
        break
    else:
        print("Invalid choice")