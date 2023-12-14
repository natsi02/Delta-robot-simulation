import tkinter as tk
from tkinter import messagebox
import numpy as np
from pose_mode import delta_pose_mode
import matplotlib.pyplot as plt

# Create the main window
root = tk.Tk()
root.title("Mode 2: Pose Mode")

global flag
flag = 0

def mainPage():
    root.destroy()
    import main
    
def validate_input(P):
    if not P:  # Check if the input is empty
        return True
    try:
        float(P)  # Try to convert the input to a float
        return True  # Input is numeric
    except ValueError:
        if P == '-' and P.count('-') == 1:
            return True  # Allow a single minus symbol at the beginning
        messagebox.showerror("Error", "Please enter a numeric value.")
        return False  # Input is not numeric

def create_input_boxes(num_rows):
    entries = []

    for i in range(num_rows):
        for coord in range(3):
            label = tk.Label(root, text=f"Pose {i + 1}, Coordinate {chr(ord('X') + coord)}:", font=("Kanit", 14, "bold"))
            label.grid(row=i + 6, column=2 * coord + 4, padx=1, pady=20)

            entry = tk.Entry(root, validate="key", validatecommand=(root.register(validate_input), '%P'))
            entry.grid(row=i + 6, column=2 * coord + 5, padx=1, pady=20)

            entries.append(entry)

    return entries

fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d')

delta_pose_mode(0,ax,flag)
flag = 1

def get_values(entries):
    values = []
    for i in range(len(entries) // 3):
        x = float(entries[i * 3].get())
        y = float(entries[i * 3 + 1].get())
        z = float(entries[i * 3 + 2].get())
        values.append([x, y, z])

    print("Entered values:", values)
    delta_pose_mode(values,ax,flag)

def generate_input_boxes():
    global entries
    num_poses = int(entry_num_poses.get())
    entries = create_input_boxes(num_poses)
    return num_poses
    
# Set weights to make the content expand and center
for i in range(11):
    root.columnconfigure(i, weight=1)
  
# Create a label widget
topic = tk.Label(root, text="Delta Robot Simulation", font=("Kanit", 30, "bold"))
topic.grid(row=1, column=1, columnspan=9, pady=20, sticky="nsew")

subtopic = tk.Label(root, text="Mode 2: Pose Mode", font=("Kanit", 20, "bold"))
subtopic.grid(row=2, column=1, columnspan=9, pady=5, sticky="nsew")

subtopic3 = tk.Label(root, text="Specifying coordinates for all the points that you want the Delta Robot to move to.", font=("Kanit", 18))
subtopic3.grid(row=3, column=1, columnspan=9, pady=10, sticky="nsew")

# Entry for the number of poses
label_num_poses = tk.Label(root, text="Enter the number of poses:", font=("Kanit", 16))
label_num_poses.grid(row=4, column=4, padx=1, pady=30)

entry_num_poses = tk.Entry(root, validate="key", validatecommand=(root.register(validate_input), '%P'))
entry_num_poses.grid(row=4, column=5, padx=1, pady=30)

# Button to generate input boxes
generatebutton = tk.Button(root, text="Enter", font=("Kanit", 14, "bold"), command=generate_input_boxes)
generatebutton.grid(row=5, column=4, pady=20)

# Button to get the values
simbutton = tk.Button(root, text="Simulate", font=("Kanit", 14, "bold"), command=lambda: get_values(entries))
simbutton.grid(row=5, column=5, pady=20)

# Create a button with a command
backbutton = tk.Button(root, text="Back", font=("Kanit", 14, "bold"), command=mainPage)
backbutton.grid(row=5, column=6, pady=20)

# Run the Tkinter event loop
root.mainloop()
