import tkinter as tk
from time import*

#Create the main GUI window
root = tk.Tk()
root.title("DIGITAL CLOCK")

#Function
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    
    day_string = strftime("%A")
    day_label.config(text=day_string)
    
    date_string = strftime("%d-%B-%Y")
    date_label.config(text=date_string)
    
    root.after(1000,update)
    

#Time label    
time_label = tk.Label(root, font=("Debug",50),foreground="#DD88CF", background="#F8E7F6")
time_label.pack()

#Day label
day_label = tk.Label(root, font=("Poppins",25),foreground="#eec0c8")
day_label.pack()

#Date label
date_label = tk.Label(root, font=("Poppins",45), foreground="#eec0c8")
date_label.pack()
update()       

root.mainloop()