class Product():
#Constructor/__init__ Fucntion
    def __init__(self, name, price, weight ):
        self.name = name
        self.price = price
        self.weight = weight

#Shipping cost Fucntion
    def get_shipping_cost(self):
        self.shipping_cost = self.weight * 10
        return self.shipping_cost
#Tax Function
    def get_tax(self):
        self.tax = self.price * 0.13
        return self.tax
#Total_cost Fucntion
    def get_total_cost(self):
        self.toal_cost = self.price + self.get_tax() + self.get_shipping_cost()
        return self.toal_cost

razor = Product("Electric Razor", 49.99, 0.25)
home_gym = Product("Home Gym", 879.99, 115.0)

print(f'Total cost of {razor.name}: {razor.get_total_cost():0.2f}')
print(f'Total cost of {home_gym.name}: {home_gym.get_total_cost():0.2f}')


