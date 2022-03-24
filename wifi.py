
import os

name = input("wifi Name (SSID) : ")
passwd = input("wifi Password : ")

f = open("/etc/network/interfaces", "w")

f.write("""

network:
    ethernets:
        eth0:
            dhcp4: true
            optional: true
    version: 2
    wifis:
        wlp3s0:
            optional: true
            access-points:
                """+name+"""
                    password: 
                        """+passwd+"""
                            dhcp4: true

""")

f.close()

