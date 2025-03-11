a = int(input("Enter Your age: "))

#       If statement no :1

if(a%2 == 0):
    print("age is Even")

#       If statement no :2

if(a>=18):
    print("You are an adult")
    print("Good")

elif(a<0):
    print("age Cannot be Negative")

elif(a==0):
    print("age Cannot be Zero")
    
else:
    print("You are not an adult")


print("End of program")