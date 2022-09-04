# Function to accept the product name and quantity
def accept_product():
    buyingData={}
    product_details= True
    #product_detail is our flag variable with default value of True
    while(product_details):
        details=input("Press A to continue and Q to quit ")
    if details== 'A':
        product=str(input("Enter product \n"))
        quantity=int(input("Enter quantity \n"))
    elif details== 'Q':
        product_details= False
    else:
        print("please select correct option")

   # print(update(buyingData))
    return accept_product        
