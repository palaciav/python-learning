file = open("..\\files\\fruits.txt",'r')
content = file.readlines()
content = [i.rstrip("\n") for i in content]
for fruit in content:
    print(len(fruit))
file.close()
