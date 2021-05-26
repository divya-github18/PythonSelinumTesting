f = open("demoFile2.txt", "w")
f.write("Welcome")
f.close()
f = open("demoFile2.txt", "r")
print(f.read())
print("---------------------------------------------")
with open("demoFile.txt", "r") as file:
    content = file.read()
    print(content)
    reversed_text = reversed(content)
print("---------------------------------------------")
with open("demoFile.txt", "w") as file1:
    for line in reversed_text:
        file1.write(line)
with open("demoFile.txt", "r") as file1:
    print(file1.read())