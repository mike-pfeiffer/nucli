#!/usr/bin/python3

import os
import subprocess
import sys
import netaddr
from netaddr import *

class PingTools:

    def ping_range(start, end):
        available_hosts = []
        
        try:
            start = IPAddress(start)
            end = IPAddress(end)

            start_ver = start.version
            end_ver = end.version

            if start_ver == end_ver:
                ip_range = IPRange(start, end)
            else:
                sys.exit("Version mismatch: start = IPv" + str(start_ver)
                    + ", end = IPv" + str(end_ver))

            for ip in ip_range:
                ip = str(ip)
                echo_reply = subprocess.call(
                    ['ping', '-c', '3', '-W', '1', '-qn', str(ip)], 
                    stdout=open(os.devnull,'wb')
                    )
                if echo_reply == 0:
                    print(ip + " responded")
                    available_hosts.append(ip)
                elif echo_reply== 1:
                    print(ip + " failed to respond")

        except netaddr.AddrConversionError as e:
            print(e)
        except netaddr.AddrFormatError as e:
            print(e)
        except netaddr.NotRegisteredError as e:
            print(e)
        
        return available_hosts