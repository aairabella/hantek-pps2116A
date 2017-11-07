import time
from power import Hantek_PPS2116A

if __name__ == '__main__':
    
    print('WARNING: Run test for all the fuckin\' commands')
    commands = ['rv', 'ra', 'ru', 'ri', 'rs']
    print ('\r')

    ps = Hantek_PPS2116A()

    ps.init_serial()

    ps.set_voltage(voltage=5.25)

    ps.set_current(current=0.1)

    ps.set_on()

    time.sleep(1)

    print(ps.read_status())

    print(ps.read_measured_voltage())

    print(ps.read_measured_current())


    print(ps.read_set_voltage())

    print(ps.read_set_current())


    ps.set_off()


"""
    for _ in commands:
        print('Command: %s' % _)
        ps.send_command_and_print_response(command=_)
        time.sleep(0.3)
"""