import numpy as np
import matplotlib.pyplot as plt
import pickle

CASSIE_QUATERNION_SLICE = slice(0, 4)
CASSIE_POSITION_SLICE = slice(4, 23)
CASSIE_OMEGA_SLICE = slice(23, 26)
CASSIE_VELOCITY_SLICE = slice(26, 45)
CASSIE_JOINT_POSITION_SLICE = slice(7, 23)
CASSIE_JOINT_VELOCITY_SLICE = slice(29, 45)
CASSIE_FB_POSITION_SLICE = slice(4, 7)
CASSIE_FB_VELOCITY_SLICE = slice(26, 29)

CASSIE_NX = 45
CASSIE_NQ = 23
CASSIE_NV = 22
CASSIE_NU = 10

CASSIE_DTS = 100  # 2000Hz * 0.05s
DATASET_DIR = ''

class CassieHardwareTraj():

    def __init__(self, dataset_num):
        '''
            Shape of member variables
            t        : (CASSIE_DTS,)
            x_samples: (CASSIE_DTS, CASSIE_NX)
            u_samples: (CASSIE_DTS, CASSIE_NU)
        '''

        self.dataset_num = dataset_num
        self.t = np.load(DATASET_DIR + 't_' + dataset_num + '.npy')
        self.x_samples = np.load(DATASET_DIR + 'x_' + dataset_num + '.npy')
        self.u_samples = np.load(DATASET_DIR + 'u_' + dataset_num + '.npy')
        self.x_legend = pickle.load(open('state_legend', "rb"))
        self.u_legend = pickle.load(open('actuator_legend', "rb"))

    def time_to_index(self, t):
        if int(t * 2000) >= self.u_samples.shape[0]:
            print("time %.2f is out of bounds" % t)
        return int(t * 2000)

    def get_positions(self):
        return self.x_samples[:, CASSIE_POSITION_SLICE]

    def get_orientations(self):
        return self.x_samples[:, CASSIE_QUATERNION_SLICE]

    def get_velocities(self):
        return self.x_samples[:, CASSIE_VELOCITY_SLICE]

    def get_omegas(self):
        return self.x_samples[:, CASSIE_OMEGA_SLICE]

    def get_initial_state(self):
        initial_state = np.copy(self.x_samples[0, :])
        return initial_state

    def get_action(self, t):
        return self.u_samples[self.time_to_index(t), :]

    def plot_joint_positions(self):
        plt.plot(self.t, self.x_samples[:, CASSIE_JOINT_POSITION_SLICE])
        plt.legend(self.x_legend[CASSIE_JOINT_POSITION_SLICE])

    def plot_floating_base_positions(self):
        plt.plot(self.t, self.x_samples[:, CASSIE_FB_POSITION_SLICE])
        plt.legend(self.x_legend[CASSIE_FB_POSITION_SLICE])

    def plot_floating_base_quaternion(self):
        plt.plot(self.t, self.x_samples[:, CASSIE_QUATERNION_SLICE])
        plt.legend(self.x_legend[CASSIE_QUATERNION_SLICE])

    def plot_joint_velocities(self):
        plt.plot(self.t, self.x_samples[:, CASSIE_JOINT_VELOCITY_SLICE])
        plt.legend(self.x_legend[CASSIE_JOINT_VELOCITY_SLICE])

    def plot_floating_base_linear_velocities(self):
        plt.plot(self.t, self.x_samples[:, CASSIE_FB_VELOCITY_SLICE])
        plt.legend(self.x_legend[CASSIE_FB_VELOCITY_SLICE])

    def plot_floating_base_angular_velocities(self):
        plt.plot(self.t, self.x_samples[:, CASSIE_OMEGA_SLICE])
        plt.legend(self.x_legend[CASSIE_OMEGA_SLICE])

    def plot_efforts(self):
        plt.plot(self.t, self.u_samples)
        plt.legend(self.u_legend)