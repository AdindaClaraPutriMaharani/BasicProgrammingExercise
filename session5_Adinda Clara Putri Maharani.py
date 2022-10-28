# Descriptive
# Make variable of the product
# Maake variable price of the product
# Make variable percent of the product
# input product name
# input product price
# calculate the price of the product 
# price of the product * product / 100
# print the price of the product along with the product name



while(True):
    
    all_capital = 0
    all_profit = 0
    product_name = input("\nInput product name : ")
    product_price = int(input("Input product price : "))
    amount_items = int(input("The amount of the product : "))
    purchased_product = int(input("How many products did you buy : "))
    total_profit = int(product_price * purchased_product)
    stock = int(amount_items - purchased_product)
    
    percent = 10
    percent_price = int(product_price * percent/ 100)
    
    print("\n================================================")
    print("================ R E C E I P T ===============")
    print("================================================")
    print("selling price per item               : Rp.", product_price + percent_price)
    print("number of items sold                 : ", purchased_product, "pcs")
    print("Total selling price                  : Rp.", product_price * purchased_product) 
    print("profit                               : Rp.", total_profit * percent_price)
    print("\n-----------------------------------------")
    
    apakahlanjut = input("Do you want to buy something else? Y or N : ")
    if (apakahlanjut != 'y'):  
        break 
