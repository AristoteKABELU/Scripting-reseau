from netmiko import ConnectHandler
from init_router import R1, R2

# ----------configuration of the first Router-----------------------


net_connect = ConnectHandler(**R1)

config_interface_router1_commands = ['interface f1/0',
                                     'ip address 10.10.10.1 255.255.255.0',
                                     'no shutdown']
net_connect.send_config_set(config_interface_router1_commands)
config_ospf_router1 = [
    'router ospf 1',
    'network 10.10.10.0 0.0.0.255 area 10',
    'network 10.10.20.0 0.0.0.255 area 10',
    'network 192.168.122.0 0.0.0.255 area 10'
]
net_connect.send_config_set(config_ospf_router1)


# ----------configuration of the second Router-----------------------


net_connect = ConnectHandler(**R2)
config_interface_router2_commands = ['interface f1/0',
                                     'ip address 10.10.20.1 255.255.255.0',
                                     'no shutdown']
net_connect.send_config_set(config_interface_router2_commands)
output = net_connect.send_command('show ip interface brief')

config_ospf_router2 = [
    'router ospf 2',
    'network 10.10.20.0 0.0.0.255 area 10',
    'network 10.10.10.0 0.0.0.255 area 10',
    'network 192.168.122.0 0.0.0.255 area 10'
]
net_connect.send_config_set(config_ospf_router2)
