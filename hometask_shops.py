class Shops:

    sell_number = 0

    def __init__(self, title, number):
        self.title = title
        self.number = number

    def sell(self, increase):
        self.increase = increase

        Shops.sell_number += self.number + self.increase
        return Shops.sell_number

shop1 = Shops("Bingo", 300)
shop2 = Shops("Dingo", 200)
shop1.sell(150)
shop2.sell(300)

print("Total sales: ", Shops.sell_number)