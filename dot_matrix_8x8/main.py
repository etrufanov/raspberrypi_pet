# HT16K33 control board
# https://cdn-shop.adafruit.com/datasheets/ht16K33v110.pdf

from machine import I2C, Pin
import time


i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# system on
i2c.writeto(0x70, bytes([0b00100001]))

# display on
i2c.writeto(0x70, bytes([0b10000001]))

# dim at 1/16 (brightness)
i2c.writeto(0x70, bytes([0b11100001]))

b_arr = bytearray(17)
# emoji icon
# 8 items = 8 matrix rows
# 1 byte (item) = 8 row leds 
b_inp = [0x3c, 0x66, 0x99, 0x81, 0xa5, 0x99, 0x66, 0x3c]

# declare shift to move icon
for shift in range(-8, 9):
    for i, x in enumerate(b_inp):
        b_arr[i * 2 + 1] = shift >= 0 and x << shift or x >> abs(shift)

    # data bytes are form of 0x00 - data byte - 0x00 - data byte - ...
    i2c.writeto(0x70, bytes(b_arr))
    
    time.sleep_ms(50)

