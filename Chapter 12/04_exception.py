
try:
    a= int(input("Hey, Enter a number: "))
    print(a)
    
except ValueError as v:
    print("Hey")
    print(v)


except Exception as e:
    print(e)
