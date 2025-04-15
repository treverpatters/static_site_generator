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
    print("Created docs directory")

    template_path = "template.html"
    content_dir = "content"
    docs_dir = "docs"
    print("Starting to generate HTML files...")
    generate_pages_recursive(content_dir, template_path, docs_dir, basepath)
    print("Finished generating HTML files")
    html_files = [f for f in os.listdir(docs_dir) if f.endswith('.html')]
    print(f"HTML files in docs directory: {html_files}")


    os.makedirs(os.path.join(docs_dir, "images"), exist_ok=True)
    copy_static.copy_static(docs_dir)



def copy_recursive(src, dst):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    # List all items in source directory

if __name__ == "__main__":
    print("Calling main function")
    main()
    print("Script completed")