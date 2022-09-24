# note
Before using ws281x library 
install pip3 and install ws281x library from pip3

1. `sudo apt install pip3`
2. `sudo pip3 install ws281x`

# Procedure
```
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
roslaunch rpi_led_tape ledtape_control.launch
```
# reference 

## rpi_led_tape
led tape

ws2812について
1. https://www.marutsu.co.jp/pc/static/large_order/WS2812B_0124
2. https://mag.switch-science.com/2015/02/04/ws2822s/

led tape のラズパイで制御方法
1. https://dev.classmethod.jp/articles/raspberry-pi-tape-led-ws2815/
2. https://www.youtube.com/watch?v=BZDwrxX8YEU


## ros raspberry pi led blink
1. https://kanpapa.com/today/2022/05/ros-pub-sub-pigpio-blink-led.html

## subprocess の参考文献

1. https://stackoverflow.com/questions/52721537/opens-a-process-with-popen-cant-close-it-need-to-run-ros-command-in-cmd
2. https://myenigma.hatenablog.com/entry/20110326/1301150990
3. https://myenigma.hatenablog.com/entry/20110325/1301057472
