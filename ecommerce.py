# Base class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Subclass PhysicalProduct
class PhysicalProduct(Product):
    def __init__(self, name, price, shipping_cost):
        super().__init__(name, price)
        self.shipping_cost = shipping_cost

    def get_total_cost(self):
        return self.price + self.shipping_cost


# Subclass DigitalProduct
class DigitalProduct(Product):
    def __init__(self, name, price, download_link):
        super().__init__(name, price)
        self.download_link = download_link

    def get_total_cost(self):
        return self.price


# Creating objects
laptop = PhysicalProduct("Laptop", 2500000, 50000)
ebook = DigitalProduct("Python E-Book", 50000, "www.download.com/python-ebook")

# Display details
print("Physical Product")
print("Name:", laptop.name)
print("Price: UGX", laptop.price)
print("Shipping Cost: UGX", laptop.shipping_cost)
print("Total Cost: UGX", laptop.get_total_cost())

print()

print("Digital Product")
print("Name:", ebook.name)
print("Price: UGX", ebook.price)
print("Download Link:", ebook.download_link)
print("Total Cost: UGX", ebook.get_total_cost())