from tkinter import *
from PIL import Image,ImageTk
import os

def next_image():
    global counter
    img_label.config(image=image_array[counter%len(image_array)])
    counter = counter +1

counter = 0
root = Tk()

root.title('Wallpaper Viewer')
root.minsize(400,400)
root.configure(background='black')

files = os.listdir('wallpaper')
print(files)

image_array = []
for file in files:
    img = Image.open(os.path.join('wallpaper',file))
    resized_img = img.resize((300,300))
    image_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root,image = image_array[0])
img_label.pack(pady=(15,10))


next_btn = Button(root,text='Next',bg='white',fg='black',width=28, height=2,command=next_image)
next_btn.pack(pady=(5,5))






root.mainloop()