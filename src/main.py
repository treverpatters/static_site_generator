import os
import sys
import shutil
from generate_page import generate_pages_recursive

def main():
    # Get basepath from command line args
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"Building site with basepath: {basepath}")
    
    # Set output directory to 'docs' (not 'public')
    output_dir = "docs"
    
    # Clear output directory if it exists
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    # Find the template path (update this path based on your structure)
    template_path = "./template.html"  # Adjust this path!
    
    # Generate pages
    generate_pages_recursive("content", template_path, output_dir, basepath)
    
    # Copy static files
    if os.path.exists("static"):
        copy_recursive("static", os.path.join(output_dir, "static"))
    
    if os.path.exists("images"):
        copy_recursive("images", os.path.join(output_dir, "images"))
    
    print(f"Site built successfully in {output_dir}/")

def copy_recursive(src, dst):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    # List all items in source directory