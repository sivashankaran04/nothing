import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root, width=500, height=350, bg='lightblue', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="Image Converter", bg='lightblue')
label1.config(font=('helvetica', 25))
canvas1.create_window(250, 60, window=label1)


def getPNG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browse_png = tk.Button(text="Select PNG file", command=getPNG, bg="blue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 130, window=browse_png)


def convert():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)


saveasbutton = tk.Button(text="Convert PNG to JPG", command=convert, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 180, window=saveasbutton)
root.mainloop()
