from init_router import *
from netmiko import ConnectHandler

for route in routers:
    print(ConnectHandler(**route).send_command('show ip route'))
