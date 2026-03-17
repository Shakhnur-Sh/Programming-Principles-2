import os

print("Current working directory:")
print(os.getcwd())

# Create one directory
if os.path.exists("test_folder")==False:
    os.mkdir("test_folder")
    print("test_folder created")

# Create nested directories
nested_path = os.path.join("test_folder", "subfolder1", "subfolder2")
if os.path.exists(nested_path)==False:
    os.makedirs(nested_path)
    print("Nested directories created")

# List files and folders in current directory
print("Contents of current directory:")
print(os.listdir())

# Change directory
os.chdir("test_folder")
print("Changed directory to:")
print(os.getcwd())

# Go back to parent directory
os.chdir("..") # or os.chdir("../..") to go back two levels
print("Returned to:")
print(os.getcwd())

# Remove empty directory
empty_dir = "empty_folder"
if os.path.exists(empty_dir)==False:
    os.mkdir(empty_dir)
    print("empty_folder created")

os.rmdir(empty_dir)
print("empty_folder removed")



#os.getcwd() => get current working directory
#os.mkdir() => create a single directory (одна папка)
#os.makedirs() => create nested directories (вложенные папки сразу)
#os.listdir() => list files and folders in a directory
#os.chdir() => change current working directory
#os.rmdir() => remove an empty directory