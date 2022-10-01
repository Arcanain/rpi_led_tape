#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import subprocess
from subprocess import PIPE
import time 
from std_msgs.msg import String
from std_msgs.msg import Int8
import os

red_on = ["sudo", "python3", "ledtapeRedON.py"]
green_on = ["sudo", "python3", "ledtapeGreenON.py"]
yellow_on = ["sudo", "python3", "ledtapeYellowON.py"]
off= ["sudo", "python3", "ledtapeOFF.py"]

led_script_path = "../catkin_ws/src/rpi_led_tape/script"

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    p_out = int(data.data)
    #path = os.getcwd()
    #print(path)

    if p_out == 1:
        proc_h = subprocess.Popen(red_on, cwd=led_script_path)
        print("red on")
        time.sleep(1)
    elif p_out == 2:
        proc_h = subprocess.Popen(green_on, cwd=led_script_path)
        print("green on")
        time.sleep(1)
    elif p_out == 3:
        proc_h = subprocess.Popen(yellow_on, cwd=led_script_path)
        print("yellow on")
        time.sleep(1)
    else:
        proc_b = subprocess.Popen(off, cwd=led_script_path)
        print("off")
        time.sleep(1)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
