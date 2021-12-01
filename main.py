# Imports
import dearpygui.dearpygui as dpg

#getting Tkinter for monitor size recognition
import tkinter as tk

root = tk.Tk()

# Variables
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Uncomment the below if you can't use Tkinter and edit the numbers accordingly

#screenWidth = 1920
#screenHeight = 1080

# Functions
def gorillas():
    print("Gorillas are the largest living primates")

def gorillaNames():
    print("the scientific name for the Western Lowland gorilla is\ngorilla gorilla gorilla")
def happy():
    print("Don’t worry.\nBe happy")
def car():
    print("       .--.\n      |    |\n .----      --.\n|              |\n -()---------()-")

def printStatement(sender, app_data):
    print(dpg.get_value("customInput"))

# Setup
dpg.create_context()
dpg.create_viewport(title="Print Statements! Overcomplecated edition", width=int(screenWidth), height=int(screenHeight))
dpg.setup_dearpygui()

with dpg.window(label="Normal Stuff...", width=int(screenWidth/2), height=int(screenHeight/2),  pos=(0, 3)):
    dpg.add_text("Here is the stuff you wanted me to do...")
    dpg.add_button(label="Gorillas!", callback=gorillas)
    dpg.add_button(label="Gorilla names", callback=gorillaNames)
    dpg.add_button(label="Be happy!", callback=happy)
    dpg.add_button(label="Carz!", callback=car)

with dpg.window(label="hmm... Extras!", width=int(screenWidth/2), height=int(screenHeight/2), pos=(int(screenWidth/2), 3)):
    dpg.add_text("Custom Stuff!")
    dpg.add_input_text(tag="input_text_1", label="input", default_value="some text")
    dpg.add_button(tag="btn_1", label="...and see it printed out!", callback=lambda: print(dpg.get_value("input_text_1")))


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()