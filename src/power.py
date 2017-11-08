import time
import serial
from tools import convert_voltage_to_string
from tools import convert_current_to_string

class Hantek_PPS2116A(object):
    def __init__(self):

        # List all serial ports. 

        # Find where is connected the power supply

        # Init serial
        self.init_serial()


    def init_serial(self):
        self.serial_port = serial.Serial(
            port='/dev/ttySLAB0',
            baudrate=9600,
            timeout=1
        )
        #print ('Port: ' + self.serial_port.name)       # check which port was really used


    def set_voltage(self, voltage):

        if voltage > 32:
            print('Sorry! Max. Voltage value is 32V')
            quit()

        Ch1VoltageSet = 'su' + convert_voltage_to_string(voltage) + str('\r')
        self.serial_port.write(bytes(Ch1VoltageSet, 'utf-8'))
        time.sleep(.01)
        set_voltage_status = str(self.serial_port.readline())

        if set_voltage_status[2:4] != 'ok':
            print('I couldn\'t set the voltage as you requested')
            quit()

        
    def set_current(self, current):
        if current > 5:
            print('Sorry! Max. Ccurrent value is 5A')
            quit()

        Ch1AmperageSet = 'si' + convert_current_to_string(current) + str('\r')
        self.serial_port.write(bytes(Ch1AmperageSet, 'utf-8'))
        time.sleep(.01)

        set_current_status = str(self.serial_port.readline())

        if set_current_status[2:4] != 'ok':
            print('I couldn\'t set the current as you requested')
            quit()


    def set_on(self):
        self.serial_port.write(bytes(str('o1' + '\r'), 'utf-8'))
        time.sleep(.01)

        set_on_status = str(self.serial_port.readline())

        if set_on_status[2:4] != 'ok':
            print('I couldn\'t set the Power Supply ON as you requested')
            quit()


    def set_off(self):
        self.serial_port.write(bytes(str('o0' + '\r'), 'utf-8'))
        time.sleep(.01)

        set_off_status = str(self.serial_port.readline())

        if set_off_status[2:4] != 'ok':
            print('I couldn\'t set the Power Supply OFF as you requested')
            quit()


    def read_measured_voltage(self):
        self.serial_port.write(bytes(str('rv' + '\r'), 'utf-8'))
        read_measured_voltage_value = self.serial_port.readline()
        
        return int(read_measured_voltage_value)/100


    def read_measured_current(self):
        self.serial_port.write(bytes(str('ra' + '\r'), 'utf-8'))
        read_measured_current_value = self.serial_port.readline()
        
        return int(read_measured_current_value)/1000


    def read_set_voltage(self):
        self.serial_port.write(bytes(str('ru' + '\r'), 'utf-8'))
        read_set_voltage_value = self.serial_port.readline()
        
        return int(read_set_voltage_value)/100


    def read_set_current(self):
        self.serial_port.write(bytes(str('ri' + '\r'), 'utf-8'))
        read_set_current_value = self.serial_port.readline()
        
        return int(read_set_current_value)/1000


    def read_status(self):
        self.serial_port.write(bytes(str('rs' + '\r'), 'utf-8'))
        ps_status = self.serial_port.readline()
        
        if   str(ps_status)[5] ==  '1':
            return 'CV'
        elif str(ps_status)[5] ==  '6':
            return 'CC'
        else:
            return 'Error'

    def send_command_and_print_response(self, command):
        
        print('Response: %s' % self.serial_port.write(bytes(command + str('\r'), 'utf-8')))
        time.sleep(.01)
        print('Readout:  %s' % self.serial_port.readline())
        time.sleep(.01)
