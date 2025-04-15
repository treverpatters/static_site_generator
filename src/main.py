import os
import sys
import shutil
from generate_page import generate_pages_recursive
import copy_static

def main():
    # Get basepath from command line args
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"Building site with basepath: {basepath}")
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.makedirs("docs")

    template_path = "template.html"
    content_dir = "content"
    docs_dir = "docs"
    generate_pages_recursive(content_dir, template_path, docs_dir, basepath)

    os.makedirs(os.path.join(docs_dir, "images"), exist_ok=True)
    copy_static(docs_dir)


def copy_recursive(src, dst):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    # List all items in source directory