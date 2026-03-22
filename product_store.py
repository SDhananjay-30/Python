class Product():

    count =0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total number of product are :{Product.count}")
    
    @staticmethod
    def discount(price,discount):
        final_price = price - (discount*price/100)
        print(f"discount Price:{final_price}")


produ = Product("Laptop",10_000)
p2 = Product("Phone",5000)
p3 = Product("Pen",10)

Product.get_count()

produ.get_info()

produ.discount(produ.price,12)