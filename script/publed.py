#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)

    rate = rospy.Rate(1) # 1hz

    i = 0

    while not rospy.is_shutdown():
        msg = str(i)
        rospy.loginfo(msg)
        pub.publish(msg)

        rate.sleep()
        
        if i == 3:
            i = 0
        else:
            i = i + 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
