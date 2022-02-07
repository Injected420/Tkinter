from tkinter import Frame, Entry, Button, Tk, mainloop, Label, messagebox
import tkinter.messagebox
# This is a good template for any Calcuation GUI, change the calcuation that is done and the text
# This example will output the results in a NEW window/widget, that is why we import messagebox


class Kiloconvert:
    def __init__(self):
        self.main_window = Tk()
        self.top_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        # This label is for the input
        self.prompt_label = Label(
            self.top_frame, text='Enter a Distance in Kilometers:')
        # This is the input box
        self.kilo_entry = Entry(self.top_frame, width=10)
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')
        # The button for the widget
        self.calc_button = Button(
            self.bottom_frame, text='Convert', command=self.convert)
        # Make a quit button
        self.quit_button = Button(
            self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # Pack Buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        # Pack Frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        mainloop()

        # Make the Convert function
    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        miles = format(miles, '.2f')
        messagebox.showinfo('Results', str(
            kilo) + " kilometers is equal to " + str(miles) + " miles")


kmessage = Kiloconvert()
