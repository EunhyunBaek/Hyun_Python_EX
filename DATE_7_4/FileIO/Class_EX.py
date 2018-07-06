"""

class CVS:
    def __init__(self,name):
        self.name=name
    def Name(self):
        print("안녕하세요 SevenStore " + self.name, "지점 입니다.")
    def Buy(self):
       pass

class SevenStore(CVS):
    pass
class MiniShop(CVS):
    pass
class CvsyoU(CVS):
    pass
class GS25(CVS):
    pass

Store=SevenStore("광명")
Store.Name()
"""

class Product:
    code=str()
    name=str()
    price=int()
    maker=str()
    def sell(self):
        pass

    def unknown(self):
        pass
class Person:
    name = str()
    age= str()
    money=int()

    def buy(self):
        pass
    def view(self):
        pass

class Beverage(Product):
    유통기한 = str()
class ColdBeverage(Beverage):
    pass
class HotBeverage(Beverage):
    pass
class Snack(Product):
    pass

class Liquor(product):
    pass

class Customer:
    customerid=str()
    degree = int()
    mileage = int()

class Manger(Person):
    shopid= int()
    shopname=str()

    def sell(self):
        pass
    def 일매출통계(self):
        pass
class CVS:
    def 입고(self):
        cb=ColdBeverage()

class product:
    pass