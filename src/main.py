from textnode import *
from tools import *
from copy_static import *
from generate_page import *

def main():
    
    copy_static()

    template_path = "template.html"
    content_dir = "content"
    public_dir = "public"
    generate_pages_recursive(content_dir, template_path, public_dir)

if __name__ == "__main__":
    main()