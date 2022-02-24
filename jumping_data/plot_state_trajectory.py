from cassie_hardware_trajectory import *

def main():
    dataset_num = '00'
    hardware_traj = CassieHardwareTraj(dataset_num)

    # Simple plotting options

    # hardware_traj.plot_joint_positions()
    # hardware_traj.plot_floating_base_positions()
    # hardware_traj.plot_floating_base_quaternion()
    # hardware_traj.plot_joint_velocities()
    # hardware_traj.plot_floating_base_linear_velocities()
    # hardware_traj.plot_floating_base_angular_velocities()
    # hardware_traj.plot_efforts()


    # import matplotlib; matplotlib.pyplot.show()

if __name__ == '__main__':
    main()