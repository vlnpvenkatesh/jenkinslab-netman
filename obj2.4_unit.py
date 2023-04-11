import unittest
from netmiko import ConnectHandler
import re

class Jenkinss:
    def obj1():
        router3={
            "host":"198.51.100.13",
            "username": "lab",
            "password": "lab123",
            "secret": "venky",
            "device_type": "cisco_ios"
        }
        conn = ConnectHandler(**router3)
        conn.enable()

        commands=["do show ip int br loopback99"]
        myoutput=conn.send_config_set(commands)

        final=re.search('((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))',myoutput)
        ip=final.group(1)
        if ip=="10.1.3.1":
            return True
        else:
            return False 
        
    def obj2():
        router1={
            "host":"198.51.100.11",
            "username": "lab",
            "password": "lab123",
            "secret": "venky",
            "device_type": "cisco_ios"
        }
        conn = ConnectHandler(**router1)
        conn.enable()

        commands=["do show ip ospf | in areas in"]
        myoutput=conn.send_config_set(commands)

        final=re.search('Number of areas in this router is (\d+).',myoutput)
        result=final.group(1)
        if result==str(1):
            return True
        else:
            return False 
    
    def obj3():
        router1={
            "host":"198.51.100.12",
            "username": "lab",
            "password": "lab123",
            "secret": "venky",
            "device_type": "cisco_ios"
        }
        conn = ConnectHandler(**router1)
        conn.enable()

        commands=["do ping 10.1.5.1 source 10.1.2.1"]
        myoutput=conn.send_config_set(commands)

        final=re.search('(5/5)',myoutput)
        result=final.group(1)

        if result=="4/5" or result=="5/5":
            return True
        else:
            return False 


class TestClass(unittest.TestCase):
    def runTest(self):
        print("starting unittesting")
        self.assertTrue(Jenkinss.obj1())
        print("passed1")
        self.assertTrue(Jenkinss.obj2())
        print("passed2")
        self.assertTrue(Jenkinss.obj3())
        print("passed3")

unittest.main()




