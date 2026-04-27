
# Tuples are immutable sequences,  used to store collections of heterogeneous data. 
# They are defined by enclosing the elements in parentheses ().and separated by commas.


masala_spices = ("ginger", "cardamom", "cinnamon")

(spice1, spice2, spice3) = masala_spices
print(spice1,spice2,spice3)

# masala_spice=append(masala_spices, "pepper")

# print(type(masala_spices))
# print(masala_spice)

ginger_ratio, cardamom_ratio = 1,3
print(f"ratio is ginger:{ginger_ratio} and cardamom:{cardamom_ratio}")

# membership 
#    The in operator is used to check if a specific element exists within a tuple. 
# It returns True if the element is found and False otherwise.

print("ginger" in masala_spices)
print("pepper" in masala_spices )

ind=masala_spices.index("ginger")
print(ind)
index = masala_spices[0]
print(index)

if 20>10 :
    print("20 is greater than 10")