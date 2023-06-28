import tkinter as tk
from src.SelectImage import select_file

current_selected_file = 'NO FILE SELECTED'


def file_dialog_ui(root):
    label = tk.Label(root, text=current_selected_file)

    def update_selected_file():
        global current_selected_file
        file_path = select_file()
        if file_path:
            current_selected_file = file_path
            label.config(text=current_selected_file)

    button = tk.Button(root, text="Upload image/pack",
                       command=update_selected_file)
    label.pack()
    button.pack()


def main():
    root = tk.Tk()
    root.title("Hello World")
    root.geometry("1280x720")

    title = tk.Label(root, text="Wallpaper Helper Plus v0.1",
                     font=("Helvetica", 16))

    title.pack()
    file_dialog_ui(root)
    root.mainloop()


if __name__ == "__main__":
    main()