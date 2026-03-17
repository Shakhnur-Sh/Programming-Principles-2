import os
import shutil

source_file = os.path.join("file_handling", "sample.txt")
copy_file = os.path.join("file_handling", "sample_copy.txt")
backup_file = os.path.join("file_handling", "sample_backup.txt")

# Copy file
if os.path.exists(source_file):
    shutil.copy(source_file, copy_file)
    print(f"{source_file} copied to {copy_file}")

    shutil.copy(source_file, backup_file)
    print(f"{source_file} backed up as {backup_file}")
else:
    print(f"{source_file} does not exist")

# Delete copy safely
if os.path.exists(copy_file):
    os.remove(copy_file)
    print(f"{copy_file} deleted safely")
else:
    print(f"{copy_file} not found")