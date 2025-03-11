marks = {
    "Raj": 90,
    "Kaushik": 80,
    "Akilan": 99,
    "list":[1,2,9],
    0:"Mohan"
}

d ={} #this is a empty Dictionary

# print(marks.items())          #Returns a view object of key-value pairs.
# print(marks.keys())           #Returns a view object of all keys.
# print(marks.values())         #Returns a view object of all values.

# marks.update({"Raj":95, "Mani":50})   #To Updates the dictionary with another dictionary’s key-value pairs.
# print(marks)



# print(marks.get("Raju"))    #Return None
# print(marks["Raju"])        #Return error

marks["Raju"] = 45 #to add 

# a=marks.pop("list")       #remove the items
# print(a)
# print(marks)

# b= marks.popitem()      #remove the last item
# print(b)

del marks[0]                #delete the Key
del marks["list"]



# marks.clear()
print(len(marks))