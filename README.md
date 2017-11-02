# hantek-pps2116A
Controlling a Hantek PPS 2116A Power Supply using Python 3. 

## Introduction

In www.enertronicsar.com  have a Hantek PPS 2116A Power Supply. Some characteristics of this power supply are: 


. Low ripple
. High resolution: 10mV, 1mA
. Features selectable auto-serial or parallel function
. Convenient software calibration for use with PC
. High-stability
. Low drift
. Built in over voltage and over current protection
. Cooling by internal thermostatically controlled fan
. Voltage Output: 0-32VDC
. Current Output: 0-5 amps
. Source Effect: CV≤0.01%+3mV(mA)
. Load Effect:
. CV≤0.01%+3mV(I≤3A)
. CC≤0.2%+3mA(I≤3A)
. CV≤0.02%+5mV(I>3A)
. CC≤0.2%+5mA(I>3A)
. Ripple and Noise:
   . CV≤l.0mVrms(I≤3A)
   . CC≤3mArms(I≤3A)
   . CV≤2.0mVrms(I>3A)
   . CC≤6mArms(I>3A)
. Read accuracy:
. Read accuracy voltage: <±(read values 0.5% + 2bit)
. Read accuracy current: <±(read values 1% + 2bit)
. Temperature: 0-- + 40 deg C
. Humidity: ≤80%
. Power: 110VAC, 60Hz
. Dimensions: 350mm x 150mm x 210mm
. Weight: 5.44kg, 12 lbs

We're using it in a testbench of some power electronics componentes that are likely to explode (yes, you read it right), so we decided to use all the instruments remotely. 

## Requirements

1. Python 3.
2. PySerial. `python3 -m pip install pyserial`
3. A Hantek PPS 2116A Power Supply.
4. A USB port available. 
5. Linux OS. (We use it in Debian Stretc so far). 

## How to use it...

Explore the `Hantek_PPS2116A` class. There you can find some usefull methods to turn on and off, set current and voltage, and some other interesting tools. 

The `test.py` program is under development. 