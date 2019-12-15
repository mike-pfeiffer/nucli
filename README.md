# network-utilities

This is a collection of common tools network administrators use.  Click provides a simple command line interface for use.

## Requirements

The requirements.txt file uses the following Python libraries:

[netaddr](https://netaddr.readthedocs.io/en/latest/introduction.html)

[click](https://click.palletsprojects.com/en/7.x/)

## CLI Usage

### Example 1

```
$ python3 nucli.py 
Usage: nucli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  ping-sweep
```

### Example 2

```
$ python3 nucli.py ping-sweep --start 192.0.2.198 --end 192.0.2.200
192.0.2.198 failed to respond
192.0.2.199 failed to respond
192.0.2.200 responded
```