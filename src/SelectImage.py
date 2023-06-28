from tkinter import filedialog


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg'), (
        'Image File', '.png'), ('Image File', '.jpeg'), ('Image File', '.gif'), ('Image File', '.bmp'), ('Image File', '.tiff'), ('Image File', '.webp'),
        ("Compressed File", '.zip'), ('Compressed File',
                                      '.rar'), ('Compressed File', '.7z'), ('Compressed File', '.tar'),
        ('Compressed File', '.gz'), ('Compressed File', '.bz2'),])
    return file_path