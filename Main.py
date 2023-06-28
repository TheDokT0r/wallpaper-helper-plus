import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Hello World")
    root.geometry("1280x720")

    title = tk.Label(root, text="Wallpaper Helper Plus v0.1",
                    font=("Helvetica", 16))
    
    


    title.pack()

    root.mainloop()

if __name__ == "__main__":
    main()