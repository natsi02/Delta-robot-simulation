import numpy as np
import matplotlib.pyplot as plt
import time

def plot_position(ax, r, t, param):
    # Coordinates
    x, y, z = r
    t1, t2, t3 = t
    # Rod lengths in m
    r_f, r_e = param[0], param[1]
    # Triangular side lengths in m
    f, e = param[2], param[3]

    l = f + 2 * r_f  # to adjust the view

    # Update the plot in the provided axes
    ax.clear()
    ax.set_xlim([-l, l])
    ax.set_ylim([-l, l])
    ax.set_zlim([-l * 2, l / 2])

    # Plot robot f plate
    p_f1 = np.array([f / 2, -f / (2 * np.sqrt(3)), 0])
    p_f2 = np.array([0, f / np.cos(30 * np.pi / 180) / 2, 0])
    p_f3 = np.array([-f / 2, -f / (2 * np.sqrt(3)), 0])

    ax.plot([p_f1[0], p_f2[0]], [p_f1[1], p_f2[1]], [p_f1[2], p_f2[2]], 'r-')
    ax.plot([p_f2[0], p_f3[0]], [p_f2[1], p_f3[1]], [p_f2[2], p_f3[2]], 'r-')
    ax.plot([p_f3[0], p_f1[0]], [p_f3[1], p_f1[1]], [p_f3[2], p_f1[2]], 'r-')

    # Plot robot e plate
    p_e1 = r + np.array([e / 2, -e / (2 * np.sqrt(3)), 0])
    p_e2 = r + np.array([0, e / np.cos(30 * np.pi / 180) / 2, 0])
    p_e3 = r + np.array([-e / 2, -e / (2 * np.sqrt(3)), 0])

    ax.plot([p_e1[0], p_e2[0]], [p_e1[1], p_e2[1]], [p_e1[2], p_e2[2]], 'b-')
    ax.plot([p_e2[0], p_e3[0]], [p_e2[1], p_e3[1]], [p_e2[2], p_e3[2]], 'b-')
    ax.plot([p_e3[0], p_e1[0]], [p_e3[1], p_e1[1]], [p_e3[2], p_e1[2]], 'b-')
    
    # Plot end effector position
    ax.scatter(x, y, z, c='g', marker='o')

    # Plot joints f
    p_f1 = np.array([0, -f / (2 * np.sqrt(3)), 0])
    R = np.array([[np.cos(120 * np.pi / 180), -np.sin(120 * np.pi / 180), 0],
                  [np.sin(120 * np.pi / 180), np.cos(120 * np.pi / 180), 0],
                  [0, 0, 1]])

    p_f2 = np.dot(R, p_f1)
    p_f3 = np.dot(R, p_f2)

    ax.scatter(p_f1[0], p_f1[1], p_f1[2], c='g', marker='o')
    ax.scatter(p_f2[0], p_f2[1], p_f2[2], c='g', marker='o')
    ax.scatter(p_f3[0], p_f3[1], p_f3[2], c='g', marker='o')

    # Plot joint positions f
    p_j1 = np.array([0, -f / (2 * np.sqrt(3)) - r_f * np.cos(t1), -r_f * np.sin(t1)])
    p_j2 = np.dot(R, np.array([0, -f / (2 * np.sqrt(3)) - r_f * np.cos(t2), -r_f * np.sin(t2)]))
    R = np.array([[np.cos(-120 * np.pi / 180), -np.sin(-120 * np.pi / 180), 0],
                  [np.sin(-120 * np.pi / 180), np.cos(-120 * np.pi / 180), 0],
                  [0, 0, 1]])
    p_j3 = np.dot(R, np.array([0, -f / (2 * np.sqrt(3)) - r_f * np.cos(t3), -r_f * np.sin(t3)]))

    ax.plot([p_f1[0], p_j1[0]], [p_f1[1], p_j1[1]], [p_f1[2], p_j1[2]], 'g-')
    ax.plot([p_f2[0], p_j2[0]], [p_f2[1], p_j2[1]], [p_f2[2], p_j2[2]], 'g-')
    ax.plot([p_f3[0], p_j3[0]], [p_f3[1], p_j3[1]], [p_f3[2], p_j3[2]], 'g-')

    # Plot joint positions
    ax.scatter(p_j1[0], p_j1[1], p_j1[2], c='g', marker='o')
    ax.scatter(p_j2[0], p_j2[1], p_j2[2], c='g', marker='o')
    ax.scatter(p_j3[0], p_j3[1], p_j3[2], c='g', marker='o')

    # Plot joint positions e
    transl = np.array([0, -e / (2 * np.sqrt(3)), 0])
    p_e1 = transl + np.array([x, y, z])
    R = np.array([[np.cos(120 * np.pi / 180), -np.sin(120 * np.pi / 180), 0],
                  [np.sin(120 * np.pi / 180), np.cos(120 * np.pi / 180), 0],
                  [0, 0, 1]])
    p_e2 = np.dot(R, transl) + r
    R = np.array([[np.cos(-120 * np.pi / 180), -np.sin(-120 * np.pi / 180), 0],
                  [np.sin(-120 * np.pi / 180), np.cos(-120 * np.pi / 180), 0],
                  [0, 0, 1]])
    p_e3 = np.dot(R, transl) + r

    ax.plot([p_j1[0], p_e1[0]], [p_j1[1], p_e1[1]], [p_j1[2], p_e1[2]], 'r-')
    ax.plot([p_j2[0], p_e2[0]], [p_j2[1], p_e2[1]], [p_j2[2], p_e2[2]], 'r-')
    ax.plot([p_j3[0], p_e3[0]], [p_j3[1], p_e3[1]], [p_j3[2], p_e3[2]], 'r-')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


def animation(ax, angles, traj, param):
    # Simulation step size
    dt = 0.1

    for i in range(angles.shape[1]):
        start_time = time.time()
        plot_position(ax, traj[:, i], angles[:, i], param)
        plt.pause(dt)
        elapsed_time = time.time() - start_time

        # Adjust pause duration to maintain the specified time step
        if elapsed_time < dt:
            time.sleep(dt - elapsed_time)