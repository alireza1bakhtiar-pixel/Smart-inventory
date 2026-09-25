import csv
from product import Product

product_list = []


def save_product(product):
    with open("products.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                product.id,
                product.name,
                product.category,
                product.price,
                product.quantity,
            ]
        )
        product_list.append(product)


def load_product():
    try:
        with open("products.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                p = Product(int(row[0]), row[1], row[2], int(row[3]), int(row[4]))
                product_list.append(p)
    except FileNotFoundError:
        print("file not found !!")


def remove_product_by_id(product_list, product_id):
    for product in product_list:
        if product.id == product_id:
            product_list.remove(product)
            print("product removed successfully.")
            return True

    print("product with this ID was not found.")
    return False


def remove_product_by_name(product_list, product_name):
    temp_list = []
    for i in product_list:
        if product_name == i.name:
            temp_list.append(i)
    if len(temp_list) == 0:
        print("product not found.")
        return
    elif len(temp_list) == 1:
        remove_product_by_id(product_list, temp_list[0].id)
        return
    else:
        for i in temp_list:
            print(f"ID: {i.id}, name: {i.name}")
        id_by_name = int(input("which one of them you want to remove enter an id: "))
        remove_product_by_id(product_list, id_by_name)


def remove_product_by_category(product_list, category):

    temp_list = []
    for i in product_list:
        if category == i.category:
            temp_list.append(i)
    if len(temp_list) == 0:
        print("category does not exists !")
        return
    else:
        for i in temp_list:
            product_list.remove(i)

        print(
            f"{len(temp_list)} products from this category were removed successfully!"
        )


def remove_product():
    print("1. Remove by ID")
    print("2. Remove by Name")
    print("3. Remove by Category")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        product_id = int(input("enter product id: "))
        remove_product_by_id(product_list, product_id)

    elif choice == 2:
        product_name = input("enter product name you want to remove:")
        remove_product_by_name(product_list, product_name)
    elif choice == 3:
        product_category = input("please enter categry to remove:")
        remove_product_by_category(product_list, product_category)
        
    rewrite_products()


def rewrite_products():
    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for i in product_list:
            writer.writerow([i.id, i.name, i.category, i.price, i.quantity])


load_product()

print("*$* WELCOME TO SMART INVENTORY *$*")


while True:

    print(
        "1.ADD PRODUCT\n"
        "2.REMOVE PRODUCT\n"
        "3.UPDATE PRODUCT\n"
        "4.SEARCH PRODUCT\n"
        "5.SHOW ALL PRODUCTS\n"
        "6.SHOW PRODUCTS VALUE\n"
        "7.SAVE/LOAD DATA"
    )

    choice = int(input("please enter your choice :"))
    if choice == 1:
        p_id = int(input("Enter ID : "))
        p_name = input("Enter Product Name: ")
        p_category = input("Enter Product Category: ")
        p_price = int(input("Enter Product price: "))
        p_quantity = int(input("Enter Quantity of Product: "))

        p = Product(p_id, p_name, p_category, p_price, p_quantity)

        save_product(p)
    elif choice == 2:
        remove_product()
