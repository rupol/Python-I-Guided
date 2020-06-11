class Product:
    def __init__(self, name, price, discount = 0):
        self.name = name
        self.price = price
        self.discount = discount

    def __str__(self):
        return f'{self.name}: ${self.price}'

# Sneaker is a Product
class Sneaker(Product):
    def __init__(self, name, price, shoe_size, brand):
        # super function returns us the parent class instance
        # we can set a default discount for all sneakers here...
        super().__init__(name, price, 10)
        self.shoe_size = shoe_size
        self.brand = brand

class SoccerBall(Product):
    def __init__(self, name, price, material):
        # if we don't want to do anything with discount, we don't have to change this class at all
        super().__init__(name, price)
        self.material = material

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} WILSOOONNNNNNN'
        
    def kick(self):
        print("The ball flew away")

generic_product = Product("Widget", "99.99")
nike_free = Sneaker("Nike Free", "100", "10", "Nike")
soccer_ball = SoccerBall("Wilson", "20", "Rubber")

print(nike_free.name)
print(soccer_ball.price)
print(soccer_ball.discount)
print(nike_free.discount)
print(generic_product)
print(nike_free)
print(soccer_ball)
soccer_ball.kick()