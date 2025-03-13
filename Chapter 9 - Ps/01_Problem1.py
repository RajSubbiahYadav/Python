with open("01_poem.txt") as f:
    content = f.read()
    if ("fall" in content):
        print("The word Fall is present in the content")
    else:
        print("The word Fall is not present in the content")