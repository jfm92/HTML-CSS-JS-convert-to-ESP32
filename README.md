# HTML-CSS-JS-convert-to-ESP32

Python script to join, serialize and adapt a web project with HTML+CSS+JS into a .h file compatible with ESP32 microcontroller, making easier web server front end development.

## Dependencies:

- Python3
- pip
- minify_html

### How to install minify_html:

```bash
pip install minify-html
```

## Ussage:

First make sure you HTML, CSS and JS files are on the same folder. And project files naming should be the next:
- html.main
- style.css
- script.js

Execute the next command where the scripts lives:
```bash
python convertWeb2ESP32 -i <relative_path_web_project> -o <path_where_save_header_file>
```