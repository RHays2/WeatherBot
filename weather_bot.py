from sense_hat import SenseHat
from time import sleep
from random import choice
import pyowm
sense = SenseHat()

R = (255, 50, 19)
O = (255, 151, 28)
Y = (255, 213, 0)
G = (114, 203, 59)
B = (3, 65, 174)
P = (128, 0, 128)
N = (123, 200, 45)
W = (255, 255, 255)
GR = (128, 128, 128)
BL = (0, 0, 0)

clear  = [
    B, B, B, B, B, B, B, B,
    B, B, B, Y, Y, B, B, B,
    B, B, Y, Y, Y, Y, B, B,
    B, Y, Y, Y, Y, Y, Y, B,
    B, Y, Y, Y, Y, Y, Y, B,
    B, B, Y, Y, Y, Y, B, B,
    B, B, B, Y, Y, B, B, B,
    B, B, B, B, B, B, B, B
]

clouds  = [
    B, B, B, B, B, B, B, B,
    B, B, GR, GR, GR, GR, B, B,
    B, GR, GR, GR, GR, GR, GR, B,
    GR, GR, GR, GR, GR, GR, GR, GR,
    GR, GR, GR, GR, GR, GR, GR, GR,
    B, GR, GR, GR, GR, GR, GR, B,
    B, B, GR, GR, GR, GR, B, B,
    B, B, B, B, B, B, B, B
]

rain = [
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

<<<<<<< HEAD
not_found  = [
    R, R, R, R, R, R, R, R,
    R, R, W, R, R, W, R, R,
    R, R, W, R, R, W, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, W, W, R, R, R,
    R, R, W, R, R, W, R, R,
    R, W, R, R, R, R, W, R,
    R, R, R, R, R, R, R, R,
]

owm = pyowm.OWM('4dc989dc9fceac17d923773b08e23ec7')
print("Enter a location: ")
location = input()
observation = owm.weather_at_place(location)
w = observation.get_weather()
temp = w.get_temperature('fahrenheit') 
status = w.get_status()

r = 75
g = 150
b = 130
sense.show_message(status, 0.1, [r,g,b])
sense.show_message(temp, 0.1, [r,g,b])

if w.get_status() == 'Clouds':
    sense.set_pixels(clouds)
elif w.get_status() == 'Clear':
    sense.set_pixels(clear)
elif w.get_status() == 'Snowy':
    sense.set_pixels(snowy)
elif w.get_status() == 'Rain':
    sense.set_pixels(rain)
else:
    sense.set_pixels(not_found)

stormy  = [
    BL, BL, Y, Y, Y, Y, BL, BL,
    BL, Y, Y, Y, Y, BL, BL, BL, 
    Y, Y, Y, Y, BL, BL, BL, BL,
    BL, Y, Y, Y, Y, BL, BL, BL,
    BL, BL, Y, Y, Y, Y, BL, BL,
    BL, BL, BL, Y, Y, Y, Y, BL,
    BL, BL, BL, Y, Y, Y, BL, BL,
    BL, BL, BL, Y, Y, BL, BL, BL,
]
