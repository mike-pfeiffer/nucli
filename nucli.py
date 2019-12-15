#!/usr/bin/python3

import click
from nutils import *

@click.group()
def nucli():
    pass

@click.command()
@click.option('--start', help="Starting IP Address")
@click.option('--end', help="Ending IP Address")
def ping_sweep(start, end):
    PingTools.ping_range(start, end)

nucli.add_command(ping_sweep)

def click_entry():
    """Entry Point for Setuptools Integration with Click."""
    nucli()

if __name__ == '__main__':
    nucli()
