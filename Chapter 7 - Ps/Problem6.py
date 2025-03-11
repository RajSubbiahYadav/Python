# 5! = 1 X 2 X 3 X 4 X 5 = 120

n = int(input("Enter a number: "))

p = 1

for i in range(1, n+1):
    p = p * i
    i += 1

print(f"The factorial of {n} is {p}")
