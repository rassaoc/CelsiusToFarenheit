from tkinter import *
from tkinter import ttk

class CelsiusToFahrenheit:

    def __init__(self, root):

        root.title("Celsius To Fahrenheit") #Set title of application

        mainFrame = ttk.Frame(root, padding="5") # Create the main frame
        mainFrame.grid(column=0, row=0, sticky=(N,W,E,S)) # Creates the grid
        root.columnconfigure(0, weight=1) # Configures the columns
        root.rowconfigure(0, weight=1) # Configures the rows

        inputText = ttk.Label(mainFrame, text="Input Temperature") # Creates the Label for telling user to input temperature
        inputText.grid(column=2, row=1) # Assigns label to grid

        self.temperature = StringVar()
        tempEntry = ttk.Entry(mainFrame, textvariable=self.temperature) # Creates temperature entry box
        tempEntry.grid(column=2, row=2) # Assigns entry box to grid

        cToFButton = ttk.Button(mainFrame, text="Celsius To Fahrenheit", command=self.CelToFar) # Creates button and assigns command
        cToFButton.grid(column=1, row=3) # Assigns Button to grid

        fToCButton = ttk.Button(mainFrame, text="Fahrenheit To Celsius", command=self.FarToCel) # Creates button and assigns command
        fToCButton.grid(column=3, row=3) # Assigns button to grid

        ttk.Label(mainFrame, text="Your Temp in C/F is: ").grid(column=1, row=4) # Creates label left of final temperature and assigns it to the grid

        self.changedTemp = StringVar()
        finalTempLabel = ttk.Label(mainFrame, textvariable=self.changedTemp) # Creates final Temperature Label
        finalTempLabel.grid(column=2, row=4) # Asigns final temp label to the grid

    def CelToFar(self):
        try: # Stops the code from making an error when the button is pressed with no entry
            tempC = int(self.temperature.get()) # Gets the current temp in Entry Box
            tempF = (9/5) * tempC + 32 # Converts Fahrenheit to Celsius
            self.changedTemp.set(tempF) # Changes the changedTemp variable so it will be shown in the label
        except ValueError:
            pass

    def FarToCel(self):
        try: # Stops the code from making an error when the button is pressed with no entry
            tempF = int(self.temperature.get()) # Gets temp in entry box
            tempC = (5/9) * (tempF - 32) # Converts Celsius to Fahrenheit
            self.changedTemp.set(tempC) # Changed changedTemp variable
        except ValueError:
            pass

root = Tk()
CelsiusToFahrenheit(root)
root.mainloop()
