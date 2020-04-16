#Modified code obtained from Adafruit
#https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/overview

import adafruit_drv2605
import busio
import board
import time

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

# Initialize DRV2605 haptic controller
i2c = busio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c)

while True:
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    # Now we're connected

    while ble.connected:
        if uart.in_waiting:
            packet = Packet.from_stream(uart)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.BUTTON_1:
                        # The 1 button was pressed.
                        print("\nPULSES\nPulsing Strong 1\nPulsing Strong 2\nPulsing Medium 1\nPulsing Medium 2")
                        drv.sequence[0] = adafruit_drv2605.Effect(52)
                        drv.sequence[1] = adafruit_drv2605.Pause(1)
                        drv.sequence[2] = adafruit_drv2605.Effect(53)
                        drv.sequence[3] = adafruit_drv2605.Pause(1)
                        drv.sequence[4] = adafruit_drv2605.Effect(54)
                        drv.sequence[5] = adafruit_drv2605.Pause(1)
                        drv.sequence[6] = adafruit_drv2605.Effect(55)
                        drv.play()
                        #-----
                        time.sleep(6)
                        drv.stop()
                    elif packet.button == ButtonPacket.BUTTON_2:
                        # The 2 button was pressed.
                        print("\nPULSES *TEST*\nPulsing Strong 2\nPulsing Medium 2\nPulsing Medium 1\nPulsing Strong 1")
                        drv.sequence[0] = adafruit_drv2605.Effect(53)
                        drv.sequence[1] = adafruit_drv2605.Pause(1)
                        drv.sequence[2] = adafruit_drv2605.Effect(55)
                        drv.sequence[3] = adafruit_drv2605.Pause(1)
                        drv.sequence[4] = adafruit_drv2605.Effect(54)
                        drv.sequence[5] = adafruit_drv2605.Pause(1)
                        drv.sequence[6] = adafruit_drv2605.Effect(52)
                        drv.play()
                        #-----
                        time.sleep(6)
                        drv.stop()
                    elif packet.button == ButtonPacket.BUTTON_3:
                        # The 3 button was pressed.
                        print("\nTRANSITIONS\nTransition Click 1\nTransition Click 3\nTransition Hum 1\nTransition Hum 3")
                        drv.sequence[0] = adafruit_drv2605.Effect(58)
                        drv.sequence[1] = adafruit_drv2605.Pause(1)
                        drv.sequence[2] = adafruit_drv2605.Effect(60)
                        drv.sequence[3] = adafruit_drv2605.Pause(1)
                        drv.sequence[4] = adafruit_drv2605.Effect(64)
                        drv.sequence[5] = adafruit_drv2605.Pause(1)
                        drv.sequence[6] = adafruit_drv2605.Effect(66)
                        drv.play()
                        #-----
                        time.sleep(6)
                        drv.stop()
                    elif packet.button == ButtonPacket.BUTTON_4:
                        # The 4 button was pressed.
                        print("4 button pressed!")
                        drv.sequence[0] = adafruit_drv2605.Effect(64)
                        drv.sequence[1] = adafruit_drv2605.Pause(1)
                        drv.sequence[2] = adafruit_drv2605.Effect(60)
                        drv.sequence[3] = adafruit_drv2605.Pause(1)
                        drv.sequence[4] = adafruit_drv2605.Effect(58)
                        drv.sequence[5] = adafruit_drv2605.Pause(1)
                        drv.sequence[6] = adafruit_drv2605.Effect(66)
                        drv.play()
                        #-----
                        time.sleep(6)
                        drv.stop()
                    elif packet.button == ButtonPacket.UP:
                        # The UP button was pressed.
                        print("\nWAVEFORM TYPES\nStrong Click\nSharp Tick\nSoft Bump\nStrong Buzz")
                        drv.sequence[0] = adafruit_drv2605.Effect(1)
                        drv.sequence[1] = adafruit_drv2605.Pause(1)
                        drv.sequence[2] = adafruit_drv2605.Effect(24)
                        drv.sequence[3] = adafruit_drv2605.Pause(1)
                        drv.sequence[4] = adafruit_drv2605.Effect(7)
                        drv.sequence[5] = adafruit_drv2605.Pause(1)
                        drv.sequence[6] = adafruit_drv2605.Effect(14)
                        drv.play()
                        #-----
                        time.sleep(6)
                        drv.stop()
                    elif packet.button == ButtonPacket.RIGHT:
                        # The RIGHT button was pressed.
                        print("\nWAVEFORM TYPES *TEST*\nStrong Buzz\nSharp Tick\nStrong Click\nSoft Bump\n*")
                        drv.sequence[0] = adafruit_drv2605.Effect(14)
                        drv.sequence[1] = adafruit_drv2605.Pause(1)
                        drv.sequence[2] = adafruit_drv2605.Effect(24)
                        drv.sequence[3] = adafruit_drv2605.Pause(1)
                        drv.sequence[4] = adafruit_drv2605.Effect(1)
                        drv.sequence[5] = adafruit_drv2605.Pause(1)
                        drv.sequence[6] = adafruit_drv2605.Effect(7)
                        drv.play()
                        #-----
                        time.sleep(6)
                        drv.stop()
                    elif packet.button == ButtonPacket.DOWN:
                        # The DOWN button was pressed.
                        print("\nSTRENGTH & DURATION\nStrong Click\nMedium Click\nShort Double Click Strong\nLong Double Click Strong\n-")
                        drv.sequence[0] = adafruit_drv2605.Effect(17)
                        drv.sequence[1] = adafruit_drv2605.Pause(1)
                        drv.sequence[2] = adafruit_drv2605.Effect(21)
                        drv.sequence[3] = adafruit_drv2605.Pause(1)
                        drv.sequence[4] = adafruit_drv2605.Effect(27)
                        drv.sequence[5] = adafruit_drv2605.Pause(1)
                        drv.sequence[6] = adafruit_drv2605.Effect(37)
                        drv.play()
                        #-----
                        time.sleep(6)
                        drv.stop()
                    elif packet.button == ButtonPacket.LEFT:
                        # The LEFT button was pressed.
                        print("\nSTRENGTH & DURATION *TEST*\nLong Double Click Strong\nMedium Click\nStrong Click\nShort Double Click\n=")
                        drv.sequence[0] = adafruit_drv2605.Effect(37)
                        drv.sequence[1] = adafruit_drv2605.Pause(1)
                        drv.sequence[2] = adafruit_drv2605.Effect(21)
                        drv.sequence[3] = adafruit_drv2605.Pause(1)
                        drv.sequence[4] = adafruit_drv2605.Effect(17)
                        drv.sequence[5] = adafruit_drv2605.Pause(1)
                        drv.sequence[6] = adafruit_drv2605.Effect(27)
                        drv.play()
                        time.sleep(6)
                        drv.stop()
    # If we got here, we lost the connection. Go up to the top and start
    # advertising again and waiting for a connection.