#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import subprocess
from subprocess import PIPE
import time 
from std_msgs.msg import String
import os

on = ["sudo", "python3", "ledtapeON.py"]
off= ["sudo", "python3", "ledtapeOFF.py"]

led_script_path = "../catkin_ws/src/rpi_led_tape/script"

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    p_out = int(data.data)
    #path = os.getcwd()
    #print(path)

    if p_out == 1:
        proc_h = subprocess.Popen(on, cwd=led_script_path)
        print("on")
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
