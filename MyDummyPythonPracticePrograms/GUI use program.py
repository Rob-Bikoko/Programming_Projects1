import tkinter as tk

def update_label():
    label.config(text="Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("600x600")

# Create a label
label = tk.Label(root, text="Click the button!")
label.pack(pady=50)

# Create a button
button = tk.Button(root, text="Click Me!", command=update_label)
button.pack(pady=60)

# Start the GUI event loop
root.mainloop()