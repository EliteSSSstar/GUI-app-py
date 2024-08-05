import csv
import numpy as np # type: ignore
import pandas as pd # type: ignore
from tkinter import *
from matplotlib import style    # type: ignore
from PIL import Image, ImageTk  # type: ignore
import matplotlib.pyplot as plt # type: ignore
from tkinter import ttk, messagebox # type: ignore
from matplotlib.figure import Figure    # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg   # type: ignore
from matplotlib.backends._backend_tk import NavigationToolbar2Tk    # type: ignore


#Themes
primary = ['black', 'white']
reverse = ['white', 'black']
secondary = ['grey', '#f4f4f4']
second2 = ['#202020', '#f4f4f4']
close = ['close_dark.png', 'close_light.png']
open = ['open_dark.png', 'open_light.png']


class App():
    #create the GUI
    mod = 0
    root = Tk()
    win_width = root.winfo_screenwidth()
    win_height = root.winfo_screenheight()

    # Hover effect
    def on_enter(self, event):
        event.widget.config(cursor="hand2")

    # Leave effect
    def on_leave(self, event):
        event.widget.config(cursor="")

    #Design and create the GUI
    def __init__(self) -> None:
        root = self.root
        root.title("AI Gui")
        root.state('zoomed')
        root.resizable(0, 0)


        self.render_components()

    def render_components(self):
        root = self.root
        root.configure(background=primary[self.mod])
        # Images for open and close
        open_img = Image.open('../assets/' + open[self.mod])
        resized_image = open_img.resize((35, 28))
        self.open = ImageTk.PhotoImage(resized_image)

        # close image
        close_img = Image.open('../assets/' + close[self.mod])
        resized_image = close_img.resize((30, 30))
        self.close_img = ImageTk.PhotoImage(resized_image)



        self.topBar() #Top bar
        #Define sideFrame dashboard
        side_dashboard, frame1, frame2 = self.verticalFrames()

        #render side dashboard
        self.render_side_dashboard(side_dashboard)
        self.render_text_canvas(frame2) #Right side above


        # Top bar Function
    def topBar(self):
        frame = Frame(self.root, bg=primary[self.mod], height=40)
        frame.pack(side=TOP, fill=X)
        Label(frame, text="AI GUI Pro+", fg=reverse[self.mod], bg=primary[self.mod], font=('Arial', 15)).pack(side=LEFT, padx=10, pady=0    )
        return frame

    # Create Frames
    def verticalFrames(self):
        #define sideFrame dashboard
        side_dashboard = Frame(self.root, bg=primary[self.mod], width=230)
        side_dashboard.pack(side=LEFT, fill=Y)

        #Create 2 Frames
        #left side position frame 1
        frame1 = Frame(self.root, bg=secondary[self.mod], width=(self.win_width *2)// 5)
        frame1.pack(side=LEFT, fill=BOTH, expand=True, padx=10)
        frame1.pack_propagate(0) # Prevent the frame from resizing

        #right side position frame 2
        frame2 = Frame(self.root, bg=second2[self.mod], width=(self.win_width *3)// 5)
        frame2.pack(side=LEFT, fill=BOTH, expand=True, padx=10)
        frame2.pack_propagate(0) # Prevent the frame from resizing

        #return Frames
        return side_dashboard, frame1, frame2

    def render_text_canvas(self, parent):
        # Create a frame with the desired height
        frame = Frame(parent,bg=second2[self.mod], height=(parent.winfo_screenheight()//2)-100, width=parent.winfo_screenwidth())
        frame.pack(side=TOP, padx=20, pady=20)
        frame.pack_propagate(0)  # Prevent the frame from resizing


        def render_side_dashboard(self, side_dashboard):
            open_button = Button(side_dashboard, bg=primary[self.mod], fg=reverse[self.mod],
                                 font=('Arial', 12), command=self.open_side_dashboard,
                                 relief=FLAT, image=self.open, compound=LEFT,
                                 highlightbackground=primary[self.mod], highlightcolor=primary[self.mod])
            open_button.pack(side=TOP, fill=X, pady=10)

            open_button.bind("<Enter>", self.on_enter)
            open_button.bind("<Leave>", self.on_leave)

    def render_side_dashboard(self, side_dashboard):
        open_button = Button(side_dashboard, bg=primary[self.mod], fg=reverse[self.mod],
                             font=('Arial', 12), command=self.open_side_dashboard,
                             relief=FLAT, image=self.open, compound=LEFT,
                             highlightbackground=primary[self.mod], highlightcolor=primary[self.mod])
        open_button.pack(side=TOP, fill=X, pady=10)

        open_button.bind("<Enter>", self.on_enter)
        open_button.bind("<Leave>", self.on_leave)

    def open_side_dashboard(self):
        root = self.root # root positioning
        options = ['Change Theme', 'Add Contacts']

        #design side dashboard
        side_dashboard = Frame(root, bg=primary[self.mod], width=200, height=2000)
        side_dashboard.place(x=0, y=0)
        side_dashboard.pack_propagate(0)

        frame = Frame(side_dashboard, bg=primary[self.mod], width=200, height=10)
        frame.pack(side=TOP, fill=X, padx=10)

        Label(frame, text='AI GUI Pro+', bg=primary[self.mod], fg=reverse[self.mod], font=('Arial', 15)).pack(side=LEFT, fill=X, pady=0)

        # close dashboard button
        btnFrame = self.util_frame(side_dashboard)

        close_btn = Button(btnFrame, bg=primary[self.mod], image=self.close_img, fg=reverse[self.mod], relief=FLAT,
                           command=lambda: side_dashboard.destroy())
        close_btn.pack(side=RIGHT, padx=10, pady=10)

        close_btn.bind("<Enter>", self.on_enter)
        close_btn.bind("<Leave>", self.on_leave)

        #Change theme button Placement
        btnFrame2 = self.util_frame(side_dashboard)

        theme_btn = Button(btnFrame2, text=options[0], bg=primary[self.mod], fg=reverse[self.mod], relief=FLAT,
                           font='Arial 14',
                           command=self.change_theme)
        theme_btn.place(x=0, y=0)



    def util_frame(self, side_dashboard):
        btnFrame = Frame(side_dashboard, bg=primary[self.mod], width=200, height=40)
        btnFrame.pack(side=TOP, fill=X)
        btnFrame.pack_propagate(0)
        return btnFrame

    #Change Theme Function
    def change_theme(self):
        self.mod = 0 if self.mod == 1 else 1

        for i in self.root.winfo_children():
            i.destroy()
        self.render_components()

#Run App program
App()
mainloop()







