# Python provides several ways to manipulate files.
# Python provides the open() function to open a file. It takes two argumnets: the name of file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing or 'a' for appending.
# Modes in file:
# 1. read(r) : This mode opens file for reading only and gives error if file doesn't exist
# 2. write(w) : This mode opens file for writing only and creates a new file if file doesn't exist
# 3. apend(a) : This mode opens file for appending only and creates a new if file doesn't exist
# 4. create(x) : This mode creates a file and gives error if file already exist
# 5. text(t) : t mode refers to the handling of text mode, therefore, it is used to handle text files. The default mode is 'r'(open for reading text, synonym of 'rt')
# 6. binary(b) : This mode refers to the handling of binary files such as images, pdfs, etc

# READING A FILE :
# f = open('test file.txt' , 'r')
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE :
# writing to a file will overwrite its content
# f = open('test file.txt' , 'w')
# f.write('New content is here')
# f.close()

# APPENDIG IN A FILE :
# Appending will not over-write its content and will add new content to the end of file
# f = open('test file.txt' , 'a')
# f.write('\nNew content is here')
# f.close()

# If we don't want to make opening-closing pairs all time or if we don't want to close a file on our own than we can simply use 'with' statement

# with open('test file.txt' , 'a') as f:
#     f.write('\nNew content is added')



# METHODS of FILE I/O:

# f = open("test file.txt" , 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline() # It is used to read a file line by line. It returns a string output
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of student in {i} in Maths is : {m1}")
#     print(f"Marks of student in {i} in English is : {m2}")
#     print(f"Marks of student in {i} in SST is : {m3}")
# f.close()

# f = open("test file.txt" , 'w')
# lines = ['line 1\n' , 'line 2\n' , 'line 3\n']
# f.writelines(lines) # It writes a sequence of strings to a file. The sequence can be any iterable obect such as list or tuple
# f.close()

# In python seek and tell functions are used to work with file objects and their positions within a file. These functions are part of builtin module
# seek() - Used to place cursor at a specified positoin
# tell() - This function return the current positon within the file in bytes. It helps to locate the position of our cursor

with open('test file.txt' , 'r') as f:
    print(f.seek(10))
    f.tell()
    data = f.read(4) # Used to read n characters, here n is 5
print(data)

with open('test file.txt' , 'w') as f:
    f.write('12345789_test')
    f.truncate(5) # use to change your file size to specific characters
with open('test file.txt' , 'r') as f:
    print(f.read())
