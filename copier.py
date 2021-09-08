import os
import shutil
import sys

#rename the files and set the path as you need
my_js = "my.js"
my_css = "my.css"
vivaldi_path = "%localappdata%\Vivaldi\Application"

# 4
def quitting():
    input("Press Enter to quit.")
    sys.exit()
# 5
def is_valid_folder(folder_name):
    if folder_name.replace(".", "").isdigit():
        return True
    else:
        return False
# 6
vivaldi_path = os.path.expandvars(vivaldi_path)
for folder in os.listdir(vivaldi_path):
    if is_valid_folder(folder):
        break
else:
    print("No valid folder found.")
    quitting()
# 7
vivaldi_resources_path = os.path.join(vivaldi_path, folder, "resources", "vivaldi")
# 8
shutil.copy(my_js, vivaldi_resources_path)
shutil.copy(my_css, vivaldi_resources_path)
# 9
browser_html_path = os.path.join(vivaldi_resources_path, "browser.html")
# 10
with open(browser_html_path, "r") as browser_html:
    browser_html_content = browser_html.read()
    browser_html_content = browser_html_content.replace("</head>", "  <link rel=\"stylesheet\" href=\"" + my_css + "\" />\n  </head>")
    browser_html_content = browser_html_content.replace("</body>", "  <script src=\"" + my_js + "\"></script>\n  </body>")
with open(browser_html_path, "w") as browser_html:
    browser_html.write(browser_html_content)
# 12
print("Successfully installed.")
quitting()