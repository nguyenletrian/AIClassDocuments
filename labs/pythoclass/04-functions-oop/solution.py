"""12 products: functions, inheritance and abstract method."""
from abc import ABC,abstractmethod
def discount(price, rate=0.1):
    if price<0 or not 0<=rate<=1: raise ValueError("Invalid price/rate")
    return price*(1-rate)
class Product(ABC):
    def __init__(self,product_id,name,price):
        self.id,self.name,self.price=product_id,name,price
    @abstractmethod
    def describe(self): pass
class Electronic(Product):
    def describe(self): return f"Electronic {self.id}: {self.name}"
class Household(Product):
    def describe(self): return f"Household {self.id}: {self.name}"
def main():
    products=[Electronic(f"E{i:03}",f"Device {i}",100+i*20) for i in range(1,7)]
    products += [Household(f"H{i:03}",f"Item {i}",60+i*10) for i in range(1,7)]
    assert len(products)==12
    for item in products: print(item.describe(),"Discounted:",discount(item.price))
    print("Total list price:",sum(x.price for x in products))
if __name__ == "__main__":
    main()
