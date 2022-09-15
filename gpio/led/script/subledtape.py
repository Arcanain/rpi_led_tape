#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# led subledtape

import rospy
import pigpio
from rpi_ws281x import Color, PixelStrip

from std_msgs.msg import String


LED_COUNT = 18  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0
LED_STATE_OFF = Color(0, 0, 0)  # OFF
#

class Ws281x:
    def __init__(self):
        self.__strip = PixelStrip(
            LED_COUNT,
            LED_PIN,
            LED_FREQ_HZ,
            LED_DMA,
            LED_INVERT,
            LED_BRIGHTNESS,
            LED_CHANNEL,
        )
        self.__strip.begin()

    def on(self, red: int, green: int, blue: int) -> None:
        color = Color(red, green, blue)
        for i in range(self.__strip.numPixels()):
            self.__strip.setPixelColor(i, color)
            self.__strip.show()

    def off(self) -> None:
        for i in range(self.__strip.numPixels()):
            self.__strip.setPixelColor(i, LED_STATE_OFF)
            self.__strip.show()

led = Ws281x()

GPIO_PIN = 27

pi = pigpio.pi()
pi.set_mode(GPIO_PIN, pigpio.OUTPUT)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    p_out = int(data.data)
    pi.write(GPIO_PIN, p_out)
    
    if p_out == 1:
    	led.on(100,0,0)
    else:
    	led.on(0,100,0)	
    	

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback) # topic name and kata should be same 
    rospy.spin()

if __name__ == '__main__':
    listener()
