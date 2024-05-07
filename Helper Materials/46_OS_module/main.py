import os , rena

# os.chdir("46_OS_module") #--> To change the directory

if(not os.path.exists("data")):
    os.mkdir("data") #--> To create a new directory/file

for i in range(10):#--> It will show an error that fie already exist so we can use path.exist function see how:
    os.mkdir(f'data/fill{i}')

folders = os.listdir("data") #--> To make a list of all folders of a directory
b = len(folders)
# To rename a file see rename program
# rena.rename('data' , b )

folders = os.listdir("data") 
# os.chdir("data")
# for folder in folders:
#     os.chdir(f"{folder}")                         #--> Not working as we can't move one folder back
#     os.mkdir(f"try {folder}")
#     path = os.path.abspath(os.path.join(os.getcwd() , os.pardir()))
#     os.chdir(path)
    # print(os.getcwd())
    

# folders = os.listdir("data") #--> To make a list of all folders of a directory
# # print(folders)
for folder in folders:
    print(folder)

# os.rmdir() #--> Removes an empty directory
os.remove('data')


