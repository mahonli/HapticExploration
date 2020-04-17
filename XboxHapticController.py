"""
Circuit Playground Express GBoard: arcade buttons generating keycodes

Adafruit invests time and resources providing this open source code.
Please support Adafruit and open source hardware by purchasing
products from Adafruit!

Written by Dave Astels for Adafruit Industries
Copyright (c) 2018 Adafruit Industries
Licensed under the MIT license.

All text above must be included in any redistribution.
"""
import adafruit_drv2605
import busio
import board
import time
from digitalio import DigitalInOut, Direction, Pull
from adafruit_circuitplayground import cp

# Converts touchpads to digial inputs
button_a = DigitalInOut(board.A1)
button_a.direction = Direction.INPUT
button_a.pull = Pull.UP

button_b = DigitalInOut(board.A2)
button_b.direction = Direction.INPUT
button_b.pull = Pull.UP

# Initialize DRV2605 haptic controller
i2c = busio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c)

cp.pixels.brightness = 0.3
cp.pixels.fill((0, 0, 0))  # Turn off the NeoPixels if they're on!

def touch_a():
    return not button_a.value


def touch_b():
    return not button_b.value


while True:
    if touch_a():
        print("\nRight Bumper\n")

        # Set NeoPixel colour to green on button press
        cp.pixels[0] = (0,255,0)

        # Play haptic waveform sequence
        drv.sequence[0] = adafruit_drv2605.Effect(64)
        drv.sequence[1] = adafruit_drv2605.Effect(58)
        drv.play()

        while touch_a():
            pass
    else:
        cp.pixels[0] = (0,0,0)

    if touch_b():
        print("\nLeft Bumper\n")

        # Set NeoPixel colour to green on button press
        cp.pixels[9] = (0,255,0)

        # Play haptic waveform sequence
        drv.sequence[0] = adafruit_drv2605.Effect(17)
        drv.sequence[1] = adafruit_drv2605.Effect(6)
        drv.play()

        while touch_b():
            pass
    else:
        cp.pixels[9] = (0,0,0)