

class Menu:
    """fill in class definition here"""
    def add(self,food,price):
        self.food = food
        self.price = price
    def show(self):
        print(self.food,self.price)

m = Menu()  # Menu is a class
m.add("idly", 10)
m.show()

m.add("vada", 20)
m.show()
