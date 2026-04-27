# list
    # Lists are mutable sequences, used to store collections of homogeneous or heterogeneous
    #  data. 
    # They are defined by enclosing the elements in square brackets [] and 
    # separated by commas.

list_1=[1,"tea",3.14,True]
print(list_1)
print(type(list_1))


ingredients=["water","fruits","milk","sugar"]

# list functions
#  1. len() function is used to get the number of elements in the list.
#  2. count() function is used to count the number of specific element in the list.
#  3. index() function is used to get the index of the specific element in the list.
#  4. reverse() function is used to reverse the order of the elements in the list.
#  5. sort() function is used to sort the elements in the list in ascending order.
#  6. append() method is used to add an element to the end of the list.
#  7. remove() method is used to remove the specified element from the list.
#  8. clear() method is used to remove all the elements from the list.
#  9. pop() method is used to remove the last element from the list and return it.
# 10. insert() method is used to add an element at the specified index in the list.
# 11. extend() method is used to add all the elements of a list to another list.





#   append() method is used to add an element to the end of the list.
ingredients.append("ice cubes")
ingredients.append("boost powder")
ingredients.append("dry fruits")
print(ingredients)

# remove() method is used to remove  a 
# specified element from the list.

ingredients.remove("fruits")
print(ingredients)
ingredients.remove("sugar")
print(ingredients)

# clear() method is used to remove all the elements from the list.
# ingredients.clear()

# pop() method is used to remove the last element from the list and return iti
ingredients.pop()
print(ingredients)

# insert() method is used to add an element at the specified index in the list.
ingredients.insert(2,"honey")
print(ingredients)

# extend() method is used to add all the elements of a list to another list.
new_ingredients=["lemon","ginger"]
ingredients.extend(new_ingredients)
print(ingredients)

# sort() function is used to sort the elements in the list in ascending order.
ingredients.sort()
print(ingredients)

# reverse() function is used to reverse the order of the elements in the list.
ingredients.reverse()
print(ingredients)







