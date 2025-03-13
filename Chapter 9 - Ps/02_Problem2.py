import random

def game():
    print("You are playing a game...")
    score = random.randint(1,62)
    #Fetch the Hiscore 
    with open("02_hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
        #write this Hiscore to the file
        with open("02_hiscore.txt","w") as f:
            f.write(str(score))

    return score

game()