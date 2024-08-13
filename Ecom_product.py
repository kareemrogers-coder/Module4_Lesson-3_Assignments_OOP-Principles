# 2. E-commerce Product Catalog System


# Objective: The goal of this assignment is to demonstrate a deep understanding of inheritance and method overriding in Python. Students will apply these concepts to develop an E-commerce Product Catalog System that handles various types of products with both common and unique attributes.


# Problem Statement: An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. Each product type shares some common characteristics but also has unique features. The system should be able to display information about each product appropriately.


# Task 1: Create Base Product Class


# Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
# Expected Outcome: A Product class that can hold general information about a product and display it.
from helper import d

class Product():

    def __init__(self, product_id, item_name, price):
        self.product_id = product_id
        self.name = item_name
        self.price = price

## Testing the super class:
    # def product_info(self):
    #     print(f"Product info has the produc id: {self.product_id}, type of product: {self.item_name} and at {self.price}")

# book1 = Product("test85"," book", "$50.00")
    # print(book1) output the class
        # print(book1.product_id) output the product id of the product

# Task 2: Implement Subclasses for Specific Products

# (ONLY BOOK SUBCLASS REQUIRED)

# Create subclasses Book, Electronic, and Clothing that inherit from Product.
# Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).
# Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.


# Task 3: Override Display Method in Subclasses


# Override the method to display product information in each subclass to include specific attributes.
# For example, the Book class should display the author, Electronic should display specs, etc.
# Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.

## Creating a subclass for books
class Book(Product):
    
    def __init__(self, product_id, item_name, price, author, title):
        super().__init__(product_id, item_name, price)
        self.author = author
        self.title = title
        self.item_name = item_name
    
    def display_info(self):
        print(f" Welcome to Rogers Store: \n The product information is as follows: \n Type of product is a {self.item_name} with a Product id of {self.product_id}.\n The author for {self.title} is {self.author} with a price tag of {self.price}")

class Electronic(Product):

    def __init__(self, product_id, item_name, price, product, specs):
        super().__init__(product_id, item_name, price)
        self.product = product
        self.specs = specs
        self.item_name = item_name
    
    def display_info(self):
        print(f" Welcome to Rogers Store: \n The product information is as follows: \n Type of product is a {self.item_name} with a Product id of {self.product_id}.\n The electronic type falls under the {self.product} category, with an operations system of {self.specs}. The current price will be at {self.price}")


### Creating instances 

###testing
New_book = Product("sku87989", "Book", "$40.00")

# print(book3.price)
# print(book3.product_id)


# Task 4: Test Product Catalog Functionality


# Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
# Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method overriding.

d()

new_book = Book("sku87989", "book", "$40.00", "Simon Sinek", "Leaders Eat Last")

new_book.display_info()

d()

new_book2 = Book("sku87990", "book", "$29.99", "Noam Wasserman", "The Founder's Dilemmas")

new_book2.display_info()

d()

Electronic_1 = Electronic("sku87958", "Macbook", "$4000.00", "Macbook pro", "macos 14 Sonoma")

Electronic_1.display_info()


