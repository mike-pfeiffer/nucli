#!/usr/bin/python3

import os
import subprocess
import sys

from netaddr import (IPAddress, IPRange, IPNetwork, AddrConversionError,
                     AddrFormatError, NotRegisteredError)

IPV6_LINK_LOCAL = IPNetwork("FE80::/10")


class PingTools:

    def ping(self, ip, iface):
        """Ping user-defined range of IP addresses to check for liveliness

        Parameters
        ----------
        ip : str
            host ip address
        iface : str
            Interface name

        Returns
        -------
        boolean
            A boolean representing IP reachability

        """
        try:

            cmd = "ping"
            options = "-c 1 -W 1 -qn"
            echo_request = []

            if iface:
                echo_request = [cmd, '-I', iface, options, ip]
            else:
                echo_request = [cmd, options, ip]

            echo_reply = subprocess.call(echo_request,
                                         stdout=open(os.devnull, 'wb'))

            if echo_reply == 0:
                return True
            else:
                return False

        except TypeError as e:
            sys.exit(e)

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

        Returns
        -------
        dict
            A dict of IP addresses and boolean for liveliness

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
