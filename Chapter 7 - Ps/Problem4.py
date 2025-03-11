n = int(input("Enter a number: "))

for i in range(2,n):
    if(n%i)== 0 :
        print(f"Number is Not prime Number")
        break
else:
    print("Number is Prime")