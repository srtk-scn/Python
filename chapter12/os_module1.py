import os
#os.getcwd()--->>to know where we are woking
print(os.getcwd())
os.mkdir('movies')
print(os.path.exists('movies'))
if os.path.exists('movies'):
    print('already exists')
else:
    os.mkdir('movies')
open("moves.txt","a").close()
os.mkdir(r"D:\New folder\movies")
os.chdir(r"D:\New folder")
os.mkdir(r"D:\New folder\movies")
os.chdir(r"F:\new python course\chapter12")
print(os.listdir())
print(os.listdir(r"D:\New folder"))#print the list of file anf folder in the directory
# for item in os.listdir():        #for printing the paths
#     print(r"F:\new python course\chapter12"+"\\"+item)
# for item in os.listdir():
#     print(os.path.join(os.getcwd(),item))

# for item in os.listdir(r"D:\New folder"):
#     print(os.path.join(r"D:\New folder",item))