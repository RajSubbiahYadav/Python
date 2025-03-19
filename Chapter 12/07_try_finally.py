try:
    a= int(input("Hey, Enter a number: "))
    print(a)


except Exception as e:
    print(e)

finally:
    print("i am inside finally")  #if try is successful then else will run
    