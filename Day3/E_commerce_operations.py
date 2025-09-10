cart=[]

def add(product):
    cart.append(product)
    print(f"Product {product} added to cart.")
def remove(product):
    if product in cart:
        cart.remove(product)
        print(f"{product} removed from cart.")
    else:
        print(f"{product} not found in cart.")

def search(product):
    if product in cart:
        print(f"Yes,'{product}' is in the cart.")
    else:
        print(f"{product} is not in the cart.")

def display():
    if cart:
        print("Cart:",cart)
    else:
        print("Cart is empty")

def count():
    print(len(cart))

def sort():
    print(sorted(cart))

def clear():
    cart.clear()



print("Cart Operations:")
print("1.Add Product\n2.Remove Product\n3.Search Product\n4.Display Cart\n5.Count Products\n6.Sort the cart items alphabetically\n7.CLear the Cart\n8.Exit")
while True:
    choice=int(input("Enter choice:"))
    if choice==1:
        p=input("Enter product to add:")
        add(p)
    elif choice==2:
        r=input("Enter product to remove:")
        remove(r)
    elif choice==3:
        s=input("Enter product to search:")
        search(s)
    elif choice==4:
        display()
    elif choice==5:
        count()
    elif choice==6:
        sort()
    elif choice==7:
        clear()
    else:
        break