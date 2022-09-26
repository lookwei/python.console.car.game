#########################################
# A mini console game engine
# Built with Pyhton for COMP 1012
# By Xiaoyong Wei (x1wei@polyu.edu.hk)
#########################################


# create a background of 51-by-20 characters
background=[[32 for i in range(51)] for j in range(20)]
# creat a curb of 3-by-20 characters
curb=[]
for i in range(10):
    curb.append([ord('|'),ord('*'),ord('|')])
    curb.append([ord('|'),ord(' '),ord('|')])

# define a funtion to put an object into the background
# x, y are the corrdinates of the top-lef corner of the object
def put_object(bg, x, y, object):
    bg_width,bg_height=len(bg[0]),len(bg)
    wid_obj,hei_obj=len(object[0]),len(object)
    for r in range(hei_obj):
        for c in range(wid_obj):
            tag_x,tag_y=x+c,y+r
            if object[r][c]==' ' or tag_x>=bg_width or tag_y>=bg_height: continue
            bg[tag_y][tag_x]=object[r][c]
    return bg

# print a scene
def print_scene(background):
    for row in background:
        row_str="".join([chr(d) for d in row])
        print(row_str)

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
# a function to clean the printed content on screen
def clean_screen():
    for idx in range(20):
        print(LINE_UP, end=LINE_CLEAR)

start_logo_code=[[32, 32, 32, 95, 95, 95, 95, 95, 95, 95, 32, 32, 32, 32, 95, 95, 95, 95, 95, 95, 32, 32, 32, 32, 95, 95, 95, 32, 32, 32, 32, 32, 32, 32, 95, 95, 95, 32, 32, 95, 95, 95, 32], [32, 
32, 124, 32, 32, 32, 95, 95, 32, 34, 92, 32, 32, 47, 32, 32, 32, 32, 34, 32, 92, 32, 32, 124, 34, 32, 32, 124, 32, 32, 32, 32, 32, 124, 34, 32, 32, 92, 47, 34, 32, 32, 124], [32, 32, 40, 46, 32, 124, 95, 95, 41, 32, 58, 41, 47, 47, 32, 95, 
95, 95, 95, 32, 32, 92, 32, 124, 124, 32, 32, 124, 32, 32, 32, 32, 32, 32, 92, 32, 32, 32, 92, 32, 32, 47, 32], [32, 32, 124, 58, 32, 32, 95, 95, 95, 95, 47, 47, 32, 32, 47, 32, 32, 32, 32, 41, 32, 58, 41, 124, 58, 32, 32, 124, 32, 32, 32, 
32, 32, 32, 32, 92, 32, 32, 92, 47, 32, 32, 32], [32, 32, 40, 124, 32, 32, 47, 32, 32, 32, 40, 58, 32, 40, 95, 95, 95, 95, 47, 32, 47, 47, 32, 32, 92, 32, 32, 124, 95, 95, 95, 32, 
32, 32, 32, 47, 32, 32, 32, 47, 32, 32, 32], [32, 47, 124, 95, 95, 47, 32, 92, 32, 32, 32, 92, 32, 32, 32, 32, 32, 32, 32, 32, 47, 32, 32, 40, 32, 92, 95, 124, 58, 32, 32, 92, 32, 
32, 47, 32, 32, 32, 47, 32, 32, 32, 32], [40, 95, 95, 95, 95, 95, 95, 95, 41, 32, 32, 92, 34, 95, 95, 95, 95, 95, 47, 32, 32, 32, 32, 92, 95, 95, 95, 95, 95, 95, 95, 41, 124, 95, 95, 95, 47, 32, 32, 32, 32, 32, 32], [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32], [32, 32, 95, 95, 95, 95, 95, 95, 32, 32, 32, 32, 32, 32, 32, 32, 95, 95, 32, 32, 32, 32, 32, 32, 32, 32, 95, 95, 95, 95, 95, 95, 95, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32], [32, 47, 34, 32, 95, 32, 32, 34, 92, 32, 32, 32, 32, 32, 32, 47, 34, 34, 92, 32, 32, 32, 32, 32, 32, 47, 34, 32, 32, 32, 32, 32, 32, 92, 32, 32, 32, 32, 32, 32, 32, 32, 32], [40, 58, 32, 40, 32, 92, 95, 95, 95, 41, 32, 32, 32, 32, 47, 32, 32, 32, 32, 92, 32, 32, 32, 32, 124, 
58, 32, 32, 32, 32, 32, 32, 32, 32, 124, 32, 32, 32, 32, 32, 32, 32, 32], [32, 92, 47, 32, 92, 32, 32, 32, 32, 32, 32, 32, 32, 47, 32, 47, 92, 32, 32, 92, 32, 32, 32, 124, 95, 95, 
95, 95, 95, 47, 32, 32, 32, 41, 32, 32, 32, 32, 32, 32, 32, 
32, 32], [32, 47, 47, 32, 32, 92, 32, 95, 32, 32, 32, 32, 47, 47, 32, 32, 95, 95, 32, 32, 92, 32, 32, 32, 47, 47, 32, 32, 32, 32, 32, 32, 47, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32], [40, 58, 32, 32, 32, 95, 41, 32, 92, 32, 32, 47, 32, 32, 
32, 47, 32, 32, 92, 32, 32, 92, 32, 124, 58, 32, 32, 95, 95, 32, 32, 32, 92, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32], [32, 92, 95, 95, 95, 95, 95, 95, 95, 41, 40, 95, 95, 95, 47, 32, 32, 32, 32, 92, 95, 95, 95, 41, 124, 95, 95, 124, 32, 32, 92, 95, 95, 95, 41, 32, 32, 32, 32, 32, 32, 32, 32], [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32], [32, 66, 121, 32, 88, 105, 97, 111, 121, 111, 110, 103, 32, 87, 101, 105, 32, 64, 32, 67, 79, 77, 80, 32, 49, 48, 49, 50, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32], [32, 83, 
69, 80, 32, 50, 52, 44, 32, 50, 48, 50, 50, 32, 32, 32, 32, 
32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 
32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]]

car_code=[[32, 32, 32, 32, 95, 95, 95, 95, 32, 32, 32, 32, 32, 
32], [32, 95, 95, 47, 32, 32, 124, 95, 92, 95, 32, 32, 32, 32], [124, 32, 32, 95, 32, 32, 32, 32, 32, 95, 96, 96, 45, 46], [39, 45, 40, 95, 41, 45, 45, 45, 40, 95, 41, 45, 45, 39], [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]]

dog1_code=[[32, 32, 46, 32, 32, 32, 32, 32, 32], [32, 46, 46, 94, 95, 95, 95, 95, 47], [96, 45, 46, 32, 95, 95, 95, 32, 41], [32, 32, 
124, 124, 32, 32, 124, 124, 32]]

dog2_code=[[32, 32, 32, 32, 32, 32, 32, 32, 95, 95, 32, 32], [32, 32, 32, 40, 95, 95, 95, 40, 41, 39, 96, 59], [32, 32, 32, 47, 44, 32, 32, 32, 32, 47, 96, 32], [32, 32, 32, 92, 34, 45, 45, 92, 32, 32, 32, 32]]

# decode an object into a character list
def decode_object(obj_code):
    pic=[]
    for row in obj_code:
        pic.append([chr(d) for d in row])
    return pic

import copy
# put the left curb into the scene
cur_bg=put_object(copy.deepcopy(background),0,0,curb)
# put the right curb into the scene
cur_bg=put_object(cur_bg,48,0,curb)
# print the updated scene
#print_scene(cur_bg)

# put logo into scene
scene_start=put_object(copy.deepcopy(cur_bg),4,1,start_logo_code)
# display the updated scene
print_scene(scene_start)

import time
# let the startup screen stay for 5 seconds
time.sleep(5) 

# clean the screen before printing new content
#clean_screen()

# # put the more object into a new scene
# new_scene=put_object(copy.deepcopy(cur_bg),5,3,car_code)
# new_scene=put_object(new_scene,15,8,dog1_code)
# new_scene=put_object(new_scene,18,15,dog2_code)
# # print the updated scene
# print_scene(new_scene)



car_pos=[15,4] #set the initial car position at y=15, x=4
car_speed=[0,1]

from pynput import keyboard
def on_press(key):
    global car_pos
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k=='right':
        car_pos=[car_pos[0],car_pos[1]+1]  
    elif k=='left': 
        car_pos=[car_pos[0],car_pos[1]-1]
        

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread

while True:
    # clean the screen before printing new content
    clean_screen()
    #car_pos=[car_pos[0]+car_speed[0],car_pos[1]+car_speed[1]]
    new_scene=put_object(copy.deepcopy(cur_bg),car_pos[1],car_pos[0],car_code)
    # print the updated scene
    print_scene(new_scene)
    time.sleep(0.1)



