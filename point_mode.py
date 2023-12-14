import numpy as np
import matplotlib.pyplot as plt
from robot_computation import calc_trajectory, calc_trajectory_angles
from plotting_simulation import animation

def delta_point_mode(target_x, target_y, target_z, ax, trajectory, angles, last_traj, last_angles, current, count):
    
    # Parameters
    r_f = 3e-2  # Length of upper joint in m
    r_e = 8e-2  # Length of lower joint
    f = 3.7e-2    # Side of Fixed triangle
    e = 2.6e-3    # Side of End effector triangle

    # Define param to keep all of parameters
    param = [r_f, r_e, f, e]

    # Trajectory
    m = 10  # number of trajectory points

    # Define current_pose as empty array
    current_pose = np.zeros(3)

    if (count == 0):
        
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
        count = count + 1
        return trajectory, angles, last_traj, last_angles, current_pose, count
    else:
        # Update current pose for the next iteration
        current_pose = current
    
    print("Point mode control")

    # Update the target position
    r_goal = np.array([target_x, target_y, target_z])

    # Calculate trajectory and angles
    trajectory[:, :, 0] = calc_trajectory(current_pose, r_goal, m)
    angles[:, :, 0], s = calc_trajectory_angles(trajectory[:, :, 0], param)
    angles[:, :, 0] *= np.pi / 180

    # Check if have singularity will return immediately
    if s == 1:
        trajectory[:, :, 0] = last_traj[:, :, 0]
        angles[:, :, 0] = last_angles[:, :, 0]
        return trajectory, angles, last_traj, last_angles, current_pose, count
            
    # Update last_traj and last_angles for singularity check
    last_traj[:, :, 0] = trajectory[:, :, 0]
    last_angles[:, :, 0] = angles[:, :, 0]

    # Update current pose for the next iteration
    current_pose = r_goal

    # Proceed with animation without checking for singularity
    animation(ax, angles[:, :, 0], trajectory[:, :, 0], param)
    print(f"Goal {count} reached.")
    
    # Count
    count = count + 1
    
    return trajectory, angles, last_traj, last_angles, current_pose, count

plt.show()
