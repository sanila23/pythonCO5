# Program to read a file line by line and store it into a list
open_file = open('data.txt','r')
File_lines = open_file.readlines()

# Without using strip
print("\n File Content with newline characters:")
print(File_lines)

# By using strip
print("\n File content after removing newline characters:")
File_lines = [x.strip() for x in File_lines]
print([x.strip() for x in File_lines])
open_file.close()gitgitgithub