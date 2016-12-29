import Flask
import pigpio


R = 1
G = 2
B = 3

pi = pigpio.pi()
b = 255
pi.set_PWM_dutycycle(R, 100*(b/255))
