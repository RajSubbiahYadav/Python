a= (1, 45.5,"Raj","Kriti",
    False,1,2,1)

print(a.count(1))  #3       #Returns the number of times x appears in the tuple.


print(a.index(1,1,6)) #5        #Returns the index of the first occurrence of x (optional: search within start to end).

"""
tup = (1, 2, 3)
lst = list(tup)  # Convert to list
lst.append(4)  # Modify the list
tup = tuple(lst)  # Convert back to tuple
print(tup)  # Output: (1, 2, 3, 4)
"""