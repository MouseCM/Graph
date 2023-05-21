import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image  
from tkinter import filedialog
from sources import data_processing

def run():
    global app
    app = tk.Tk()
    app.title('Mouse Graph')
    app.geometry("960x600")

    database()

    create_welcome()

    create_about()

    create_home()

    app.mainloop()

def database():
    global bg1, bg2, bg3

    img1 =Image.open('data/home_bg.jpg')
    bg1 = ImageTk.PhotoImage(img1)
    
    img2 = Image.open('data/data.jpeg')
    bg2 = ImageTk.PhotoImage(img2)

    img3 = Image.open('data/me.jpg')
    bg3 = ImageTk.PhotoImage(img3)

def create_welcome():
    global f_welcome
    f_welcome = Frame(app)
    canvas_w = Canvas(f_welcome, width = 960,height = 600)
    canvas_w.create_image( -865, -90, image = bg1, anchor = 'nw')
    canvas_w.create_text( 500, 50, text = 'Welcome to Mouse Graph', font = ('Helvetica bold', 40))
    start = Button(canvas_w, text = "Home", height= 3, width=8, command = home, fg = 'blue').pack(pady = 210)
    about_us = Button(canvas_w, text = 'About Us', command = about, height=3, width=8, fg = 'green').pack(pady = 10)
    exit_but = Button(canvas_w, text = 'Exit', command = exit, height=1, width=3, fg = 'red').pack()
    canvas_w.pack(fill = 'both', expand = True)
    f_welcome.pack(fill = 'both', expand = True)    

def create_about():
    global f_about
    f_about = Frame(app)
    canvas_a = Canvas(f_about, width = 960,height = 600)
    canvas_a.create_image( -850, -800, image = bg3, anchor = "nw")
    back = Button(canvas_a, text = 'Back', fg = 'green', command = welcome, height= 1, width=3).pack(pady = 20)
    canvas_a.create_text( 500, 150, text = '- This application was creadted by Mouse \n- Mouse Graph is application used to help users draw charts easily from excel files ', font = ('Helvetica bold', 18))
    canvas_a.pack(fill = "both", expand = True)

def create_home():
    global f_home, canvas_h, e1, e2
    f_home = Frame(app)
    canvas_h = Canvas(f_home, width = 960,height = 600)
    canvas_h.create_image( 0, -240, image = bg2, anchor = "nw")
    back_welcome = Button(canvas_h, text = 'Back', fg = 'green', height= 1, width=3, command = welcome).pack(pady = 10)
    canvas_h.create_text( 490, 180, text = 'Choose file you want to make graph', font = ('Helvetica bold', 18))
    canvas_h.create_text( 400, 210, text = 'Enter column (number)', font = ('Helvetica bold', 14))
    e1 = Entry(f_home)
    canvas_h.create_window(580, 210, window = e1)
    canvas_h.create_text( 385, 230, text = 'Enter start row', font = ('Helvetica bold', 14))
    e2 = Entry(f_home)
    canvas_h.create_window(580, 230, window = e2)
    choose_file = Button(canvas_h, text = 'Choose file', height = 2,  width = 7, fg = 'blue', command = choose).pack(pady = 200)
    canvas_h.pack(fill = 'both', expand = True)

def exit():
    app.destroy()

def welcome():
    f_home.pack_forget()
    f_about.pack_forget()
    f_welcome.pack(fill = 'both', expand = True)

def about():
    f_welcome.pack_forget()
    f_about.pack(fill = 'both', expand = True)

def home():
    f_welcome.pack_forget()
    f_home.pack(fill = 'both', expand = True)

def choose():
    app.filename = filedialog.askopenfilename()
    file_pos = app.filename
    data_processing.process(file_pos, e1.get(), e2.get())

