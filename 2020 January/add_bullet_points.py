#Adds Markdown Bullet Points to a list in the clipboard

import pyperclip

def bullet_point_builder(text):
    if text:
        bullet_list = text
    else:
        bullet_list = pyperclip.paste()
    
    lines = bullet_list.split("\n")
    
    for i in range(len(lines)):
        if i < len(lines):
            lines[i] = "* " + lines[i]
    
    bullet_list = ""
    for i in range(len(lines)):
        bullet_list = bullet_list + lines[i] + "\n"
        
    
    
    pyperclip.copy(bullet_list)
    
if __name__ == "__main__":
    bullet_point_builder("")