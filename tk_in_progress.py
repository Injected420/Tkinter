import tkinter as tk

"""def empty_window():
    # Create the main window
    main_window = tk.Tk()

    # Enter the tkinter main loop
    tk.mainloop()

empty_window()"""

class myGUI:
    def __init__(self):
        # Create main window
        self.main_window = tk.Tk()

        # Enter the loop
        tk.mainloop()

# Create an instance of the class
#my_gui = myGUI()

# Widget with Label

class myGui:
  def __init__(self):
      self.main_win = tk.Tk()
      self.label = tk.Label(self.main_win, text="This is the Label")

      # Call the Label Widget's pack method
      self.label.pack()

      # tk loop
      tk.mainloop()


# Widget with 2 Labels

class twolabels:
    def __init__(self):
        self.window = tk.Tk()
        self.label = tk.Label(self.window, text="Python Widget |")
        self.label1 = tk.Label(self.window, text="Please Enter Your Name: ")
        self.label.pack(side='left')
        self.label1.pack(side='left')
        tk.mainloop()

labs = twolabels()
