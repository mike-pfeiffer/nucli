#!/usr/bin/python3

import os
import subprocess
import sys

from netaddr import (IPAddress, IPRange, IPNetwork, AddrConversionError,
    AddrFormatError, NotRegisteredError)

IPV6_LINK_LOCAL = IPNetwork("FE80::/10")

class PingTools:

    def ping(self, ip, iface):
        """
        """
        cmd = "ping"
        options = "-c 1 -W 1 -qn"
        echo_request = []

        if iface:
            echo_request = [cmd, '-I', iface, options, ip]
        else:
            echo_request = [cmd, options, ip]
        
        echo_reply = subprocess.call(echo_request,
                                     stdout=open(os.devnull,'wb'))

        if echo_reply == 0:
            return True
        else:
            return False

    def ping_range(self, start, end, iface):
        """Ping user-defined range of IP addresses to check for liveliness

        Parameters
        ----------
        start : str
            Starting IP address
        end : str
            Ending IP address
        iface : str
            Interface name

        Raises
        ------
        AddrConversionError
            Netaddr custom exception
            "a failure to convert between address types or notations"
        AddrFormatError
            Netaddr custom exception
            "a network address is not correctly formatted."
        NotRegisteredError
            Netaddr custom exception
            "an OUI or IAB was not found in the IEEE Registry"
        ValueError
            Handles IPRange exception in netaddr library

        Returns
        -------
        list
            A list of IP addresses that responded to ping

        """

        available_hosts = {}

        try:
            start = IPAddress(start)
            if end:
                end = IPAddress(end)
            else:
                end = IPAddress(start)

            if start.is_unicast() and end.is_unicast():
                ip_range = IPRange(start, end)
            else:
                sys.exit('Only unicast address type supported')

            for ip in ip_range:
                ip = str(ip)
                is_alive = self.ping(ip, iface)
                if is_alive:
                    available_hosts[ip] = is_alive
                else:
                    available_hosts[ip] = is_alive

        except AddrConversionError as e:
            sys.exit(e)
        except AddrFormatError as e:
            sys.exit(e)
        except NotRegisteredError as e:
            sys.exit(e)
        except ValueError as e:
            sys.exit(e)

        return available_hosts
