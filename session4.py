#create product name to variable
product_name = input("the product name : ")

#input product price to variable
product_price = int(input("product price : "))

#set 10% variable
persen = 10

#input amount of items
amount_items = int(input("how many product do you buy : "))

#the money spent
print("money spent : ", product_price * amount_items)

#calculate the 10% from the product price
profit = product_price * persen / 100
profit_items = profit * amount_items
print("profit 10% per item: " + str(profit))
print("total profit all items : " + str(profit_items))

#sale price
sale_price = product_price + int(profit)
total_selling = sale_price * amount_items

#print the final product price
print(product_name, " sale price per item is : ", sale_price )
print(product_name, " total sale price is : ", total_selling )

#items sold
items_sold = int(input( "how many product have been sold : "))
profit_sold = profit * items_sold
print("profit from items sold : " + str(profit_sold))
