import time
from power import Hantek_PPS2116A

if __name__ == '__main__':
    
    print('WARNING: Run test Under development')
    Ch1_Potential = 19.2        #voltage in V
    Ch1_Current = 5          #amperage in A

    print ('Ch1 Voltage Set To: ' + str(Ch1_Potential) + ' V')
    print ('Ch1 Amperage Set To: ' + str(Ch1_Current) + ' A')

    print ('\r')

    ps = Hantek_PPS2116A()

    #ps.init_serial()


    ps.set_voltage(voltage=Ch1_Potential)
    ps.set_current(current=Ch1_Current)

    time.sleep(.1)

    print(ps.read_device_model())
    ps.serial_port.close()
  #  ps.set_on()

   # ps.set_off()
