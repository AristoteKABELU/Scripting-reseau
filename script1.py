from netmiko import ConnectHandler
from init_router import *

for router in routers:
    net_connect = ConnectHandler(**router)
    configurations = [
        'router ospf 1',
        'network 10.10.20.0 0.0.0.255 area 10',
        'network 10.10.10.0 0.0.0.255 area 10',
        'network 192.168.122.0 0.0.0.255 area 10'
    ]
    for v in router.values():
        if v == 'scripting1':
            configurations.append(['interface f1/0',
                                   'ip address 10.10.10.1 255.255.255.0',
                                   'no shutdown'])
        elif v == 'scripting2':
            configurations.append(['interface f1/0',
                                   'ip address 10.10.20.1 255.255.255.0',
                                   'no shutdown'])
    for conf in configurations:
        net_connect.send_config_set(conf)
