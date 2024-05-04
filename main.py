
from machine import Pin, SoftI2C
from time import sleep
import dht 
import network
import urequests as requests
import ujson
import ssd1306


sensor = dht.DHT11(Pin(14))



while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)

    i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    oled.text('-------------------------------------', 0, 0)
    oled.text('Temp & Humidity', 0, 10)
    oled.text('-------------------------------------', 0, 20)
    oled.text('Temp: %3.1f C' %temp, 0, 30)
    oled.text('Temp: %3.1f F' %temp_f, 0, 40)
    oled.text('Humidity: %3.1f %%' %hum, 0, 50)        
    oled.text('-------------------------------------', 0, 60)
    oled.show()


  except OSError as e:
   print('Failed read or send information.') 