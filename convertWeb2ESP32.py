import os
import minify_html
import argparse

parser = argparse.ArgumentParser(description='Transform HTML+CSS+JS project to a compatible ESP32 file.')
parser.add_argument("-i", "--input_dir", help="Relative direction to web project folder.")
parser.add_argument("-o", "--output_dir", help="Relative direction where header file will be saved.")

args = parser.parse_args()

# Build input and output absolute path
script_dir = os.path.dirname(__file__) 
htmlPath = vars(args)["input_dir"] + "\main.html"
cssPath = vars(args)["input_dir"] + "\style.css"
jsPath = vars(args)["input_dir"] + "\script.js"
outputFilePath = vars(args)["output_dir"] + "//" + vars(args)["input_dir"].split("\\")[-1] + "_Serialized.h"

htmlAbsPath = os.path.join(script_dir, htmlPath)
cssAbsPath = os.path.join(script_dir, cssPath)
jsAbsPath = os.path.join(script_dir, jsPath)
outputAbsFilePath = os.path.join(script_dir, outputFilePath)

fdHTML = open(htmlAbsPath, "r")
fdCSS = open(cssAbsPath, "r")
fdJS = open(jsAbsPath, "r")

# Get content of the web projct
htmlData = fdHTML.read()
cssData = fdCSS.read()
jsData = fdJS.read()

# Erase link to use CSS and JS in multiple files to join on a single file
modHTML = htmlData.replace('<link rel="stylesheet" href="style.css">', '<style>' + cssData + '</style>')
modHTML = modHTML.replace('<script src="script.js"></script>', '<script>' + jsData + '</script>')

# Erase unnecessary spaces
minified = minify_html.minify(modHTML, minify_js=True, minify_css=True, remove_processing_instructions=True)

# Write new header file with the content
fdOut = open(outputAbsFilePath, "w")
fdOut.write('#include <pgmspace.h> \n' + 'const char PAGE_MAIN[] PROGMEM = R"rawliteral( ' + minified + ')rawliteral";')
fdOut.close()

print("WebProject conversion succeed.")