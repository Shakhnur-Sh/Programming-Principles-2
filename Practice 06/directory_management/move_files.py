import os
import shutil
from pathlib import Path

source_dir = Path("source_files")
target_dir = Path("target_files")

if os.path.exists("source_files") == False:
    os.mkdir("source_files")

if os.path.exists("target_files") == False:
    os.mkdir("target_files")

# Create sample files
file1 = source_dir / "notes.txt"
file2 = source_dir / "data.csv"

with open(file1, "w", encoding="utf-8") as f:
    f.write("This is a text file.\n")

with open(file2, "w", encoding="utf-8") as f:
    f.write("id,name\n1,Ali\n2,Aruzhan\n")

# Find files by extension
print("TXT files:")
for file in source_dir.iterdir():
    if file.suffix == ".txt":
        print(file.name)

# Copy txt file
shutil.copy(file1, target_dir / file1.name)
print(f"{file1.name} copied to {target_dir}")

# Move csv file
shutil.move(str(file2), str(target_dir / file2.name))
print(f"{file2.name} moved to {target_dir}")# directory_management/move_files.py

import os
import shutil
from pathlib import Path

source_dir = Path("source_files")
target_dir = Path("target_files")

source_dir.mkdir(exist_ok=True)
target_dir.mkdir(exist_ok=True)

# Create sample files
file1 = source_dir / "notes.txt"
file2 = source_dir / "data.csv"

with open(file1, "w", encoding="utf-8") as f:
    f.write("This is a text file.\n")

with open(file2, "w", encoding="utf-8") as f:
    f.write("id,name\n1,Ali\n2,Aruzhan\n")

# Find files by extension
print("TXT files:")
for file in source_dir.iterdir():
    if file.suffix == ".txt":
        print(file.name)

# Copy txt file
shutil.copy(file1, target_dir / file1.name)
print(f"{file1.name} copied to {target_dir}")

# Move csv file
shutil.move(str(file2), str(target_dir / file2.name))
print(f"{file2.name} moved to {target_dir}")