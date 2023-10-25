import tkinter as tk

def increment():
    value.set(value.get() + 1)

def decrement():
    value.set(value.get() - 1)

root = tk.Tk()
root.title("Fancy Counter")

value = tk.IntVar()
value.set(0)

counter_label = tk.Label(root, textvariable=value, font=("Arial", 36))
counter_label.pack()

increment_button = tk.Button(root, text="Increment", command=increment, font=("Arial", 18))
decrement_button = tk.Button(root, text="Decrement", command=decrement, font=("Arial", 18))

increment_button.pack()
decrement_button.pack()

root.mainloop()
