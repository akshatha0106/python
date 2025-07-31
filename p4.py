from tkinter import Tk, Label
import time

def digital_clock():
    current_time = time.strftime("%I:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, digital_clock)


root = Tk()
root.title("Digital Clock")
root.geometry("620x150")
root.configure(bg="black")

# Create a label to display time
label = Label(root, font=("Arial", 60), bg="black", fg="cyan", bd=25)
label.pack()

# Start updating the clock
digital_clock()

# Run the GUI event loop
root.mainloop()