from sense_hat import SenseHat
from time import sleep
from random import choice
import pyowm
sense = SenseHat()

owm = pyowm.OWM('4dc989dc9fceac17d923773b08e23ec7')
observation = owm.weather_at_place()
observation = owm.weather_at_place('London,GB')
w = observation.get_weather()
print(w.get_status())
print(w) 

R = (255, 50, 19)
O = (255, 151, 28)
Y = (255, 213, 0)
G = (114, 203, 59)
B = (3, 65, 174)
P = (128, 0, 128)
N = (123, 200, 45)
W = (255, 255, 255)
GR = (128, 128, 128)

sunny  = [
    B, B, B, B, B, B, B, B,
    B, B, B, Y, Y, B, B, B,
    B, B, Y, Y, Y, Y, B, B,
    B, Y, Y, Y, Y, Y, Y, B,
    B, Y, Y, Y, Y, Y, Y, B,
    B, B, Y, Y, Y, Y, B, B,
    B, B, B, Y, Y, B, B, B,
    B, B, B, B, B, B, B, B
]

cloudy  = [
    B, B, B, B, B, B, B, B,
    B, B, GR, GR, GR, GR, B, B,
    B, GR, GR, GR, GR, GR, GR, B,
    GR, GR, GR, GR, GR, GR, GR, GR,
    GR, GR, GR, GR, GR, GR, GR, GR,
    B, GR, GR, GR, GR, GR, GR, B,
    B, B, GR, GR, GR, GR, B, B,
    B, B, B, B, B, B, B, B
]

rainy = [
    GR, GR, GR, B, B, GR, GR, GR,
    GR, GR, B, B, B, B, GR, GR,
    GR, GR, B, B, B, B, GR, GR,
    GR, B, B, B, B, B, B, GR,
    GR, B, B, B, B, B, B, GR,
    GR, B, B, B, B, B, B, GR,
    GR, GR, B, B, B, B, GR, GR,
    GR, GR, GR, GR, GR, GR, GR, GR
]

snowy  = [
    W, B, B, W, W, B, B, W,
    B, W, B, W, W, B, W, B,
    B, B, W, W, W, W, B, B,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    B, B, W, W, W, W, B, B,
    B, W, B, W, W, B, W, B,
    W, B, B, W, W, B, B, W
]

#sense.set_pixels(sunny)
sense.set_pixels(snowy)
