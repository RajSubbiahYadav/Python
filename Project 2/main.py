from random import randint

n = randint(1,100)

a = -1
guesses = 0
while(a!= n):
    guesses += 1
    a = int(input("Guess a Number:"))
    if( a == n):
        print(f"Hey you made the correct guess {n} in {guesses}attempts")
        break
    elif(a>n):
        print("Lower Number Plz")
    elif(a<n):
        print("Higher Number Plz")