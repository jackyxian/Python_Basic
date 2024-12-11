file = open("./data.txt","r",encoding="utf-8")
content = file.read()
print(content)
file.close()

with open("./data.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)