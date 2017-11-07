import time
from power import Hantek_PPS2116A

if __name__ == '__main__':
    
    print('WARNING: Run test Under development')
    Ch1_Potential = 10.2        #voltage in V
    Ch1_Current = 2.5          #amperage in mA

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
