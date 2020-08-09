![nucli workflow](https://github.com/pfeiffermj/nucli/workflows/nucli%20workflow/badge.svg)

# nucli

Network Utilities CLI (nucli) is a collection of commonly used tools for network engineers.

## System 

Built and tested on Ubuntu 18.04.3

## Setup (Makefile)

1. Clone the repository and change directory to nucli

```shell
$ git clone git clone https://github.com/pfeiffermj/nucli.git
$ cd nucli
```

2. Run the Makefile and activate virtual environment

```shell
$ make install
$ . env/bin/activate
```

3. Test your installation and begin using

```shell
$ nucli
```

4. When finished deactivate and clean

```shell
$ deactivate
$ make clean
```

## Setup (manual)

1. Clone the repository and change directory to nucli

```shell
$ git clone git clone https://github.com/pfeiffermj/nucli.git 
$ cd nucli
```

2. Create a virtual environment and activate it

```shell
$ python3 -m venv env
$ . env/bin/activate
```

3. Install setup and requirements

```shell
$ pip3 install -e .
$ pip3 install -r requirements.txt
```

4. Test your installation and begin using

```shell
$ nucli
```

5. Deactivate your virtual environment when finished

```shell
$ deactivate
```

## Linting & Testing

1. Navigate to **nucli** folder if not already in the directory

2. Run make options for **lint** and **test**

```shell
(env) ~/nucli$ make lint
(env) ~/nucli$ make test
```

## CLI Usage

### Main

Demonstrates calling *nucli* directly from shell without requiring the file to be executable or prefaced with python3:

```shell
$ nucli 
Usage: nucli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  ping-range
```

### ping-range

Demonstrates the *ping-range* tool being executed from *nucli* CLI.

IPv4 example:

```
$ nucli ping-range --start 192.0.2.198 --end 192.0.2.200
192.0.2.198 failed to respond
192.0.2.199 failed to respond
192.0.2.200 responded
```

IPv6 example:

```
$ nucli ping-range --start fe80::20c:29ff:fe7a:bcf3 --end fe80::20c:29ff:fe7a:bcf5 --iface ens33
fe80::20c:29ff:fe7a:bcf3 responded
fe80::20c:29ff:fe7a:bcf4 failed to respond
fe80::20c:29ff:fe7a:bcf5 failed to respond
```
