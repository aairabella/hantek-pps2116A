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

        if voltage > 32:
            print('Sorry! Max. Voltage value is 32V')
            quit()

        Ch1VoltageSet = 'su' + convert_voltage_to_string(voltage) + str('\r')
        self.ser.write(bytes(Ch1VoltageSet, 'utf-8'))
        time.sleep(.01)
        set_voltage_status = str(self.ser.readline())

        if set_voltage_status[2:4] != 'ok':
            print('I couldn\'t set the voltage as you requested')
            quit()
        
    def set_current(self, current):
        if current > 5:
            print('Sorry! Max. Ccurrent value is 5A')
            quit()
            
        Ch1AmperageSet = 'si' + convert_current_to_string(current) + str('\r')
        self.ser.write(bytes(Ch1AmperageSet, 'utf-8'))
        time.sleep(.01)

        set_current_status = str(self.ser.readline())

        if set_current_status[2:4] != 'ok':
            print('I couldn\'t set the current as you requested')
            quit()

    def set_on(self):
        self.ser.write(bytes(str('o1' + '\r'), 'utf-8'))
        time.sleep(.01)

        set_on_status = str(self.ser.readline())

        if set_on_status[2:4] != 'ok':
            print('I couldn\'t set the the Power Supply ON as you requested')
            quit()

    def set_off(self):
        self.ser.write(bytes(str('o0' + '\r'), 'utf-8'))
        time.sleep(.01)

        set_off_status = str(self.ser.readline())

        if set_off_status[2:4] != 'ok':
            print('I couldn\'t set the the Power Supply OFF as you requested')
            quit()

    def read_measured_voltage(self):
        self.ser.write(bytes(str('rv' + '\r'), 'utf-8'))
        read_measured_voltage_value = self.ser.readline()
        
        return int(read_measured_voltage_value)/100


    def read_measured_current(self):
        self.ser.write(bytes(str('ra' + '\r'), 'utf-8'))
        read_measured_current_value = self.ser.readline()
        
        return int(read_measured_current_value)/1000

    def read_set_voltage(self):
        self.ser.write(bytes(str('ru' + '\r'), 'utf-8'))
        read_set_voltage_value = self.ser.readline()
        
        return int(read_set_voltage_value)/100


    def read_set_current(self):
        self.ser.write(bytes(str('ri' + '\r'), 'utf-8'))
        read_set_current_value = self.ser.readline()
        
        return int(read_set_current_value)/1000


    def read_status(self):
        self.ser.write(bytes(str('rs' + '\r'), 'utf-8'))
        ps_status = self.ser.readline()
        
        if   str(ps_status)[5] ==  '1':
            return 'CV'
        elif str(ps_status)[5] ==  '6':
            return 'CC'
        else:
            return 'Error'

    def send_command_and_print_response(self, command):
        
        print('Response: %s' % self.ser.write(bytes(command + str('\r'), 'utf-8')))
        time.sleep(.01)
        print('Readout:  %s' % self.ser.readline())
        time.sleep(.01)