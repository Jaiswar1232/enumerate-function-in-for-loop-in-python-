list_1 = ["apple", "banana", "orange", "mango"]
 
for index, element in enumerate(list_1):
   print(index, element)
   
 #Please note that, using range() function, to get index and accessing element using index, is not in the spirit of python. enumerate() is relatively recommended if you would like to access index in the for loop.  
#enumerate() function keeps track of the count of elements we are iterating in the loop.
