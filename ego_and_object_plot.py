import matplotlib.pyplot as plt
import pickle
import argparse
import os

cwd = os.getcwd()
join_dir = lambda *args: os.path.join(*args)



# Reading the object file
def read_file(filename):
    with open(filename, 'rb') as f13:
        f_dict = pickle.load(f13)
    return f_dict


desc = "Plot of ego and detected objects"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-f', '--filename', type=str,
                    help='specify log file name in the current directory ')

args = parser.parse_args()
if args.filename == None:
    exit()

loaded_object =read_file(args.filename)

ego_logs = loaded_object['ego_logs']
detected_object_logs = loaded_object['detected_object_logs']

ego_lat=[]
ego_long=[]
obj_y=[]
obj_x=[]

for e in ego_logs:
    ego_lat.append(e['latitude'])
    ego_long.append(e['longitude'])

for e in detected_object_logs:
    obj_y.append(e['y'])
    obj_x.append((e['x']))

graph_name=(args.filename).split('.')[0]

fig = plt.figure()
plt.xlabel("Longitude")
plt.ylabel("Latitude")
ax = fig.add_subplot()
plt.title(graph_name+'_ego')
plt.plot(ego_long,ego_lat)
plt.savefig(join_dir(cwd,graph_name+'_ego.png'))


fig = plt.figure()
plt.xlabel("X")
plt.ylabel("Y")
ax1 = fig.add_subplot()
plt.title(graph_name+'_object')
plt.plot(obj_x,obj_y)
plt.savefig(join_dir(cwd,graph_name+'_object.png'))

