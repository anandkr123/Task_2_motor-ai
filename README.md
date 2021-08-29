# Task_2_motor-ai
Motor-AI Task 2

Ego and detected object plots and heading visulaization from the log files


## ego_and_object_plot.py

pass the log filename in the current directory through terminal to generate the ego and object plot
e.g.  python ego_and_object_plot.py --filename 0084_41_object.obj

## ego_and_obj_heading.py 

pass the log filename in the current directory through terminal to generate the headings of the ego and the detecetd objects.
Saves the plot at every timestamp in a seperate directory.

e.g.  python ego_and_obj_heading.py --filename 0084_41_object.obj

## make_video.py
Generates the mp4 video of the timestamp plots, given the directory name

e.g.  python make_video.py --dirname 0084_41_object_z_heading
