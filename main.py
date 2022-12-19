# import OS module
import os

# Get the list of all files and directories
path = "C://Users//subhash.reddy//OneDrive - Veoneer//Desktop//subhash"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)
for i in dir_list:
    if i=="practice.txt":
        path=path+"//"+i
        f = open(path, "r")
        print(f.read(5))
        f.close()
    else:
        print("No such file exists please check again")
f=open(path, "a")
f.write("the file is extended")
f.close()
