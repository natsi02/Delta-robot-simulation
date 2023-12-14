import tkinter as tk
from tkinter import messagebox
from point_mode import delta_point_mode
import matplotlib.pyplot as plt
import numpy as np

# Create the main window
root = tk.Tk()
root.title("Mode 1: Point Mode")

# Set the size of the window
width = 800
height = 600
root.geometry(f"{width}x{height}")

# Define variable
# Declare state as a global variable
global state, trajectory, last_traj, angles, last_angles, current_pose, count

# Trajectory
m = 10  # number of trajectory points
    
trajectory = np.zeros((3, m, 1))
last_traj = np.zeros((3, m, 1))    
angles = np.zeros((3, m, 1))    
last_angles = np.zeros((3, m, 1))     
current_pose = np.zeros(3)
count = 0

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
    
# Set weights to make the content expand and center
for i in range(11):
    root.columnconfigure(i, weight=1)
  
# Create a label widget
topic = tk.Label(root, text="Mode 1: Point Mode", font=("Kanit", 30, "bold"))
topic.grid(row=1, column=5, sticky='nsew', pady=50)
subtopic2 = tk.Label(root, text="Setting coordinates for the Delta Robot to move to a specific point.", font=("Kanit", 18))
subtopic2.grid(row=2, column=1, columnspan=9, pady=10, sticky="nsew")

def create_input_grid():
    label1 = tk.Label(root, text="X:", font=("Kanit", 14, "bold"))
    label1.grid(row=4, column=4, padx=1, pady=20)

    entry1 = tk.Entry(root, validate="key", validatecommand=(root.register(validate_input), '%P'))
    entry1.grid(row=4, column=5, padx=1, pady=20)

    label2 = tk.Label(root, text="Y:", font=("Kanit", 14, "bold"))
    label2.grid(row=5, column=4, padx=1, pady=20)

    entry2 = tk.Entry(root, validate="key", validatecommand=(root.register(validate_input), '%P'))
    entry2.grid(row=5, column=5, padx=1, pady=20)

    label3 = tk.Label(root, text="Z:", font=("Kanit", 14, "bold"))
    label3.grid(row=6, column=4, padx=1, pady=20)

    entry3 = tk.Entry(root, validate="key", validatecommand=(root.register(validate_input), '%P'))
    entry3.grid(row=6, column=5, padx=1, pady=20)
    return entry1, entry2, entry3

fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d')

result = delta_point_mode(0, 0, 0, ax, trajectory, angles, last_traj, last_angles, current_pose, count)
trajectory = result[0]
angles = result[1]
last_traj = result[2]
last_angles = result[3]
current_pose = result[4]
count = result[5]

def inputParam():
    global state, trajectory, angles, last_traj, last_angles, current_pose, count

    target_x = entry1.get()
    target_y = entry2.get()
    target_z = entry3.get()
       
    if validate_input(target_x) and validate_input(target_y) and validate_input(target_z):
        if count == 1:
            result = delta_point_mode(float(target_x), float(target_y), float(target_z), ax, trajectory, angles, last_traj, last_angles, current_pose, count)
            trajectory = result[0]
            angles = result[1]
            last_traj = result[2]
            last_angles = result[3]
            current_pose = result[4]
            count = result[5]
        else:
            result = delta_point_mode(float(target_x), float(target_y), float(target_z), ax, trajectory, angles, last_traj, last_angles, current_pose, count)          
            trajectory = result[0]
            angles = result[1]
            last_traj = result[2]
            last_angles = result[3]
            current_pose = result[4]
            count = result[5]
    
# Buttons
# Create a button with a command
simbutton = tk.Button(root, text="Simulate", font=("Kanit", 14, "bold"), command=inputParam)
simbutton.grid(row=8, column=5, padx=5, pady=20)

# Create a button with a command
backbutton = tk.Button(root, text="Back", font=("Kanit", 14, "bold"), command=mainPage)
backbutton.grid(row=9, column=5, padx=5, pady=10)

# Run the Tkinter event loop
entry1, entry2, entry3 = create_input_grid()
root.mainloop()
