import os
import shutil

# Define source and target directories
SOURCE_DIR = "/airbnb_project/notebooks"
TARGET_DIR = "/airbnb_project/notebooks_local"

# Ensure the target directory exists
os.makedirs(TARGET_DIR, exist_ok=True)

# Copy files from source to target directory if not exists
for item in os.listdir(SOURCE_DIR):
    source_item = os.path.join(SOURCE_DIR, item)
    target_item = os.path.join(TARGET_DIR, item)
    
    # Check if the item already exists in the target directory
    if not os.path.exists(target_item):
        # Copy file or directory recursively
        if os.path.isdir(source_item):
            shutil.copytree(source_item, target_item)
        else:
            shutil.copy2(source_item, target_item)

# Set appropriate permissions
for root, dirs, files in os.walk(TARGET_DIR):
    for dir in dirs:
        os.chmod(os.path.join(root, dir), 0o777)
    for file in files:
        os.chmod(os.path.join(root, file), 0o777)

# Confirm completion
print(f"Files copied from {SOURCE_DIR} to {TARGET_DIR} successfully.")
