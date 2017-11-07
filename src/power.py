import time
import serial
from tools import convert_voltage_to_string
from tools import convert_current_to_string

class Hantek_PPS2116A(object):
    #__init__(self):

    # Detectar los Serial Ports

    # Probar conexion e imprimir tipo de device

    # guardar en port el nombre del puerto donde se encontro la fuente

    def init_serial(self):
        self.ser = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            timeout=1
        )
        print ('Port: ' + self.ser.name)       # check which port was really used

    def set_voltage(self, voltage):
        Ch1VoltageSet = 'su' + convert_voltage_to_string(voltage) + str('\r')
        self.ser.write(bytes(Ch1VoltageSet, 'utf-8'))
        time.sleep(.01)

    def set_current(self, current):
        Ch1AmperageSet = 'si' + convert_current_to_string(current) + str('\r')
        self.ser.write(bytes(Ch1AmperageSet, 'utf-8'))
        time.sleep(.01)

    def set_on(self):
        self.ser.write(bytes(str('o1' + '\r'), 'utf-8'))
        time.sleep(.01)


    def set_off(self):
        self.ser.write(bytes(str('o0' + '\r'), 'utf-8'))
        time.sleep(.01)

    def read_voltage(self):
        v = self.ser.write(bytes(str('rv' + '\r'), 'utf-8'))
        print('ya pedi')
        val = self.ser.readline()
        print(v)
        print(val)


    def read_current(self):
        print('Current')   
