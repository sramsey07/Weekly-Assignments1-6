fileOne = input("Enter the name of file 1: ")

fileTwo = input("Enter the name of file 2: ")

file1 = open(fileOne, "r")

file2 = open(fileTwo, "r")

text = file1.read()

text = file2.read()

file1.close()

file2.close()
