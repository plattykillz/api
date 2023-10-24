import tkinter as tk

# Function to increment the counter
def increment():
    value.set(value.get() + 1)

# Function to decrement the counter
def decrement():
    value.set(value.get() - 1)

# Create the main window
root = tk.Tk()
root.title("Fancy Counter")

# Variable to store the counter value
value = tk.IntVar()
value.set(0)

# Create a label to display the counter value
counter_label = tk.Label(root, textvariable=value, font=("Arial", 36))
counter_label.pack()

# Create buttons for increment and decrement
increment_button = tk.Button(root, text="Increment", command=increment, font=("Arial", 18))
decrement_button = tk.Button(root, text="Decrement", command=decrement, font=("Arial", 18))

increment_button.pack()
decrement_button.pack()

# Run the main loop
root.mainloop()
