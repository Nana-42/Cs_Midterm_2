import re
def recognize_name(name):

    search_fsa = re.compile('[A-Z][a-z]+\s[A-Z][a-z]+(\sJr)?') #custom regex
    name_search = re.search(search_fsa, name) #searching

    if name_search:
        return name_search.group()
    else:
        return None

#printing
print(recognize_name('no score in the game so far')) # None 
print(recognize_name ('Bo Bichette')) # 'Bo Bichette' 
print(recognize_name('Vladimir Guerrero Jr hit a fly ball...')) # 'Vladimir Guerrero Jr' 
print(recognize_name ('and a base hit by Matt Chapman')) # ' Matt Chapman' 
print(recognize_name ('caught by Jackie Bradley Jr for the third out')) # 'Jackie Bradley Jr' 
 
