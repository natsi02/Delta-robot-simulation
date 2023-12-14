import numpy as np
from plotting_simulation import plot_position, animation
from tkinter import messagebox
import sys
def calc_trajectory(r0, r_goal, m):
    traj = np.array([np.linspace(r0[0], r_goal[0], m),
                     np.linspace(r0[1], r_goal[1], m),
                     np.linspace(r0[2], r_goal[2], m)])
    return traj

def calc_trajectory_angles(traj, param):
    m = traj.shape[1]
    angles = np.zeros((3, m))

    for i in range(m):
        angles[:, i], s = inverse_kinematics([traj[0, i], traj[1, i], traj[2, i]], param)
    print(f"angles : {angles}")
    return angles, s

last_theta = [0, 0, 0]

def inverse_kinematics(r, param):
    global last_theta
    x, y, z = r
    t1 = 0
    t2 = 0
    t3 = 0

    t1, s = calc_inverse(r, param)

    t2, s = calc_inverse([x * np.cos(120 * np.pi / 180) + y * np.sin(120 * np.pi / 180),
                        y * np.cos(120 * np.pi / 180) - x * np.sin(120 * np.pi / 180), z], param)

    t3, s = calc_inverse([x * np.cos(120 * np.pi / 180) - y * np.sin(120 * np.pi / 180),
                        y * np.cos(120 * np.pi / 180) + x * np.sin(120 * np.pi / 180), z], param)

    if s == 0:
        t = [t1, t2, t3]
        last_theta = t
    else:
        t = last_theta
    
    return t, s

def calc_inverse(r, param):
    # Theta joint angles
    theta = [0, 0, 0]
    
    # End-effector pose
    x, y, z = r
    
    # Length of upper joint in m
    r_f = param[0]  
    
    # Length of lower joint in m
    r_e = param[1]  

    # Side of Base triangle
    f = param[2]  
    
    # Side of End effector triangle
    e = param[3]  

    # Range of base triangle in y-axis
    f1 = -f / (2 * np.sqrt(3))  # f1 = -(Side of base triangle) / (2*sqrt(3)) [ 2 * tan30 ]
    
    # Range of end effector triangle in y-axis
    k = e / (2 * np.sqrt(3))  # k = (Side of end effector triangle) / (2*sqrt(3)) [ 2 * tan30 ]
    
    # Pose position - Range of end effector triangle in y-axis
    y1 = y - k  # Shift
    
    # (End-effector pose)^2 + (Length of upper link)^2 - (Length of lower link)^2 - (Range of base triangle in y-axis)^2 / (2 * Pose position in Z-Axis)
    a = (x**2 + y1**2 + z**2 + r_f**2 - r_e**2 - f1**2) / (2 * z)
    
    # (Range of base triangle in y-axis - Pose position in y-axis (shifted)) / Pose position in Z-Axis
    b = (f1 - y1) / z
    
    # -(a + b * Range of base triangle in y-axis)^2 + Length of upper joint * (b^2 * Length of upper joint + Length of upper joint)
    d = -(a + b * f1)**2 + r_f * (b**2 * r_f + r_f) 

    if d < 0:
        print('Pose not in range! Choose another Pose that is not a singularity')       
        # Replace this with your actual message
        popup_message = "Singularity occurred! Simulation stopped."
        # Create a popup with information message
        messagebox.showinfo("Singularity Warning", popup_message)

        s = 1
        return
    else:
        yj = (y1 - a * b - np.sqrt(d)) / (b**2 + 1)  # choosing outer point
        zj = a + b * yj
        theta = 180 * np.arctan(-zj / (y1 - yj)) / np.pi

        if yj > y1:
            theta += 180
        if theta < (-46.1) or theta > 95.5:
            print('Pose not in range! Choose another Pose that is not a singularity')       
            # Replace this with your actual message
            popup_message = "Singularity occurred! Simulation stopped."
            # Create a popup with information message
            messagebox.showinfo("Singularity Warning", popup_message)
            s = 1
            return
        else:
            s = 0
        
    return theta, s