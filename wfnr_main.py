import tkinter as tk
import os
from time import sleep
# Accidentally first pulled and then pushed the previous version in VSCode ;-;

# NOTE: All of this is a "sketch"
# The progress means how much progress it will contribute to the 
# overall progress once it's fully done
# These percentage are rough estimates and should be taken in 
# form of how valuable they are to the program itself


# Declare the variables that will store important data
# * Eggs or smth
'''
    "Eggs or smth" for:
    "E" Damn...
    "g" why
    "g" do
    "s" I
    " " always
    "o" stay
    "r" up
    " " till
    "s" midnight
    "m" programming
    "t" every
    "h" day...
    "\n" night?
'''

# Create the TKinter window and it's window properties
root = tk.Tk()

root.title("WFNR v0.0.0")
root.geometry("480x270") # Prev : 640x360
root.resizable(False, False)


# TKinter styling variables
# Progress -> +15%


# Find the specified watermark and remove it from the files that were found earlier
# Progress -> +30%


# If chosen, look for the file types
# Progress -> +15%


# Find the directory
# Progress -> +15%


# Make all of the window elements
# Progress -> +19% (5% remaining)
# ! IMPORTANT TODO: Add newlines or empty lines for better text formatting
# TODO: Make the entry and button align on the same line
# ? Just use a grid.
# Make the placeholders better
header = tk.Label(root, text="Watermark File Name Removal", font=("Bold", 20))
path = tk.Entry(root, justify="center")
path.insert(0, "Path to directory")
pickPath = tk.Button(root, text="Search", cursor="hand2")
fileTypeMessage = tk.Label(root,text="Input any files extensions separated by a comma (Optional)")
fileTypes = tk.Entry(root,justify="center", width=30)
fileTypes.insert(0, "File types (E.g. png, mp3, ect) ")
findFiles = tk.Button(root, text="Fetch Files", cursor="hand2")
# Will be updated automatically
filesFound = tk.Label(root, text="")
watermark = tk.Entry(root, justify="center")
watermark.insert(0, "Watermark")
startProcess = tk.Button(root, text="Rename All", cursor="hand2")


# Pack (display) all of the elements
header.pack()
path.pack()
pickPath.pack()
fileTypeMessage.pack()
fileTypes.pack()
findFiles.pack()
filesFound.pack()
watermark.pack()
startProcess.pack()

root.mainloop()
