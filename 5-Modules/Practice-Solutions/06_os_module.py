import os

os.mkdir("new_directory")
print(os.listdir("."))

os.rmdir("new_directory")
print(os.listdir("."))
