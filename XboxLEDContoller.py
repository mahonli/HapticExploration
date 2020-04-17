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
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_circuitplayground import cp


button_a = DigitalInOut(board.A1)
button_a.direction = Direction.INPUT
button_a.pull = Pull.UP

button_b = DigitalInOut(board.A2)
button_b.direction = Direction.INPUT
button_b.pull = Pull.UP

cp.pixels.brightness = 0.3
cp.pixels.fill((0, 0, 0))  # Turn off the NeoPixels if they're on!

def touch_a():
    return not button_a.value


def touch_b():
    return not button_b.value


while True:
    if touch_a():
        print("\nRight Bumper\n")
        cp.pixels[0] = (0,255,0)

        while touch_a():
            pass
    else:
        cp.pixels[0] = (0,0,0)

    if touch_b():
        print("\nLeft Bumper\n")
        cp.pixels[9] = (0,255,0)

        while touch_b():
            pass
    else:
        cp.pixels[9] = (0,0,0)