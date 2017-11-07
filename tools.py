# Tools

def convert_voltage_to_string(voltage):
   voltage_string = str(voltage)
   if voltage < 10:
       if len(voltage_string) == 3:
           output_string = '0' + str(voltage)[0] + str(voltage)[2] + '0'
       if len(voltage_string) == 4:
           output_string = '0' + str(voltage)[0] + str(voltage)[2:4] 
   else:
       if len(voltage_string) == 2:
           output_string = str(voltage)[0:2] + '00'
       if len(voltage_string) == 4:
           output_string = str(voltage)[0:2] + str(voltage)[3] + '0'
       if len(voltage_string) == 5:
           output_string = str(voltage)[0:2] + str(voltage)[3:5]

   return output_string
