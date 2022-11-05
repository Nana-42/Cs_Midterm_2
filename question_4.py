import re
def recognize_price(name):

    name_fsa = re.compile("\$\d{1,5}(\.\d{2})?") #custom regex
    word_fsa = name_fsa.search(name) #searching
    
    if word_fsa:
        return word_fsa.group()
    else:
        return None

#printing
print(recognize_price('I paid two hundred dollars for this product...')) # None 
print(recognize_price('$200')) # '$200' 
print(recognize_price('I paid $200 for this product...')) # '$200' 
print(recognize_price('I paid $200.0 for this product...')) # '$200' 
print(recognize_price('I paid $200.00 for this product...')) # '$200.00' 
print(recognize_price('I paid $2000.00 for this product...')) # '$2000.00' 
print(recognize_price('I paid $20000.00 for this product...')) # '$20000.00' 