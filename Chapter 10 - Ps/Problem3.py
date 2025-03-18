class Demo:
    a = 4

o = Demo()
print(o.a) #print the class attribute because instance attribute is not present
o.a = 1 # Instance attribute is set
print(o.a) #print the Instance  attribute because instance attribute is present
print(Demo.a) #class attribute is not changed