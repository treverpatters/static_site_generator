from markdown_to_html import markdown_to_html_node
import htmlnode
import os

def extract_title(markdown):
    # pull the h1 header from the markdown file (the line the starts with a single #) and return it
    lines = markdown.splitlines()
    h1 = ""
    for line in lines:
        #
        if len(line.strip()) != 0 and line[0] == "#" and line[1] != "#":
            h1 = line.lstrip("#").strip()
            break
    # if there is no h1 header, raise an exception.
    if h1:
        return h1
    else:
        raise Exception("no h1 header")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        page = file.read()
    with open(template_path, "r") as file:
        template = file.read()

    page_html = markdown_to_html_node(page) 
    page_html_string = page_html.to_html()
    page_title = extract_title(page)

    # Replace {{ Title }} and {{ Content }} placeholders in template with HTML and title
    added_title = template.replace("{{ Title }}", page_title)
    added_content = added_title.replace("{{ Content }}", page_html_string)
    content = added_content.replace('href="/', f'href={basepath}')
    content = content.replace('src="/', f'src="{basepath}')
    # Now write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # initiate variables
    for subdir, dirs, files in os.walk(dir_path_content):
        for file in files:
            source_file_path = os.path.join(subdir, file)
            
            rel_path = os.path.relpath(source_file_path, dir_path_content)

            dest_file_name = os.path.splitext(rel_path)[0] + '.html'
            dest_file_path = os.path.join(dest_dir_path, dest_file_name)

            os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)

            generate_page(source_file_path, template_path, dest_file_path, basepath)
            

    # crawl through content directory

        # for each markdown file, generate a new .html file using the same template.html

        # Should be written to the public directory in the same directory structure
    