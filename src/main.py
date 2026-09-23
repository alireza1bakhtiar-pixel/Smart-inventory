from product import Product
print("*$* WELCOME TO SMART INVENTORY *$*")
while True:
    print("1.ADD PRODUCT\n" \
    "2.REMOVE PRODUCT\n" \
    "3.UPDATE PRODUCT\n" \
    "4.SEARCH PRODUCT\n" \
    "5.SHOW ALL PRODUCTS\n" \
    "6.SHOW PRODUCTS VALUE\n" \
    "7.SAVE/LOAD DATA")
    choise = int(input("please enter your choise :"))
    if choise == 1:
        p_id = int(input("Enter ID : "))
        p_name = input("Enter Product Name: ") 
        p_category = input("Enter Product Category: ")
        p_price = int(input("Enter Product price: "))
        p_quantity = int(input("Enter Quantity of Product"))

        p = Product(p_id,p_name,p_category,p_price,p_quantity)
        print(p)
            