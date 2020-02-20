from sense_hat import SenseHat
from time import sleep
from random import choice
sense = SenseHat()

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
