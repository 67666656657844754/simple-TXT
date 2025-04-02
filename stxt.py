from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import ctypes
import sys

# Increase DPI awareness for sharper visuals
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Setup variables
name = "Simple-TXT"
default_file_name = "new file"
current_file_path = default_file_name
file_types = [("Text Files", "*.txt"), ("Markdown", "*.md")]
current_theme = "light"
current_language = "en" English language 

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

# Define translations
translations = {
    "en": {
        "file": "File",
        "new": "New",
        "open": "Open",
        "save": "Save",
        "save_as": "Save As",
        "themes": "Themes",
        "light_theme": "Light Theme",
        "dark_theme": "Dark Theme",
        "orange_theme": "Orange Theme",
        "red_theme": "Red Theme",
        "blue_theme": "Blue Theme",
        "green_theme": "Green Theme",
        "language": "Language",
        "english": "English",
        "ukrainian": "Ukrainian"
    },
    "uk": {
        "file": "Файл",
        "new": "Новий",
        "open": "Відкрити",
        "save": "Зберегти",
        "save_as": "Зберегти як",
        "themes": "Теми",
        "light_theme": "Світла тема",
        "dark_theme": "Темна тема",
        "orange_theme": "Помаранчева тема",
        "red_theme": "Червона тема",
        "blue_theme": "Синя тема",
        "green_theme": "Зелена тема",
        "language": "Мова",
        "english": "Англійська",
        "ukrainian": "Українська"
    }
}

def apply_theme(theme_name):
    global current_theme
    if theme_name in themes:
        theme = themes[theme_name]
        txt.config(bg=theme["bg"], fg=theme["fg"], insertbackground=theme["insertbackground"])
        root.config(bg=theme["bg"])
        current_theme = theme_name

def change_language(lang):
    global current_language
    if lang in translations:
        current_language = lang
        rebuild_menu()  

def rebuild_menu():
    # Видалити старі меню
    root.config(menu=Menu(root))  # Очистити меню

    # Створити нове меню
    menu = Menu(root)

    # File dropdown
    file_dropdown = Menu(menu, tearoff=False)
    file_dropdown.add_command(label=translations[current_language]["new"], command=lambda: file_action("new"))
    file_dropdown.add_command(label=translations[current_language]["open"], command=lambda: file_action("open"))
    file_dropdown.add_separator()
    file_dropdown.add_command(label=translations[current_language]["save"], command=lambda: file_action("save"))
    file_dropdown.add_command(label=translations[current_language]["save_as"], command=lambda: file_action("saveAs"))
    menu.add_cascade(label=translations[current_language]["file"], menu=file_dropdown)

    # Themes dropdown
    theme_dropdown = Menu(menu, tearoff=False)
    theme_dropdown.add_command(label=translations[current_language]["light_theme"], command=lambda: apply_theme("light"))
    theme_dropdown.add_command(label=translations[current_language]["dark_theme"], command=lambda: apply_theme("dark"))
    theme_dropdown.add_command(label=translations[current_language]["orange_theme"], command=lambda: apply_theme("orange"))
    theme_dropdown.add_command(label=translations[current_language]["red_theme"], command=lambda: apply_theme("red"))
    theme_dropdown.add_command(label=translations[current_language]["blue_theme"], command=lambda: apply_theme("blue"))
    theme_dropdown.add_command(label=translations[current_language]["green_theme"], command=lambda: apply_theme("green"))
    menu.add_cascade(label=translations[current_language]["themes"], menu=theme_dropdown)

    # Language dropdown
    language_dropdown = Menu(menu, tearoff=False)
    language_dropdown.add_command(label=translations[current_language]["english"], command=lambda: change_language("en"))
    language_dropdown.add_command(label=translations[current_language]["ukrainian"], command=lambda: change_language("uk"))
    menu.add_cascade(label=translations[current_language]["language"], menu=language_dropdown)

    # Встановити нове меню
    root.config(menu=menu)

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

# Initial menu setup
rebuild_menu()

# Load file from command-line argument if provided
if len(sys.argv) == 2:
    current_file_path = sys.argv[1]
    root.title(f"{name} - {current_file_path}")
    with open(current_file_path, 'r') as f:
        txt.delete(1.0, END)
        txt.insert(INSERT, f.read())

# Main loop
root.mainloop()
