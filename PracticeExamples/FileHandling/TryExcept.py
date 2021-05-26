# The try block will raise an error when trying to write to a read-only file:
try:
    f = open("demoFile.txt")
    f.write("Welcome")
except Exception as e:
    print(e)
    print("Something went wrong when writing to the file")
finally:
    f.close()
# The program can continue, without leaving the file object open
print('------------------------------------')
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")