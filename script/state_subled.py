#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import subprocess
from subprocess import PIPE
import time 
from std_msgs.msg import String
from std_msgs.msg import Int8
from geometry_msgs.msg import Twist
import os

red_on = ["sudo", "python3", "ledtapeRedON.py"]
green_on = ["sudo", "python3", "ledtapeGreenON.py"]
yellow_on = ["sudo", "python3", "ledtapeYellowON.py"]
off= ["sudo", "python3", "ledtapeOFF.py"]

led_script_path = "../catkin_ws/src/rpi_led_tape/script"

cmd_vel_joystick = Twist()
def cmd_vel_joystick_callback(data):
    cmd_vel_joystick.linear.x = data.linear.x
    cmd_vel_joystick.angular.z = data.angular.z

cmd_vel_keyboard = Twist()
def cmd_vel_keyboard_callback(data):
    cmd_vel_keyboard.linear.x = data.linear.x
    cmd_vel_keyboard.angular.z = data.angular.z

cmd_vel_automatic = Twist()
def cmd_vel_automatic_callback(data):
    cmd_vel_automatic.linear.x = data.linear.x
    cmd_vel_automatic.angular.z = data.angular.z

if __name__ == '__main__':
    rospy.init_node('state_led', anonymous=True)
    #rospy.Subscriber('state', String, state_callback)

    rospy.Subscriber('cmd_vel_joystick', Twist, cmd_vel_joystick_callback)
    rospy.Subscriber('cmd_vel_keyboard', Twist, cmd_vel_keyboard_callback)
    rospy.Subscriber('cmd_vel_automatic', Twist, cmd_vel_automatic_callback)

    #rospy.spin()

    r = rospy.Rate(10) # Hz
    while not rospy.is_shutdown():
        if cmd_vel_joystick.linear.x != 0 or cmd_vel_joystick.angular.z != 0:
            state_data = 1
        elif cmd_vel_keyboard.linear.x != 0 or cmd_vel_keyboard.angular.z != 0:
            state_data = 2
        elif cmd_vel_automatic.linear.x != 0 or cmd_vel_automatic.angular.z != 0:
            state_data = 3
        else:
            state_data = 4

        if state_data == 1:
            proc_h = subprocess.Popen(yellow_on, cwd=led_script_path)
            #print("yellow on")
            time.sleep(4)
        elif state_data == 2:
            proc_h = subprocess.Popen(yellow_on, cwd=led_script_path)
            #print("yellow on")
            time.sleep(4)
        elif state_data == 3:
            proc_h = subprocess.Popen(green_on, cwd=led_script_path)
            #print("green on")
            time.sleep(4)
        elif state_data == 4:
            proc_b = subprocess.Popen(off, cwd=led_script_path)
            #print("off")
            time.sleep(4)

        r.sleep()