from moviepy.editor import *
import os
import cv2
import argparse

cwd = os.getcwd()
join_dir = lambda *args: os.path.join(*args)

# files = [join_dir(cwd,'z_angle', f'z_rot_{i}.png') for i in range(272)]


desc = "Makes the mp4 video of the plots"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-f', '--dirname', type=str,
                    help='specify the directory of your plots ')

total_plots=0
args = parser.parse_args()
if args.dirname == None:
    exit()
else:
    total_plots = len(os.listdir(join_dir(cwd, args.dirname)))

files = [join_dir(cwd,args.dirname, f'{args.dirname}_{i}.png') for i in range(total_plots)]
clip = ImageSequenceClip(files, fps = 4)
clip.write_videofile(f'{args.dirname}.mp4', fps = 24)
