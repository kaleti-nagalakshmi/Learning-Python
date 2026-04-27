chai_order = {"size":"medium","type":"ginger","sugar":2}
print(chai_order)
print(type(chai_order))

chai_recipe={}
chai_recipe["water"]=50
chai_recipe["ginger"]=10
chai_recipe["milk"]=100
print(chai_recipe)


# index
print(chai_recipe["ginger"])
print(chai_order["size"])
print(chai_recipe["milk"])

# get() method is used to get the value of the specified key. 
# If the key is not found, it returns None 

print(chai_recipe.get("ginger"))
print(chai_order.get("type"))

# keys() method is used to get a list of all the keys in the 
# dictionary.
print(chai_recipe.keys())
print(chai_order.keys())

# values() method is used to get a list of all the values in the dictionary.
print(chai_recipe.values())
print(chai_order.values())

# items() method is used to get a list of all the key-value pairs
#  in the dictionary.
print(chai_recipe.items())
print(chai_order.items())

# update() method is used to update the value of a key in the 
# dictionary.
chai_recipe.update({"water": 60})
print(chai_recipe)

# del keyword is used to delete a key-value pair from the dictionary.
del chai_recipe["ginger"]

# clear() method is used to remove all the key-value pairs from the dictionary.
chai_recipe.clear()

# copy() method is used to create a copy of the dictionary.
chai_recipe_copy = chai_recipe.copy()


