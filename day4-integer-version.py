#########################################
# A mini console game engine
# Built with Pyhton for COMP 1012
# By Xiaoyong Wei (x1wei@polyu.edu.hk)
#########################################


scene_height,scene_width=20,80
# create a background of scene_height-by-scene_height characters
background=[[32 for i in range(scene_width)] for j in range(scene_height)]
# creat a curb of 3-by-scene_height characters
curb=[]
for i in range(int(scene_height/2)):
    curb.append([ord('|'),ord('*'),ord('|')])
    curb.append([ord('|'),ord(' '),ord('|')])

# define a funtion to put an object into the background
# x, y are the corrdinates of the top-lef corner of the object
def put_object(bg, x, y, object):
    bg_width,bg_height=len(bg[0]),len(bg)
    wid_obj,hei_obj=len(object[0]),len(object)
    crashed=False
    for r in range(hei_obj):
        for c in range(wid_obj):
            tag_x,tag_y=x+c,y+r
            if object[r][c]==32 or tag_x>=bg_width or tag_y>=bg_height: continue
            # in case the target scene position (ie., bg[tag_y][tag_x]) is 
            # with a non-space chacter, the car is hitting something (curb/dog)
            if not bg[tag_y][tag_x]==32:
                crashed=True
            bg[tag_y][tag_x]=object[r][c]
    return crashed,bg

# print a scene
def print_scene(background):
    for row in background:
        row_str="".join([chr(d) for d in row])
        print(row_str)

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
# a function to clean the printed content on screen
def clean_screen():
    for idx in range(scene_height):
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


crashedcode=[[32, 32, 32, 95, 95, 95, 32, 32, 32, 32, 32, 32, 32, 32, 
32, 32, 32, 32, 32, 32, 95, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 95, 32, 32, 32, 95, 32], [32, 32, 47, 32, 95, 95, 92, 32, 95, 95, 32, 95, 95, 32, 95, 32, 
95, 95, 95, 124, 32, 124, 95, 95, 32, 32, 32, 95, 95, 95, 
32, 32, 95, 95, 124, 32, 124, 32, 47, 32, 92], [32, 47, 32, 47, 32, 124, 32, 39, 95, 95, 47, 32, 95, 96, 32, 47, 32, 95, 95, 124, 32, 39, 95, 32, 92, 32, 47, 32, 95, 32, 92, 
47, 32, 95, 96, 32, 124, 47, 32, 32, 47], [47, 32, 47, 95, 95, 124, 32, 124, 32, 124, 32, 40, 95, 124, 32, 92, 95, 95, 32, 92, 32, 124, 32, 124, 32, 124, 32, 32, 95, 95, 47, 
32, 40, 95, 124, 32, 47, 92, 95, 47, 32], [92, 95, 95, 95, 95, 47, 95, 124, 32, 32, 92, 95, 95, 44, 95, 124, 95, 95, 95, 47, 95, 124, 32, 124, 95, 124, 92, 95, 95, 95, 124, 92, 95, 95, 44, 95, 92, 47, 32, 32, 32], [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]]

# decode an object into a character list
def decode_object(obj_code):
    pic=[]
    for row in obj_code:
        pic.append([chr(d) for d in row])
    return pic

import copy
# put the left curb into the scene
crashed,cur_bg=put_object(copy.deepcopy(background),0,0,curb)
# put the right curb into the scene
crashed,cur_bg=put_object(cur_bg,scene_width-3,0,curb)
# print the updated scene
#print_scene(cur_bg)

# put logo into scene
crashed,scene_start=put_object(copy.deepcopy(cur_bg),20,1,start_logo_code)
# display the updated scene
print_scene(scene_start)

import time
# let the startup screen stay for seconds
time.sleep(3) 

# clean the screen before printing new content
#clean_screen()

# # put the more object into a new scene
# new_scene=put_object(copy.deepcopy(cur_bg),5,3,car_code)
# new_scene=put_object(new_scene,15,8,dog1_code)
# new_scene=put_object(new_scene,18,15,dog2_code)
# # print the updated scene
# print_scene(new_scene)



car_pos=[15,6] #set the initial car position at y=15, x=6
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

import random
# a list of dog genres
dog_genres=[dog1_code, dog2_code]
# a list to record the dogs in the scene
# each dog is record with a genre and a position
list_dogs=[]
# max #dog can be put into the scene
max_num_dogs=1
# speed of dogs at y and x directions
dog_speed=[1,0]

def udpate_dogs(scene):
    global list_dogs, dog_speed
    dog2remove=[]
    for doginfo in list_dogs:
        # update position of each dog
        doginfo[1]=[doginfo[1][0]+dog_speed[0],doginfo[1][1]+dog_speed[1]]
        if doginfo[1][0]>scene_height: 
            # the dog runs out from the scene, remove it
            dog2remove.append(doginfo)
    for doginfo in dog2remove:
        list_dogs.remove(doginfo)
    if len(list_dogs)<max_num_dogs:
        # generate a dog by chance (a probability of 30%)
        if random.randint(0,100)<30:
            dog_gen=dog_genres[random.randint(0,1)]
            hei_dog,wid_dog=len(dog_gen),len(dog_gen[0])
            pos_init=[0,random.randint(4,scene_width-3-wid_dog-1)]
            list_dogs.append([dog_gen,pos_init])
    for doginfo in list_dogs:
        crashed,scene=put_object(scene,doginfo[1][1],doginfo[1][0],doginfo[0])
    return scene

def reset_game():
    global list_dogs,car_pos
    list_dogs=[]
    car_pos=[15,6]
    
while True:
    # clean the screen before printing new content
    clean_screen()
    # udpate dogs
    new_scene=udpate_dogs(copy.deepcopy(cur_bg))
    # put car into the scene
    crashed,new_scene=put_object(new_scene,car_pos[1],car_pos[0],car_code)
    # check if crashed
    if crashed:
       crashed,new_scene=put_object(new_scene,20,3,crashedcode)
       print_scene(new_scene)
       time.sleep(2)
       reset_game()
       continue
    # print the updated scene
    print_scene(new_scene)
    time.sleep(0.2)

print("**************** Game Over! ****************")

