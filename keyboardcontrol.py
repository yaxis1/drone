from djitellopy import tello 
import key_board_module as kp 
from time import sleep 

#initializing keyboardmodule and drone 
kp.init() 
drone = tello.Tello() 
drone.connect()
print(drone.get_battery())

drone.takeoff() 

while True: 
    drone.send_rc_control(0,0,0,0)