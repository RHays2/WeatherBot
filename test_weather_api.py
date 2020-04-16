import pyowm
owm = pyowm.OWM('4dc989dc9fceac17d923773b08e23ec7')
observation = owm.weather_at_place('Anchorage, US')
w = observation.get_weather()
print(w.get_status())
# print(w.get_temperature('fahrenheit')) 
