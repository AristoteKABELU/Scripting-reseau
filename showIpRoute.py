from init_router import R1, R2
from netmiko import ConnectHandler

netConnect = ConnectHandler(**R1)
output_router1 = netConnect.send_command('show ip route')

netConnect = ConnectHandler(**R2)
output_router2 = netConnect.send_command('show ip route')
print(output_router1,
      '\n------------------------------------------------------------------------------\n',
      output_router2)
