def apply_discount(price,discount_percent):
    dis_amount=price*discount_percent/100
    final=price-dis_amount
    return final
def add_gst(price,gst_percent=18):
    gst=price*gst_percent/100
    final=price+gst
    return final
def generate_invoice(cart,discount_percent=0,gst_percent=18):
    print("------INVOICE------")
    print(cart)
    print("-------------------")
    price=0
    for i in cart.values():
        price+=i
    print("Subtotal:",price)
    print(f"After 10% discount:{apply_discount(price,discount_percent)}")
    print(f"After 18% GST:{add_gst(apply_discount(price,discount_percent),gst_percent)}")
    print("-------------------")
    print("Thank You Visit Again")