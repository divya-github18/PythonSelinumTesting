import os
#os.remove("demoFile2.txt")
print("------------------------------")
if os.path.exists("demoFile2.txt"):
    os.remove("demoFile2.txt")
else:
    print("The file does not exist")
print("------------------------------")