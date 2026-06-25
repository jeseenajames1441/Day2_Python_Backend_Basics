file = open("demo.txt", "w")
file.write("Hello Python File Handling")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()