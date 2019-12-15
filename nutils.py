#!/usr/bin/python3

import os
import subprocess
import sys

from netaddr import (IPAddress, IPRange, IPNetwork, AddrConversionError,
    AddrFormatError, NotRegisteredError)

LINK_LOCAL = IPNetwork('FE80::/10')

class PingTools:

    @staticmethod
    def ping_range(start, end, iface):
        """
        """

        cmd = 'ping'
        options = '-c 3 -W 1 -qn'
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

            if (start in LINK_LOCAL) and (end in LINK_LOCAL):
                if iface:
                    iface = "%" + iface.lower()
                else:
                    sys.exit("IPv6 LLA requires an interface source")

            for ip in ip_range:
                ip = str(ip)
                echo_reply = subprocess.call(
                    [cmd, options, str(ip) + iface], 
                    stdout=open(os.devnull,'wb')
                    )
                if echo_reply == 0:
                    print(ip + " responded")
                    available_hosts.append(ip)
                elif echo_reply== 1:
                    print(ip + " failed to respond")

        except AddrConversionError as e:
            sys.exit(e)
        except AddrFormatError as e:
            sys.exit(e)
        except NotRegisteredError as e:
            sys.exit(e)
        
        return available_hosts
