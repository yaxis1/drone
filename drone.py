from djitellopy import tello
from time import sleep

#Warmup
drone = tello.Tello() 
drone.connect()
print(drone.get_battery())

#Take off
drone.takeoff()

#left-right,forward-backword,up-down,yaw
drone.send_rc_control(0,50,0,0)
sleep(2)
drone.send_rc_control(30,50,0,0)
sleep(2)

#Stop and land 
drone.send_rc_control(0,0,0,0)
drone.land()

