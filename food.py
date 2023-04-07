class burger:
    def __init__(self, calories,topping,price):
        self.calories = calories
        self.topping = topping
        self.price = price

    def __str__(self):
        return f'your burger is with {self.calories} calories, with {self.topping} on top, and the price is {self.price}'

burger1 = burger(459, 'mushrooms',55)
print(burger1)