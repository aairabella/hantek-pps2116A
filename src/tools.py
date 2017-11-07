# Tools
# Some functions to support: 
#   1) Current and Voltage conversion to String. The Power Suppy requires a string formed by 4 characters. Two funtions were included to support input of voltage and current as floats.    2) A run_test() function is added to perform some basic tests. 

def convert_voltage_to_string(voltage):
   voltage_string = str(voltage)
   if voltage < 10:
       if len(voltage_string) == 3:
           output_string = '0' + voltage_string[0] + voltage_string[2] + '0'
       if len(voltage_string) == 4:
           output_string = '0' + voltage_string[0] + voltage_string[2:4] 
   else:
       if len(voltage_string) == 2:
           output_string = voltage_string[0:2] + '00'
       if len(voltage_string) == 4:
           output_string = voltage_string[0:2] + voltage_string[3] + '0'
       if len(voltage_string) == 5:
           output_string = voltage_string[0:2] + voltage_string[3:5]

   return output_string


def convert_current_to_string(current):
   current_string = str(current)
   if len(current_string) == 1:
       output_string = current_string[0] + '000'
   if len(current_string) == 3:
       output_string = current_string[0] + current_string[2] + '00'
   if len(current_string) == 4:
       output_string = current_string[0] + current_string[2:4] + '0'
   if len(current_string) == 5:
       output_string = current_string[0] + current_string[2:5]

   return output_string
