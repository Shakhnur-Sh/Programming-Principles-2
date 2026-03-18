import os
import shutil

# Create source and target directories
source_dir = "source_files"
target_dir = "target_files"

if os.path.exists(source_dir) == False:
    os.mkdir(source_dir)

if os.path.exists(target_dir) == False:
    os.mkdir(target_dir)

# Create sample files in source_files
file1 = os.path.join(source_dir, "notes.txt")
file2 = os.path.join(source_dir, "data.csv")

with open(file1, "w", encoding="utf-8") as f:
    f.write("This is a text file.\n")

with open(file2, "w", encoding="utf-8") as f:
    f.write("id,name\n1,Ali\n2,Aruzhan\n")

# Find files by extension
print("TXT files:")
for file in os.listdir(source_dir):
    if file.endswith(".txt"):
        print(file)

# Copy txt file
copy_path = os.path.join(target_dir, "notes.txt")
shutil.copy(file1, copy_path)
print("notes.txt copied to target_files")

# Move csv file
move_path = os.path.join(target_dir, "data.csv")
shutil.move(file2, move_path)
print("data.csv moved to target_files")