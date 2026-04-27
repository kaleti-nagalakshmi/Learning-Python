# set :  in python is a collection of unique elements. It is unordered and unindexed. 
# Sets are mutable, which means that you can add or remove elements from a set after 
# it has been created. However, the elements themselves must be immutable 
# (e.g., strings, numbers, tuples).

essential_spices = {"ginger","cardamom","pepper"}
optional_spices = {"cinnamon","garlic","pepper"}

union_set = essential_spices  | optional_spices 
print(union_set)

intersection_set = essential_spices & optional_spices
print(intersection_set)

difference_set = essential_spices - optional_spices
print(difference_set)

difference_set2 = optional_spices - essential_spices    
print(difference_set2)

# membership :  check if a specific element exists within a set.
print("ginger" in essential_spices)
print("cinnamon" in essential_spices)


 



