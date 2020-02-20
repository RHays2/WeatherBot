from sense_hat import SenseHat
from time import sleep
from random import choice
sense = SenseHat()

r = 75
g = 150
b = 130
blue = [0,0,255]
sense.clear((r,g,b))
#sense.show_message("Swag", 0.1, [r,g,b])
'''
sense.show_letter("G", blue)
sleep(0.5)
sense.show_letter("A", yellow)
sleep(0.5)
sense.show_letter("Y", red)
sleep(0.5)
sense.show_letter("S", green)

faces = ["Jack", "Queen", "King", "Ace"]
card = choice(faces)
sense.show_message(card)
'''

R = (255, 50, 19)
O = (255, 151, 28)
Y = (255, 213, 0)
G = (114, 203, 59)
B = (3, 65, 174)
P = (128, 0, 128)
N = (123, 200, 45)
W = (255, 255, 255)

sunny  = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, Y, Y, Y, Y, B, B,
    B, B, Y, Y, Y, Y, B, B,
    B, B, Y, Y, Y, Y, B, B,
    B, B, Y, Y, Y, Y, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B
]

sense.set_pixels(sunny)
'''
while True:
    sense.set_rotation(0)
    sleep(0.5)
    sense.set_rotation(90)
    sleep(0.5)
    sense.set_rotation(180)
    sleep(0.5)
    sense.set_rotation(270)
    sleep(0.5)


print "Pressure: ",sense.get_pressure()
print "Temperature: ", sense.get_temperature()
print "Humidity: ", sense.get_humidity()

o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw =o["yaw"]
print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))

red = (255, 0, 0)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        sense.show_letter("!", red)
    else:
        sense.clear()
'''        
