import tkinter as tk
import matplotlib.pyplot as plt

plt.close()

# Create the main window
root = tk.Tk()
root.title("Main Page: IRB 340 Delta Robot Simulation")

# Set the size of the window
width = 800
height = 60
0
root.geometry(f"{width}x{height}")

def mode1Page():
    root.destroy()
    import mode1

def mode2Page():
    root.destroy()
    import mode2
 
# Create a label widget
topic = tk.Label(root, text="IRB 340 Delta Robot Simulation", font=("Kanit", 30, "bold"))
topic.grid(row=1, column=1, columnspan=9, pady=20, sticky="nsew")

subtopic = tk.Label(root, text="There are 2 modes which are:", font=("Kanit", 20, "bold"))
subtopic.grid(row=2, column=1, columnspan=9, pady=30, sticky="nsew")

subtopic2 = tk.Label(root, text="Mode 1: Setting coordinates for the Delta Robot to move to a specific point.", font=("Kanit", 18))
subtopic2.grid(row=3, column=1, columnspan=9, pady=10, sticky="nsew")

subtopic3 = tk.Label(root, text="Mode 2: Specifying coordinates for all the points that you want the Delta Robot to move to.", font=("Kanit", 18))
subtopic3.grid(row=5, column=1, columnspan=9, pady=10, sticky="nsew")

# Buttons
# Create a button with a command
mode1 = tk.Button(root, text="Mode 1", font=("Kanit", 14, "bold"), command=mode1Page)
mode1.grid(row=4, column=5, padx=10, pady=40)

# Create a button with a command
mode2 = tk.Button(root, text="Mode 2", font=("Kanit", 14, "bold"), command=mode2Page)
mode2.grid(row=6, column=5, padx=10, pady=40)

# Center the buttons
for i in range(11):
    root.columnconfigure(i, weight=1)

# Run the Tkinter event loop
root.mainloop()
