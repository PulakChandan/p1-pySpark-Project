#PF-Assgn-39
#This verification is based on string match.     
#Global variables
from collections import Counter 
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]
'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''

def place_order(*item_tuple):
    #Remove pass and write your logic here
   
    for i in range(0,len(item_tuple),2):
        ind=menu.index(item_tuple[i])
        if quantity_available[ind]<item_tuple[i+1]:
            return False
    for i in range(0,len(item_tuple),2):
        ind=menu.index(item_tuple[i])
        quantity_available[ind]-=item_tuple[i+1]
    return True

        
    
print(place_order('Noodles',150,'Veg Roll',2))
print(quantity_available)
    



