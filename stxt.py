from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import ctypes
import sys

# Increase DPI awareness for sharper visuals
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Setup variables
name = "x-text"
default_file_name = "new file"
current_file_path = default_file_name
file_types = [("Text Files", "*.txt"), ("Markdown", "*.md")]
current_theme = "light"

# Initialize tkinter
root = Tk()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.title(f"{name} - {current_file_path}")
root.geometry("500x400")

# Define themes
themes = {
    "light": {
        "bg": "white",
        "fg": "black",
        "insertbackground": "black"
    },
    "dark": {
        "bg": "black",
        "fg": "white",
        "insertbackground": "white"
    },
    "orange": {
        "bg": "orange",
        "fg": "black",
        "insertbackground": "black"
    },
    "red": {
        "bg": "red",
        "fg": "white",
        "insertbackground": "white"
    },
    "blue": {
        "bg": "blue",
        "fg": "white",
        "insertbackground": "white"
    },
    "green": {
        "bg": "green",
        "fg": "black",
        "insertbackground": "black"
    }
}

def apply_theme(theme_name):
    global current_theme
    if theme_name in themes:
        theme = themes[theme_name]
        txt.config(bg=theme["bg"], fg=theme["fg"], insertbackground=theme["insertbackground"])
        root.config(bg=theme["bg"])
        current_theme = theme_name

# Define handler functions
def file_action(action):
    global current_file_path

    if action == "open":
        file = filedialog.askopenfilename(filetypes=file_types)
        if file:
            current_file_path = file
            root.title(f"{name} - {current_file_path}")
            with open(file, 'r') as f:
                txt.delete(1.0, END)
                txt.insert(INSERT, f.read())

    elif action == "new":
        current_file_path = default_file_name
        txt.delete(1.0, END)
        root.title(f"{name} - {current_file_path}")

    elif action in ["save", "saveAs"]:
        if current_file_path == default_file_name or action == "saveAs":
            file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=file_types)
            if file:
                current_file_path = file
        
        if current_file_path != default_file_name:
            with open(current_file_path, "w") as f:
                f.write(txt.get(1.0, END).strip())
            root.title(f"{name} - {current_file_path}")

# Function to update window title on text change
def on_text_change(event):
    root.title(f"{name} - {current_file_path}*")

# Text area
txt = scrolledtext.ScrolledText(root, wrap=WORD)
txt.grid(row=0, column=0, sticky=N+S+E+W)
txt.bind('<KeyPress>', on_text_change)

# Apply default theme
apply_theme(current_theme)

# Menu setup
menu = Menu(root)

file_dropdown = Menu(menu, tearoff=False)
file_dropdown.add_command(label="New", command=lambda: file_action("new"))
file_dropdown.add_command(label="Open", command=lambda: file_action("open"))
file_dropdown.add_separator()
file_dropdown.add_command(label="Save", command=lambda: file_action("save"))
file_dropdown.add_command(label="Save As", command=lambda: file_action("saveAs"))
menu.add_cascade(label="File", menu=file_dropdown)

theme_dropdown = Menu(menu, tearoff=False)
theme_dropdown.add_command(label="Light Theme", command=lambda: apply_theme("light"))
theme_dropdown.add_command(label="Dark Theme", command=lambda: apply_theme("dark"))
theme_dropdown.add_command(label="Orange Theme", command=lambda: apply_theme("orange"))
theme_dropdown.add_command(label="Red Theme", command=lambda: apply_theme("red"))
theme_dropdown.add_command(label="Blue Theme", command=lambda: apply_theme("blue"))
theme_dropdown.add_command(label="Green Theme", command=lambda: apply_theme("green"))
menu.add_cascade(label="Themes", menu=theme_dropdown)

root.config(menu=menu)

# Load file from command-line argument if provided
if len(sys.argv) == 2:
    current_file_path = sys.argv[1]
    root.title(f"{name} - {current_file_path}")
    with open(current_file_path, 'r') as f:
        txt.delete(1.0, END)
        txt.insert(INSERT, f.read())

# Main loop
root.mainloop()


