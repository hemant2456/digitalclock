import tkinter as tk
import time

def update_clock():
    # Get current time and date
    current_time = time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    current_date = time.strftime("%A, %B %d, %Y")  # e.g., Monday, August 05, 2025
    
    # Update the time and date labels
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    # Schedule this function to be called again after 1 second
    time_label.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Digital Clock with Date")

# Time label configuration
time_label = tk.Label(root, font=("Arial", 48), bg="black", fg="cyan")
time_label.pack(padx=20, pady=(20, 0))  # More padding on top

# Date label configuration
date_label = tk.Label(root, font=("Arial", 24), bg="black", fg="white")
date_label.pack(padx=20, pady=(0, 20))  # More padding below

# Start the clock update loop
update_clock()

# Run the GUI event loop
root.mainloop()
