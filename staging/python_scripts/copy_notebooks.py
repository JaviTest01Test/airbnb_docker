import os
import shutil
import argparse

def copy_files(source_dir, target_dir):
    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Copy files from source to target directory if not exists
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)
        
        # Check if the item already exists in the target directory
        if not os.path.exists(target_item):
            # Copy file or directory recursively
            if os.path.isdir(source_item):
                shutil.copytree(source_item, target_item)
            else:
                shutil.copy2(source_item, target_item)

    # Set appropriate permissions
    for root, dirs, files in os.walk(target_dir):
        for dir in dirs:
            os.chmod(os.path.join(root, dir), 0o777)
        for file in files:
            os.chmod(os.path.join(root, file), 0o777)

    # Confirm completion
    print(f"Files copied from {source_dir} to {target_dir} successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy notebooks from source to target directory.")
    parser.add_argument("source_dir", type=str, help="Source directory path")
    parser.add_argument("target_dir", type=str, help="Target directory path")
    args = parser.parse_args()

    copy_files(args.source_dir, args.target_dir)
