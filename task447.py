lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line.upper())

for item in lines:
    print(item)