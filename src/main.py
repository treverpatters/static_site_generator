from textnode import *
from tools import *
from copy_static import *
from generate_page import *
import sys

def main():
    
    copy_static()
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    template_path = "template.html"
    content_dir = "content"
    docs_dir = "docs"
    generate_pages_recursive(content_dir, template_path, docs_dir, basepath)

if __name__ == "__main__":
    main()