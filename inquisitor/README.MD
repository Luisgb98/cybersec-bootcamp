Project made with [@cherrero42](https://github.com/cherrero42).

## What this program does?
This program simulates a [ARP spoofing](https://en.wikipedia.org/wiki/ARP_spoofing). Using Docker, it creates a network with 3 containers: 1 router and 2 hosts. The router is the gateway of the hosts. The hosts are connected to the router and can communicate with each other. The router is also connected to the internet. The hosts can access the internet through the router. The router is also connected to the attacker. The attacker can sniff or modify the traffic between the hosts and the router.

## Characteristics:
- Will receive four parameters: `<IP-src> <MAC-src> <IP-target> <MAC-target>`.
- Will be able to perform `ARP` poisoning in both directions (full duplex).
- When the attack is stopped `CTRL+C`, the `ARP` tables will be restored.
- Will only work with `IPv4` addresses.
- The program will be able to intercept the traffic resulting from the login to an `FTP` server.
- The names of the files exchanged between the client and the `FTP` server will be displayed in real time.
- The program will never stop unexpectedly and will handle all input errors.
- Use of `libcap` library to sniff packets.
- `Dockerfile` and `docker-compose.yml` to create the network with a `bash script` called `start.sh` to start the environment.

## Bonus part:
- `-v, --verbose` mode that shows all `FTP` traffic and not just filenames.

## ARP Spoofing:
To perform an `ARP` poisoning in both directions, I used `scapy` library to help me build the packets. The program will send `ARP` packets to the target and the source. The target will think that the attacker is the source and the source will think that the attacker is the target. The attacker will be able to sniff and modify the traffic between the target and the source.

## Sniffing:
To sniff the traffic, I used an extension of `libpcap` library in python, `pcapy`. The program will sniff the traffic between the target and the source. The program will be able to intercept the traffic resulting from the login to an `FTP` server. The names of the files exchanged between the client and the `FTP` server will be displayed in real time. If `verbose` mode is activated, the program will show all `FTP` traffic and not just filenames.

## Restoring ARP tables:
When the attack is stopped `CTRL+C`, the `ARP` tables will be restored. I also implemented a `signal handler` to restore the `ARP` tables when a file with `end` name is created.

## How to use it?
First, you need to run the `start.sh` script to create the network. Then, you need to move `inquisitor.py` to `src` directory created on `env` directory. Run the script with the four parameters: `<IP-src> <MAC-src> <IP-target> <MAC-target>`. You can also use the `-v` or `--verbose` option to show all `FTP` traffic and not just filenames. To test the program, go to `localhost:5800` on your browser and use the `FTP` server and connect to the server, all the traffic will be sniffed and will be displayed in real time. To stop the program, press `CTRL+C` and the `ARP` tables will be restored. You can also create a file with `end` name to restore the `ARP` tables.

I also added an optional argument `-ma, --mac-attack` to filter the traffic between the target and the source.

```bash
python3 inquisitor.py -ip <IP-src> -ms <MAC-src> -ip <IP-target> -mt <MAC-target> [-ma, --mac-attack] [-v, --verbose]
```