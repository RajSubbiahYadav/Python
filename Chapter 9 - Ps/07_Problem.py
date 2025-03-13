

with open("06_log.txt") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present, line no: {lineNo}")
        break
    lineNo += 1

else:
    print("No python is not present")
