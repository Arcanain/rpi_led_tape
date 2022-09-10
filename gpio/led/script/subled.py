#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# gpio_test sub.py

import rospy
import pigpio
from std_msgs.msg import String

GPIO_PIN = 27

pi = pigpio.pi()
pi.set_mode(GPIO_PIN, pigpio.OUTPUT)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    p_out = int(data.data)
    pi.write(GPIO_PIN, p_out)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
