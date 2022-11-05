class Dictionary():

#Constructor
    def __init__(self):
        self.tuple = []
#adding key(string) and value(int) to tuple
    def set(self, key, value):
        self.key = key
        self.value = value
        
        self.tuple.append((key,value))

#checking if the given key is in tuple
    def get(self, key):
        for n in self.tuple:
            if n[0] == key:
                return n[1]
        raise KeyNotFoundError(f'Key not found: {key}')
#turning tuple into a string type
    def __str__(self):
        return str(self.tuple)

#Custom exception
class KeyNotFoundError(Exception):
    pass

#adding values to tuple
products = Dictionary() 
products.set('RTX3060', 329.99) 
products.set('RTX3070', 499.99) 
products.set('RTX3080', 1499.99) 
products.set('RTX3090', 1999.99) 

#printing
print(f'products = {products}') 
print(f'RTX3090 = {products.get("RTX3090")}')
products.get('RTX3050')