#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# gpio_test sub.py

import rospy
# import pigpio
import subprocess
import time 
from std_msgs.msg import String

# GPIO_PIN = 27

pi = pigpio.pi()
pi.set_mode(GPIO_PIN, pigpio.OUTPUT)

#debug 
#hello = ["sudo","python3","hello.py"]
#bye= ["sudo","python3","bye.py"]


on = ["sudo", "python3", "ledtapeON.py"]
off= ["sudo", "python3", "ledtapeOFF.py"]

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    p_out = int(data.data)
    # pi.write(GPIO_PIN, p_out)
    if p_out == 1:
        proc_h = subprocess.Popen(on)
        print("on")
        time.sleep(1)
    else:
        #subprocess.call("sudo","python3","bye.py")
        proc_b = subprocess.Popen(off)
        print("off")
        time.sleep(1)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
