# Function to accept the product name and quantity
def accept_product():
    buyingData={}
    product_details= True
    
    while product_details:
        details = str( input("Press A to continue and Q to quit: \n "))
        if details == 'A':
            product= str(input("Enter product: "))
            quantity= int(input("Enter quantity: "))
            buyingData.update({product:quantity})
        elif details == 'Q':
            product_details = False
        else:
            print("please select correct option")
           
    return buyingData 
   

accept_product()           
