import tkinter as tk
import tkinter.messagebox

class messageGui:
    # Miles = Kilometers * 0.6214
    def __init__(self):
        self.main_window = tk.Tk()
        # Create a Button, the text will appear on the face and the command will be executed 'on click'
        self.my_button = tk.Button(self.main_window, text='Click Here', command=self.do_command)
    
        self.quit_button = tk.Button(self.main_window, text='Quit', command=self.main_window.destroy)
        self.my_button.pack(side='left')
        self.quit_button.pack(side='right')

        tk.mainloop()

# The first word in showinfo will be the messagebox's title, the rest will be the text displayed
    def do_command(self):
        tk.messagebox.showinfo("Response", "Thanks for clicking, your click has been recorded!")

g = messageGui()