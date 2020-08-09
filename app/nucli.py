#!/usr/bin/python3

import click
from .nettools.ping_tools import PingTools


@click.group()
def nucli():
    pass


@click.command()
@click.option('--host', help='Host IP Address')
@click.option('--iface', default='', help='(optional) Source Interface')
def ping(host, iface):
    pt = PingTools()
    pr = pt.ping(host, iface)
    print(pr)


@click.command()
@click.option('--start', help='Starting IP Address')
@click.option('--end', default='', help='(optional) Ending IP Address')
@click.option('--iface', default='', help='(optional) Source Interface')
def ping_range(start, end, iface):
    pt = PingTools()
    pr = pt.ping_range(start, end, iface)
    print(pr)


nucli.add_command(ping)
nucli.add_command(ping_range)


def click_entry():
    '''Entry Point for Setuptools Integration with Click.'''
    nucli()


if __name__ == '__main__':
    nucli()
