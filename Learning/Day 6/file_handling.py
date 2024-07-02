f=open("samole.txt","r")
print(f.read())
print(f.read(10)) # it read only 10 char
print(f.readline())
print(f.readlines())

f=open("samole.txt","w")
# f.write("lol")
f=open("samole.txt","a")
f.write("lol")
# print(f.read())

print(f.tell())  # it returns the current postion of the cursor
f.seek(10) #-> it moves the cursor to 10 postion of the char in the file