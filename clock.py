import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")  # Format: Hours:Minutes:Seconds
    label.config(text=current_time)
    label.after(1000, update_clock)  # Update every 1000 milliseconds (1 second)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Arial", 48), bg="black", fg="cyan")
label.pack(padx=20, pady=20)

update_clock()
root.mainloop()
