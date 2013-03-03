"""
Author: Nate Levesque <public@thenaterhood.com>
Language: Python3
Filename: raspi_binaryClock.py
Description:
    Uses the raspberry pi GPIO output to show the current time (in binary).
    Each pin controls an individual LED as per how the raspi_binary_gpio
    class works.
"""
from datetime import datetime
from time import sleep
from raspi_bus_gpio import gpio


def main():
    while True:
        """
        Loops and retrieves the current hour and minute at each iteration
        then uses the gpio_binary_class to display it on an LED array, hour,
        5 second pause, then minutes.  Loops until the program is manually
        stopped
        """
        thisHour = int( datetime.now().strftime("%I") )
        thisMinute = int( datetime.now().strftime("%M" ) )
        
        instance.Tx( thisHour )
        sleep( 5 )
        instance.Tx( thisMinute + 128 )
        sleep( 5 )

try:
    instance = gpio(8)
    main()
except (KeyboardInterrupt):
    print("Received interrupt, exiting")
