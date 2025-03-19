try:
    a= int(input("Hey, Enter a number: "))
    print(a)


except Exception as e:
    print(e)

else:
    print("i am inside else")  #if try is successful then else will run
    