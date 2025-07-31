from tkinter import Tk, Label
import time

def digital_clock():
    current_time = time.strftime("%I:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, digital_clock)


dc = Tk()
dc.title("Digital Clock")
dc.geometry("620x150")
dc.configure(bg="black")

# Create a label to display time
label = Label(dc, font=("Arial", 60), bg="black", fg="cyan", bd=25)
label.pack()

# Start updating the clock
digital_clock()

# Run the GUI event loop
dc.mainloop()
