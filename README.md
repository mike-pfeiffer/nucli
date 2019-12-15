# network-utilities

The network-utilities repository is meant to be a collection of commonly used tools for network administrators.  These tools are bundled under *nutils* as functions within broader classes.  The *nutils* library can be used independently of the *nucli* command line option.  *nucli* is supported by Click and provides a simple CLI for leveraging the tools found in *nutils*.

## Initial Setup

1. Clone the repository
```
$ git clone https://github.com/pfeiffermj/network-utilities.git
```
2. Install the requirements.txt file
```
$ pip3 install -r requirements.txt
```
3. Install the setup.py file
```
$ pip3 install -e .
```
4. Test your installation
```
$ nucli
```

## Python Libraries

[netaddr](https://netaddr.readthedocs.io/en/latest/introduction.html)

[click](https://click.palletsprojects.com/en/7.x/)

## CLI Usage

### Main

Demonstrates calling *nucli* directly from shell without requiring the file to be executable or prefaced with python3:

```
$ nucli
Usage: nucli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  ping-sweep
```

### ping-sweep

Demonstrates the *ping-sweep* tool being executed from *nucli* CLI.

IPv4 example:

```
$ nucli ping-sweep --start 192.0.2.198 --end 192.0.2.200
192.0.2.198 failed to respond
192.0.2.199 failed to respond
192.0.2.200 responded
```

IPv6 example:

```
$ nucli ping-sweep --start fe80::20c:29ff:fe7a:bcf3 --end fe80::20c:29ff:fe7a:bcf5 --iface ens33
fe80::20c:29ff:fe7a:bcf3 responded
fe80::20c:29ff:fe7a:bcf4 failed to respond
fe80::20c:29ff:fe7a:bcf5 failed to respond
```