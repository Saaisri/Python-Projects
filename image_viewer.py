from tkinter import *
from typing import Collection
#pillow to handle image files
from PIL import ImageTk, Image

root = Tk()
root.title("Computer")
root.iconbitmap('E:/Saaisri/Studies/Python/Tkinder/mobile.ico')

img1 = (Image.open("images/img1.jpg"))
re_img1 =img1.resize((300,200))

img2 = (Image.open("images/img2.jpeg"))
re_img2 =img2.resize((300,200))

img3 = (Image.open("images/img3.jpg"))
re_img3 =img3.resize((300,200))

img4 = (Image.open("images/img4.jpg"))
re_img4 = img4.resize((300,200))
#create the image/call image 3 steps find put in the var and put the var in the screen
my_img1 = ImageTk.PhotoImage(re_img1)
my_img2 = ImageTk.PhotoImage(re_img2)
my_img3 = ImageTk.PhotoImage(re_img3)
my_img4 = ImageTk.PhotoImage(re_img4)

image_list = [my_img1, my_img2, my_img3, my_img4]



my_label = Label(image= my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
    button_back = Button(root, text="<<", command= lambda:back(image_number-1))
    
    if image_number ==4:
        button_forward = Button(root, text=">>", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
    button_back = Button(root, text="<<", command= lambda:back(image_number-1))

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    if image_number == 1:
        button_back = Button(root, text=">>", state=DISABLED)


button_back = Button(root, text="<<", command= back , state=DISABLED)
button_exit = Button(root, text="Exit program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)














root.mainloop()