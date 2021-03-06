Jumping Dataset

Trajectories were collected over three days on Jan 27 2021, Feb 12 2021, and Feb 26 2021.
The trajectories include the floating base state (estimated using the contact-aided invariant EKF `Hartley 2019`), joint positions and velocities, and measured motor torques. 

The jumping controller is the impact invariant controller https://github.com/DAIRLab/dairlib/tree/master/examples/impact_invariant_control.
While the overall control architecture is the same across logs, gains were changed across the experiments.

The trajectories are stored in raw `.npy` files and can be loaded in as shown in the example script: `plot_state_trajectory.py`

The state indices are defined below, the description of the joint dofs are defined in the file `cassie_v2.urdf`.
The joint ordering is defined using the Drake (pre-Nov 16 2021) breadth-first convention when loading in the urdf.
There is not an encoder on either `ankle_spring_joint` on the physical robot Cassie. We estimate the joint position using inverse kinematics in our state estimator and include it in the trajectory data; however, we leave the velocity of those joints at 0.

|Joint Position Name| Joint Position Index|
|---|---|
|base_qw | 0|
|base_qx | 1|
|base_qy | 2|
|base_qz | 3|
|base_x | 4|
|base_y | 5|
|base_z | 6|
|hip_roll_left | 7|
|hip_roll_right | 8|
|hip_yaw_left | 9|
|hip_yaw_right | 10|
|hip_pitch_left | 11|
|hip_pitch_right | 12|
|knee_left | 13|
|knee_right | 14|
|knee_joint_left | 15|
|knee_joint_right | 16|
|ankle_joint_left | 17|
|ankle_joint_right | 18|
|ankle_spring_joint_left | 19|
|toe_left | 20|
|ankle_spring_joint_right | 21|
|toe_right | 22|

|Joint Velocity Name| Joint Velocity Index|
|---|---|
|base_wx| 23 + 0|
|base_wy| 23 + 1|
|base_wz| 23 + 2|
|base_vx| 23 + 3|
|base_vy| 23 + 4|
|base_vz| 23 + 5|
|hip_roll_leftdot| 23 + 6|
|hip_roll_rightdot| 23 + 7|
|hip_yaw_leftdot| 23 + 8|
|hip_yaw_rightdot| 23 + 9|
|hip_pitch_leftdot| 23 + 10|
|hip_pitch_rightdot| 23 + 11|
|knee_leftdot| 23 + 12|
|knee_rightdot| 23 + 13|
|knee_joint_leftdot| 23 + 14|
|knee_joint_rightdot| 23 + 15|
|ankle_joint_leftdot| 23 + 16|
|ankle_joint_rightdot| 23 + 17|
|ankle_spring_joint_leftdot| 23 + 18|
|ankle_spring_joint_rightdot| 23 + 20|
|toe_leftdot| 23 + 19|
|toe_rightdot| 23 + 21|

| Actuator Name | Actuator Index |
|---|---|
|hip_roll_left|0|
|hip_roll_right|1|
|hip_yaw_left|2|
|hip_yaw_right|3|
|hip_pitch_left|4|
|hip_pitch_right|5|
|knee_left|6|
|knee_right|7|
|toe_left|8|
|toe_right|9|
 