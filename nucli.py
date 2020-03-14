#!/usr/bin/python3

import click
from nutils import ping_tools

@click.group()
def nucli():
    pass

@click.command()
@click.option('--start', help='Starting IP Address')
@click.option('--end', default = '', help='(optional) Ending IP Address')
@click.option('--iface', default= '', help='(optional) Source Interface')
def ping_sweep(start, end, iface):
    ping_tools.ping_range(start, end, iface)


nucli.add_command(ping_sweep)

def click_entry():
    '''Entry Point for Setuptools Integration with Click.'''
    nucli()

if __name__ == '__main__':
    nucli()
