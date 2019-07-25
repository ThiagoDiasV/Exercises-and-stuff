import PIL.Image, PIL.ImageTk
from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('Python Image Resizer')
root.geometry('550x500')

window_title = Label(root, text='Python Image Resizer 1.0', font=('Helvetica', 16), pady=20)
window_title.pack()

img = PIL.ImageTk.PhotoImage(PIL.Image.open(''))  # Insert any image here
panel = Label(root, image = img)
panel.pack()

new_width_label = Label(root, text='New width value(px)')
new_width_label.pack()

new_width = Entry(background='white')
new_width.pack()

new_height_label = Label(root, text='New height value(px)')
new_height_label.pack()

new_height = Entry(background='white')
new_height.pack()

new_filename_label = Label(root, text='New filename')
new_filename_label.pack()

new_filename = Entry(background='white')
new_filename.pack()


def process_file():
    file_wrapper = filedialog.askopenfile()
    print(file_wrapper)
    file_name = file_wrapper.name
    file_extension = os.path.splitext(file_name)[1]

    image = PIL.Image.open(file_name)
    width = int(new_width.get())
    height = int(new_height.get())
    image = image.resize((width, height), PIL.Image.ANTIALIAS)
    image.save(new_filename.get() + file_extension)
    image.show()


button = Button(root, text='Open file', command=process_file)
button.pack()

root.mainloop()
