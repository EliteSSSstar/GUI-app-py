import csv
import tkinter

import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from tkinter import *

from PIL._tkinter_finder import tk
from matplotlib import style  # type: ignore
from PIL import Image, ImageTk  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from tkinter import ttk, messagebox, filedialog  # type: ignore
from matplotlib.figure import Figure  # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # type: ignore
from matplotlib.backends._backend_tk import NavigationToolbar2Tk  # type: ignore




# Themes
primary = ['black', 'white']
reverse = ['white', 'black']
secondary = ['grey', '#f4f4f4']
second2 = ['#202020', '#f4f4f4']
close = ['close_dark.png', 'close_light.png']
open = ['open_dark.png', 'open_light.png']

# File path
file_path = "../data_File/IBM.csv"


# Design and create the plots
def load_data3(self, canvas):  # Hisogram
    try:
        if file_path:
            ox_data = pd.read_csv(file_path, index_col=0)
            high_values = ox_data['High'].values
            low_values = ox_data['Low'].values
            open_values = ox_data['Open'].values
            adj_values = ox_data['Adj Close'].values

            fig = Figure(facecolor=secondary[self.mod])
            ax = fig.add_subplot(111, facecolor=secondary[self.mod])
            ax.plot(high_values, 'o', color='red', label='High Values')
            ax.plot(low_values, '-', color='blue', label='Low Values')
            ax.plot(open_values, '_', color='orange', label='Open Values')
            ax.plot(adj_values, 'v--', color='green', label='Adj Values')
            ax.set_title("High and Low Values", color=reverse[self.mod])
            ax.set_xlabel("Index", color=reverse[self.mod])
            ax.set_ylabel("Value", color=reverse[self.mod])
            ax.grid(color=reverse[self.mod])
            ax.legend(facecolor=secondary[self.mod], edgecolor=secondary[self.mod])

            canvas.figure = fig
            canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {e}")


def load_data4(self, canvas):  # Pie Chart
    try:
        if file_path:
            ox_data = pd.read_csv(file_path, index_col=0)
            adj_values = ox_data['Adj Close'].values
            labels = ox_data.index

            fig = Figure(facecolor=secondary[self.mod])
            ax = fig.add_subplot(111, facecolor=secondary[self.mod])
            sizes = adj_values[:10]
            ax.pie(sizes, labels=labels[:10], autopct='%1.1f%%', startangle=140,
                   textprops={'color': reverse[self.mod]})
            ax.set_title("Adjusted Close Values Pie Chart", color=reverse[self.mod])

            canvas.figure = fig
            canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {e}")


def load_data5(self, canvas):  # Bar Chart
    try:
        if file_path:
            ox_data = pd.read_csv(file_path, index_col=0)
            data = ox_data['Close'].values
            dates = ox_data.index

            fig = Figure(facecolor=second2[self.mod])
            ax = fig.add_subplot(111, facecolor=second2[self.mod])
            ax.bar(dates[:10], data[:10], color='skyblue')
            ax.set_title("Close Prices Bar Chart", color=reverse[self.mod])
            ax.set_xlabel("Date", color=reverse[self.mod])
            ax.set_ylabel("Close Price", color=reverse[self.mod])
            ax.tick_params(colors=reverse[self.mod])
            fig.tight_layout()

            canvas.figure = fig


            canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {e}")

class App():
    # create the GUI
    mod = 0
    root = Tk()
    win_width = root.winfo_screenwidth()
    win_height = root.winfo_screenheight()

    # Hover effect
    @staticmethod
    def on_enter(event):
        event.widget.config(cursor="hand2")

    # Leave effect
    @staticmethod
    def on_leave(event):
        event.widget.config(cursor="")

    # Design and create the GUI
    def __init__(self) -> None:
        self.file_path = ""  # Initialize file path as an empty string
        self.data_table = None
        root = self.root
        root.title("AI Gui")
        root.state('zoomed')
        root.resizable(0, 0)

        self.render_components()

    # Create the widgets
    def create_widgets(self):
        self.file_menu()
        self.shadow_widgets()
        self.dat_table()

    # Shadow function Violet
    @staticmethod
    def shadow(frame, frame2):
        # Add violet shadow to the TOP of the header
        top_shadow = Frame(frame, bg='violet')
        top_shadow.configure(width=frame.winfo_screenwidth(), height=5)
        top_shadow.pack(side=TOP, fill=X)  # Shadow length

        # Add violet shadow at the bottom of the GUI
        bottom_shadow = Frame(frame2, bg='violet')
        bottom_shadow.configure(width=frame2.winfo_screenwidth(), height=5)
        bottom_shadow.pack(side=BOTTOM, fill=X)  # Footer length

    def file_menu(self):
        # File menu
        menu_bar = Menu(self.root, fg='white', bg='black')
        self.root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0, fg='white', bg='black')
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=lambda: print("Open File"))
        file_menu.add_command(label="Save", command=lambda: print("Save File"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

    # Data Table
    def dat_table(self):
        # List Widget
        list_frame = Frame(self.root, bg='black')
        list_frame.pack(fill=BOTH, expand=True)

        listbox = Listbox(list_frame)
        listbox.pack(side=LEFT, fill=BOTH, expand=True)
        listbox.insert(END, "Option 1")
        listbox.insert(END, "Option 2")
        listbox.insert(END, "Option 3")

        table_frame = Frame(self.root, bg='black')
        table_frame.pack(fill=BOTH, expand=True)

        self.data_table = ttk.Treeview(table_frame, columns=("A", "B", "C"), show='headings')
        self.data_table.heading("A", text="Date")
        self.data_table.heading("B", text="High")
        self.data_table.heading("C", text="Low")
        self.data_table.pack(fill=BOTH, expand=True)

    def csv_button(self):
        # Button to open CSV file
        btn_load_csv = Button(self.root, text="Load CSV", fg='white', bg='black', command=self.open_file_dialog)
        btn_load_csv.pack(side=TOP)



    # Open File
    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.load_data(file_path)

    # Load Data
    def load_data(self, file_path):
        try:    # Check if file path is valid
            if file_path:
                df = pd.read_csv(file_path)
                self.show_data_in_new_window(df)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")

    # Display dat_Table in a new window
    def show_data_in_new_window(self, df):
        data_window = Toplevel(self.root)
        data_window.title("Data Table")
        data_window.geometry("1500x600")
        data_table = ttk.Treeview(data_window)
        data_table.pack(fill=BOTH, expand=True)

        # Set up the table columns
        data_table["columns"] = list(df.columns)
        data_table["show"] = "headings"
        for col in df.columns:
            data_table.heading(col, text=col)

        # Insert data into the table
        for index, row in df.iterrows():
            data_table.insert("", END, values=list(row))

    # Function to open a new window and display the selected plot
    @staticmethod
    def open_plot_window(self, plot_func):
        new_window = Toplevel(self.root)
        new_window.geometry('800x600')
        new_window.title("Plot Window")

        plot_frame = Frame(new_window)
        plot_frame.pack(fill=BOTH, expand=True)

        # Create the canvas for plotting
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        # Add toolbar
        toolbar = NavigationToolbar2Tk(canvas, plot_frame)
        toolbar.update()
        toolbar.pack(side=TOP, fill=X)

        # Load the data
        plot_func(self, canvas)

    def radiobuttons(self, frame):
        radio_frame = Frame(frame, bg='black')
        radio_frame.pack(side=LEFT, padx=10)

        plot_type = StringVar()
        plot_type.set('Histogram')

        radio_histogram = Radiobutton(radio_frame, text="Histogram", variable=plot_type, value='Histogram',
                                      command=lambda: self.open_plot_window(self, load_data3))
        radio_histogram.pack(side=LEFT, padx=10)

        radio_pie = Radiobutton(radio_frame, text="Pie Chart", variable=plot_type, value='Pie Chart',
                                command=lambda: self.open_plot_window(self, load_data4))
        radio_pie.pack(side=LEFT, padx=10)

        radio_bar = Radiobutton(radio_frame, text="Bar Chart", variable=plot_type, value='Bar Chart',
                                command=lambda: self.open_plot_window(self, load_data5))
        radio_bar.pack(side=LEFT, padx=10)

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

        # render shadow
        self.shadow(root, frame2=root)

        # render file menu
        self.file_menu()

        self.topBar()  # Top bar
        # Define sideFrame dashboard
        side_dashboard, frame1, frame2 = self.verticalFrames()

        # render side dashboard
        self.render_side_dashboard(side_dashboard)
        self.render_text_canvas(frame2)  # Right side above
        self.render_data_canvas1(frame1)  # Left side above
        self.render_data_canvaspie(frame1)  # Left side below
        self.render_data_canvasbar(frame2)  # Right side below

    # Top bar Function
    def topBar(self):
        frame = Frame(self.root, bg=primary[self.mod], height=40)
        frame.pack(side=TOP, fill=X)
        Label(frame, text="AI GUI Pro+", fg=reverse[self.mod], bg=primary[self.mod], font=('Arial', 15)).pack(side=LEFT,
                                                                                                              padx=10,
                                                                                                              pady=0)

        # render radio buttons
        self.radiobuttons(frame)

        # render csv button
        self.csv_button()

        return frame



    def render_side_dashboard(self, parent):
        # Create a frame with the desired height
        frame = Frame(parent, bg=primary[self.mod], height=parent.winfo_screenheight() // 4,
                      width=parent.winfo_screenwidth())
        frame.pack(side=TOP, padx=20, pady=20)
        frame.pack_propagate(0)  # Prevent the frame from resizing

    # Create Frames
    def verticalFrames(self):
        # define sideFrame dashboard
        side_dashboard = Frame(self.root, bg=primary[self.mod], width=230)
        side_dashboard.pack(side=LEFT, fill=Y)

        # Create 2 Frames
        # left side position frame 1
        frame1 = Frame(self.root, bg=secondary[self.mod], width=(self.win_width * 2) // 5)
        frame1.pack(side=LEFT, fill=BOTH, expand=True, padx=10)
        frame1.pack_propagate(0)  # Prevent the frame from resizing

        # right side position frame 2
        frame2 = Frame(self.root, bg=second2[self.mod], width=(self.win_width * 3) // 5)
        frame2.pack(side=LEFT, fill=BOTH, expand=True, padx=10)
        frame2.pack_propagate(0)  # Prevent the frame from resizing

        # return Frames
        return side_dashboard, frame1, frame2

    def render_text_canvas(self, parent):
        # Create a frame with the desired height
        frame = Frame(parent, bg=second2[self.mod], height=(parent.winfo_screenheight() // 2) - 100,
                      width=parent.winfo_screenwidth())
        frame.pack(side=TOP, padx=20, pady=20)
        frame.pack_propagate(0)  # Prevent the frame from resizing

        # Create the Text widget inside the frame
        text_widget = Text(frame, wrap=WORD, bg=second2[self.mod], fg=reverse[self.mod], font=('Arial', 17))
        text = """ The Nasdaq and S&P 500 hit new high afterStock Market Split, Pressured
        The market rally came under pressure, especially on the tech side. The Nasdaq fell sharply, led by Tesla (TSLA), Google-parent Alphabet (GOOGL) and other megacaps. The Nasdaq and S&P 500 fell below their 50-day lines, though the latter fought for that key level on Friday. The Dow Jones rose modestly, while the small-cap Russell 2000 jumped. Hospitals and aerospace/defense firms were strong performers. Treasury yields were little changed after mixed inflation data."""
        text_widget.insert(END, text)
        text_widget.config(state=DISABLED, relief=FLAT)
        text_widget.pack(fill=BOTH, expand=True)

    def render_side_dashboard(self, side_dashboard):
        open_button = Button(side_dashboard, bg=primary[self.mod], fg=reverse[self.mod],
                             font=('Arial', 12), command=self.open_side_dashboard,
                             relief=FLAT, image=self.open, compound=LEFT,
                             highlightbackground=primary[self.mod], highlightcolor=primary[self.mod])
        open_button.pack(side=TOP, fill=X, pady=10)

        open_button.bind("<Enter>", self.on_enter)
        open_button.bind("<Leave>", self.on_leave)

    def open_side_dashboard(self):
        root = self.root  # root positioning
        options = ['Change Theme', 'Add Contacts']

        # design side dashboard
        side_dashboard = Frame(root, bg=primary[self.mod], width=200, height=2000)
        side_dashboard.place(x=0, y=0)
        side_dashboard.pack_propagate(0)

        frame = Frame(side_dashboard, bg=primary[self.mod], width=200, height=10)
        frame.pack(side=TOP, fill=X, padx=10)

        Label(frame, text='AI GUI Pro+', bg=primary[self.mod], fg=reverse[self.mod], font=('Arial', 15)).pack(side=LEFT,
                                                                                                              fill=X,
                                                                                                              pady=0)

        # close dashboard button
        btnFrame = self.util_frame(side_dashboard)

        close_btn = Button(btnFrame, bg=primary[self.mod], image=self.close_img, fg=reverse[self.mod], relief=FLAT,
                           command=lambda: side_dashboard.destroy())
        close_btn.pack(side=RIGHT, padx=10, pady=10)

        close_btn.bind("<Enter>", self.on_enter)
        close_btn.bind("<Leave>", self.on_leave)

        # Change theme button Placement
        btnFrame2 = self.util_frame(side_dashboard)

        theme_btn = Button(btnFrame2, text=options[0], bg=primary[self.mod], fg=reverse[self.mod], relief=FLAT,
                           font='Arial 14',
                           command=self.change_theme)
        theme_btn.place(x=0, y=0)

        # Change theme button
        btnFrame3 = self.util_frame(side_dashboard)

        contacts_btn = Button(btnFrame3, text=options[1], bg=primary[self.mod], fg=reverse[self.mod], relief=FLAT,
                              font='Arial 14')
        contacts_btn.place(x=0, y=0)

    def util_frame(self, side_dashboard):
        btnFrame = Frame(side_dashboard, bg=primary[self.mod], width=200, height=40)
        btnFrame.pack(side=TOP, fill=X)
        btnFrame.pack_propagate(0)
        return btnFrame

    # Change Theme Function
    def change_theme(self):
        self.mod = 0 if self.mod == 1 else 1

        for i in self.root.winfo_children():
            i.destroy()
        self.render_components()

    # Histograme Display
    def render_data_canvas1(self, parent):
        # Create Frame
        frame = Frame(parent, bg=second2[self.mod], height=80)
        frame.pack(side=TOP, fill=BOTH, expand=True)
        frame.pack_propagate(0)

        # Create the canvas
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        # Add toolbar
        toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=True)
        toolbar.update()
        toolbar.pack(anchor='w', fill=X)
        # Pack canvas to apear on top
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

        # Load Data
        load_data3(self, canvas)

    # Pie Display
    def render_data_canvaspie(self, parent):
        # Create Frame
        frame = Frame(parent, bg=second2[self.mod])
        frame.pack(side=TOP, fill=BOTH, expand=True)
        frame.pack_propagate(0)

        # Create the canvas
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=frame)

        # Add toolbar
        toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=True)
        toolbar.update()
        toolbar.pack(anchor='w', fill=X)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

        # Load Data
        load_data4(self, canvas)

    # Bar Display
    def render_data_canvasbar(self, parent):
        # Create Frame
        frame = Frame(parent, bg=second2[self.mod])
        frame.pack(side=TOP, fill=BOTH, expand=True)
        frame.pack_propagate(0)

        # Create the canvas
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        # Add toolbar
        toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(anchor='w', fill=X)

        # Load Data
        load_data5(self, canvas)

# Run App program
App()
mainloop()
