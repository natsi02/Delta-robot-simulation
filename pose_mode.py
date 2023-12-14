import numpy as np
import matplotlib.pyplot as plt
from robot_computation import calc_trajectory, calc_trajectory_angles
from plotting_simulation import animation

def delta_pose_mode(values,ax,flag):
    
    # Parameters
    r_f = 3e-2  # Length of upper joint in m
    r_e = 8e-2  # Length of lower joint
    f = 3.7e-2  # Side of Fixed triangle
    e = 2.6e-3  # Side of End effector triangle

    param = [r_f, r_e, f, e]

    # Trajectory
    m = 10  # number of trajectory points

    # Define variable
    trajectory = np.zeros((3, m, 1))
    last_traj = np.zeros((3, m, 1))
    angles = np.zeros((3, m, 1))
    last_angles = np.zeros((3, m, 1))

    if flag == 0:
        # Define starting position
        r0 = [0, 0, -0.1]  # start Pose
        current_pose = np.array(r0)
        r_goal = r0

        # Calculate trajectory and angles
        trajectory[:, :, 0] = calc_trajectory(current_pose, r_goal, m)
        angles[:, :, 0], s = calc_trajectory_angles(trajectory[:, :, 0], param)
        angles[:, :, 0] *= np.pi / 180

        # Update current pose for the next iteration
        current_pose = r_goal
        
        # Proceed animation
        animation(ax, angles[:, :, 0], trajectory[:, :, 0], param)
        return
    else :
        i = 0
        input_func = 0

        current_pose = np.array([0, 0, -0.1])  # Set the initial pose

        for target in values:
            # Calculate trajectory and angles
            trajectory[:, :, 0] = calc_trajectory(current_pose, target, m)
            angles[:, :, 0], s = calc_trajectory_angles(trajectory[:, :, 0], param)
            angles[:, :, 0] *= np.pi / 180

            # Update current pose for the next iteration
            current_pose = target

            # Proceed with animation without checking for singularity
            animation(ax, angles[:, :, 0], trajectory[:, :, 0], param)

            print("Goal reached.")
    return
# Show the plot for each iteration
plt.show()
