#!/usr/bin/python3

import os
import subprocess
import sys

from netaddr import (IPAddress, IPRange, IPNetwork, AddrConversionError,
    AddrFormatError, NotRegisteredError)

IPV6_LINK_LOCAL = IPNetwork('FE80::/10')

class PingTools:

    def ping_range(start, end, iface):
        ''' Ping user-defined range of IP addresses to check for liveliness

        Parameters
        ----------
        start : str
            Starting IP address
        end : str
            Ending IP address
        iface : str
            Interface name
        cmd : str
            Ping command
        options : str
            Applied ping options
        echo_request : list
            Full ping request for subprocess call
        available_hosts : list
            A list for storing available hosts

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

        '''

        cmd = 'ping'
        options = '-c 3 -W 1 -qn'
        echo_request = []
        available_hosts = []

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

            if iface:
                echo_request = [cmd, '-I', iface, options]
            else:
                echo_request = [cmd, options]

            for ip in ip_range:
                ip = str(ip)
                echo_request.append(ip)
                echo_reply = subprocess.call(
                    echo_request,
                    stdout=open(os.devnull,'wb')
                )

                if echo_reply == 0:
                    print(ip + ' responded')
                    available_hosts.append(ip)
                elif echo_reply== 1:
                    print(ip + ' failed to respond')

                echo_request.remove(ip)

        except AddrConversionError as e:
            sys.exit(e)
        except AddrFormatError as e:
            sys.exit(e)
        except NotRegisteredError as e:
            sys.exit(e)
        except ValueError as e:
            sys.exit(e)

        return available_hosts
