# list
    # Lists are mutable sequences, used to store collections of homogeneous or heterogeneous
    #  data. 
    # They are defined by enclosing the elements in square brackets [] and 
    # separated by commas.

list_1=[1,"tea",3.14,True]
print(list_1)
print(type(list_1))


ingredients=["water","fruits","milk","sugar"]


ingredients.append("ice cubes")
ingredients.append("boost powder")
ingredients.append("dry fruits")
print(ingredients)



ingredients.remove("fruits")
print(ingredients)
ingredients.remove("sugar")
print(ingredients)


ingredients.pop()
print(ingredients)


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







