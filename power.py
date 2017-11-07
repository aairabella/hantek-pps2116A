import time
import serial
from tools import convert_voltage_to_string


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
        Ch1AmperageSet = 'si' + str(Ch1_Current) + str('\r')
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
        #v = self.ser.readline()
        print(v)
        #print('Voltage %d' % 


    def read_current(self):
        print('Current')


if __name__ == '__main__':

    Ch1_Potential = 10.2        #voltage in V
    Ch1_Current = 4321          #amperage in mA

    Ch1VoltageCall = 'su'
    Ch1AmpereageCall = 'si'

    Return = '\r'

    print ('\r')

    print ('Ch1 Voltage Set To: ' + str(Ch1_Potential) + ' V')
    print ('Ch1 Amperage Set To: ' + str(Ch1_Current) + ' mA')

    print ('\r')

    ps = Hantek_PPS2116A()

    ps.init_serial()


    ps.set_voltage(voltage=Ch1_Potential)
    ps.set_current(current=Ch1_Current)

    time.sleep(1)
    ps.set_on()

    ps.read_voltage()
    time.sleep(2)

    ps.set_off()


