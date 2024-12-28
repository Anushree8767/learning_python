f = open("D:\Python\demo.txt ","r")

data = f.read()
print(data)

f = f.close()



# try:
#     with open("demo.txt", "rt") as f:
#         data = f.read()
#         print("File content:")
#         print(data)
# except FileNotFoundError:
#     print("The file was not found.")
# except IOError:
#     print("Error reading the file.")
