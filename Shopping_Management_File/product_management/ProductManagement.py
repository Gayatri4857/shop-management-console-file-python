import os

from product_management.Product import Product
from product_management.ProductOptions import ProductOptions


class ProductManagement:
    al = []
    file_path = r"C:\Users\hemag\PycharmProjects\Shopping_Management_File\product_management\Products.csv.py"

    @staticmethod
    def product_management():
        can_i_keep_running_program = True

        while can_i_keep_running_program:
            print("*** WELLCOME TO PRODUCT MANAGEMENT ****")
            print("\n")
            print("What would you like to do ?")
            print("1. Add Product:")
            print("2. Edit Product:")
            print("3. Delete Product:")
            print("4. Search Product:")
            print("5. Quit Product:")

            option_selected_by_product = int(input())

            if option_selected_by_product == ProductOptions.QUIT:
                ProductManagement.save_data_to_file()
                print("!! Program closed..")
                can_i_keep_running_program = False

            elif option_selected_by_product == ProductOptions.ADD_PRODUCT:
                ProductManagement.add_product()
                print("\n")

            elif option_selected_by_product == ProductOptions.SEARCH_PRODUCT:
                sn = input("Enter Product Name to Search: ")
                ProductManagement.search_product(sn)
                print("\n")

            elif option_selected_by_product == ProductManagement.EDIT_PRODUCT:
                edit_product_name = input("Enter the Product Name to Edit:")
                ProductManagement.edit_product(edit_product_name)
                print("\n")

            elif option_selected_by_product == ProductManagement.DELETE_PRODUCT:
                delete_product_name = input("Enter the peroduct name to delete:")
                ProductManagement.delete_product(delete_product_name)
                print("\n")

    @staticmethod
    def add_product():
        product_object = Product()
        product_object.productName = input("Product Name:")
        product_object.productID = input("Product ID:")
        product_object.productPrice = input("Product Price:")
        product_object.productQuality = input("Product Quality:")
        product_object.productCategory = input("Product Category:")
        ProductManagement.al.append(product_object)

    @staticmethod
    def search_product(product_name):
        for product in ProductManagement.al:
            if product.productName.lower() == product_name.lower():
                ProductManagement.print_product_details(product)
                return
            print("Product not found!!")

    @staticmethod
    def search_product(product_name):
        for product in ProductManagement.al:
            if product.productName.lower() == product_name.lower():
                ProductManagement.print_product_product_details(product)
                return
        print("User not found")

    @staticmethod
    def delete_product(product_name):
        for product in ProductManagement.al[:]:
            if product.productName.lower() == product_name.lower():
                ProductManagement.al.remove(product)
                print(f"Product {product.productName} has been deleted..")
                return
        print("Product not found..")

    @staticmethod
    def edit_product(product_name):
        for product in ProductManagement.al:
            if product.productName.lower() == product_name.lower():
                ProductManagement.print_product_details(product)
                Product.productName = input("New Product Name:")
                Product.productID = input("New Product ID:")
                Product.productPrice = input("New Product Price:")
                Product.productQuantity = input("New Product Quantity:")
                Product.productCategory = input("New Product Category:")
                print("Product Information Updated.")
                return
            print("Product Not Found.")

    @staticmethod
    def print_product_details(product):
        print("Product Name:" + product.productName)
        print("Product ID:" + product.productID)
        print("Product Price:" + product.productPrice)
        print("Product Quality:" + product.productQualtiy)
        print("Product Category :" + product.productCategory)

    @staticmethod
    def load_data_from_file():
        if os.path.exists(ProductManagement.file_path):
            with open(ProductManagement.file_path, "r") as file:
                for line in file:
                    p_data = line.strip().split(",")
                    if len(p_data) > 4:
                        product = Product(p_data[0], p_data[1], p_data[2], p_data[3], p_data[4])
                        ProductManagement.al.append(Product)

    @staticmethod
    def save_data_to_file():
        print("Saving Product data to file")
        with open(ProductManagement.file_path, "a") as file:
            for Product in ProductManagement.al:
                file.write(
                    f"{Product.productName},{Product.productID},{Product.price},{Product.quantity},{Product.categoary}\n")








