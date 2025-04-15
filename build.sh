python3 src/main.py "/static_site_generator/"
cp -r static/index.css docs/index.css
mkdir -p docs/images
cp -r static/images/* docs/images/