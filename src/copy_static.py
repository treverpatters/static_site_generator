import os
import shutil

def copy_static():
    print(f"Current working directory: {os.getcwd()}")
    # check if public exists and delete it if it does
    if os.path.exists("public"):
        shutil.rmtree("public")
    # create a fresh public directory
    print("Creating fresh public directory")
    os.mkdir("public")
    # Now start copying...
    copy_recursive("static", "public")

# Should take a source path and destination path
def copy_recursive(src, dst):
    # List all items in the source path
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        # debugging print
        print(f"Copying {src_path} to {dst_path}")
        # For each item:
        # If it's a file, copy it to the destination
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        # If it's a directory, create that directory in the destination and recursively call the function on that subdirectory
        else:
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
            copy_recursive(src_path, dst_path)