# c/5 = (f-32)/9   formula
# c = 5*(f-32)/9

def f_to_c():
    f = int(input("Enter temperature in F : "))
    a = 5*(f-32)/9
    return a

c = f_to_c()
print(f"{round(c,2)}°C")