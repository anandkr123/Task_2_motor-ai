import pickle
import math
import matplotlib.pyplot as plt
import os
import argparse
import transforms3d
import numpy as np

cwd = os.getcwd()
join_dir = lambda *args: os.path.join(*args)


def check_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


# Reading the object file
def read_file(filename):
    with open(filename, 'rb') as f13:
        f_dict = pickle.load(f13)
    return f_dict

# Plots the ego headings
def plot_point_ego(point_1, point_2, i, length=0.000004):
    '''
    point_1, point_2 - Tuple (x, y)
    length - length of the arrow line you want to plot
    length - Length of the line you want to plot.
    '''

    # unpack the first point
    x_1, y_1 = point_1
    x_2, y_2 = point_2

    rad = math.atan((y_2-y_1)/(x_2-x_1))
    angle = math.degrees(rad)

    # find the end point
    dy = length * math.sin(math.radians(angle))
    dx = length * math.cos(math.radians(angle))

    plt.title(graph_name+'_ego_heading')
    # plot the points

    plt.xlim(min(ego_long), max(ego_long) + 0.0001)
    plt.ylim(min(ego_lat), max(ego_lat)+ 0.0001)

    # direction of arrow from one point to another point
    plt.arrow(x_1, y_1, dx, dy, head_width=0.00001, width=0.000001)
    check_dir(graph_name+'_ego_heading')
    plt.savefig(join_dir(cwd,graph_name+'_ego_heading',f'{graph_name}_ego_heading_{i}.png'), dpi=200)


def plot_point_detected_obj(point_1, angle, i, length=0.2):
    '''
    point - Tuple (x, y)
    angle - Angle you want your end point at in degrees.
    length - Length of the line you want to plot.
    '''

    # unpack the first point
    x_1, y_1 = point_1

    # find the end point
    dy = length * math.sin(math.radians(angle))
    dx = length * math.cos(math.radians(angle))

    # plot the points
    plt.xlim(-10, 60)
    plt.ylim(min(obj_y)-1, max(obj_y))

    # The detected object is heading opposite
    plt.title(graph_name+"_z_angle_heading")

    # direction of arrow from one point to another point
    plt.arrow(x_1+dx, y_1+dy, -dx, -dy,  head_width=0.1,width =0.1)
    check_dir(graph_name + '_z_heading')
    plt.savefig(join_dir(cwd, graph_name+"_z_heading",f'{graph_name}_z_heading_{i}.png') , dpi=200)


desc = "Plots of ego and objects heading"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-f', '--filename', type=str,
                    help='specify log file name in the current directory ')


args = parser.parse_args()
if args.filename == None:
    exit()


loaded_object =read_file(args.filename)

# get the ego and detected object logs
ego_logs = loaded_object['ego_logs']
detected_object_logs = loaded_object['detected_object_logs']

graph_name=(args.filename).split('.')[0]

ego_lat=[]
ego_long=[]
obj_y=[]
obj_x=[]

# list of ego coordinates
for e in ego_logs:
    ego_lat.append(e['latitude'])
    ego_long.append(e['longitude'])

# list of detected object coordinates
for e in detected_object_logs:
    obj_y.append(e['y'])
    obj_x.append((e['x']))


# plt.ion()
fig = plt.figure()
plt.xlabel("Longitude")
plt.ylabel("Latitude")
ax = fig.add_subplot()

# plot of ego headings
for i in range((len(ego_logs))-1):
    point_1 = (ego_long[i], ego_lat[i])
    point_2 = (ego_long[i+1], ego_lat[i+1])
    plot_point_ego(point_1, point_2, i)


# computation of the angles from quaternions of the detected object
angles_in_degree =[]
for i in range(len(detected_object_logs)):
    first_pose = detected_object_logs[i]
    quaternion_traj_list = [first_pose['theta_w'], first_pose['theta_x'], first_pose['theta_y'], first_pose['theta_z']]
    angles_traj_list = transforms3d.euler.quat2euler(quaternion_traj_list, axes='sxyz')
    rot_traj_list = [0, 0, np.rad2deg(angles_traj_list[-1])]
    angles_in_degree.append(rot_traj_list[-1])


# Create the figure
fig = plt.figure()
plt.xlabel("X")
plt.ylabel("Y")
ax = fig.add_subplot()

# Get the x,y coordinates of the detected object
for i in range((len(detected_object_logs))):
    point_1 = obj_x[i], obj_y[i]
    plot_point_detected_obj(point_1, angles_in_degree[i],i)


















