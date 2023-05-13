import os

root_dir = input("Enter root directory name: ")
os.mkdir(root_dir)

num_subdirs = int(input("Enter the number of subdirectories: "))
subdirs = []
for i in range(num_subdirs):
    subdir_name = input("Enter name of subdirectory {}: ".format(i+1))
    os.mkdir(os.path.join(root_dir, subdir_name))
    subdirs.append(subdir_name)

num_files = int(input("Enter the number of files: "))
for i in range(num_files):
    file_name = input("Enter name of file {}: ".format(i+1))
    subdir_name = input("Enter name of subdirectory to store the file in: ")
    if subdir_name not in subdirs:
        print("Error: {} is not a valid subdirectory.".format(subdir_name))
    else:
        file_path = os.path.join(root_dir, subdir_name, file_name)
        with open(file_path, "w") as f:
            f.write("This is a sample file.")

print("Root directory contents:")
print(os.listdir(root_dir))

for subdir in subdirs:
    subdir_path = os.path.join(root_dir, subdir)
    print("Contents of subdirectory {}: ".format(subdir))
    print(os.listdir(subdir_path))
