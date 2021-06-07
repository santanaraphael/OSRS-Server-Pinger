"""
Walid Sodki
Python 3.5
OSRS-Server-Pinger
MIT License
"""

import os  # os is used for the ping

import ping3

f2p_list = [
    1,
    8,
    16,
    26,
    35,
    81,
    82,
    83,
    84,
    85,
    93,
    94,
    97,
    98,
    99,
    113,
    114,
    117,
    118,
    119,
    124,
    125,
    126,
    127,
    130,
    131,
    132,
    133,
    134,
    135,
    136,
    137,
    138,
    139,
    140,
    141,
    151,
    152,
    153,
    154,
    155,
    156,
    157,
    158,
    159,
    160,
    168,
    169,
    170,
    171,
    172,
    173,
    174,
    175,
    176,
    177,
    178,
    179,
    197,
    198,
    199,
    200,
    201,
    202,
    203,
    204,
    205,
    206,
]  # list of all the F2P servers


def format_server_ping(server, ping):
    return "{0}: {1:.2f}ms".format(server, ping)


def print_server_list(server_list, message="Best 5 pings:"):
    print(f"\n{message}")
    print(
        "\n".join(
            [
                format_server_ping(entry["world"], entry["ping"])
                for entry in sorted(server_list, key=lambda entry: entry["ping"])[:5]
            ]
        )
    )


def servers():
    servers = []
    p2p_servers = p2p(print_final_list=False)
    f2p_servers = f2p(print_final_list=False)

    servers.extend(p2p_servers)
    servers.extend(f2p_servers)

    print_server_list(servers)
    print_server_list(p2p_servers, message="Best 5 p2p pings:")
    print_server_list(f2p_servers, message="Best 5 f2p pings:")


def p2p(print_final_list=True):
    p2p_servers = []
    for i in range(1, 206):  # server 1 is F2P and can be skipped in the range
        if (
            i in f2p_list
        ):  # if a server is part of the F2P list then skip it with continue
            continue
        world = "oldschool" + str(i) + ".runescape.com"
        ping = ping3.ping(world, unit="ms") or 9999
        print(format_server_ping(world, ping))
        p2p_servers.append({"world": world, "ping": ping})

    if print_final_list:
        print_server_list(p2p_servers, message="Best 5 p2p pings:")

    return p2p_servers


def f2p(print_final_list=True):
    f2p_servers = []
    for i in f2p_list:
        world = "oldschool" + str(i) + ".runescape.com"
        ping = ping3.ping(world, unit="ms") or 9999
        print(format_server_ping(world, ping))
        f2p_servers.append({"world": world, "ping": ping})

    if print_final_list:
        print_server_list(f2p_servers, message="Best 5 f2p pings:")

    return f2p_servers


def specificServer(serverType):
    world = "oldschool" + str(serverType) + ".runescape.com"
    ping = ping3.ping(world, unit="ms") or 9999
    print(format_server_ping(world, ping))


def start():  # take input from user to what filter for the pinging should be used

    serverType = input(
        "Do you want to ping ALL servers, Memebers only or Free to Play only? \nYou can also ping a specific world by typing in the number (eg. 2 for world 2)\n"
    ).lower()
    if serverType.isdigit():
        return specificServer(serverType)

    if any(p2p_value in serverType for p2p_value in ["mem", "p2p", "pay"]):
        print("Only members (P2P) servers will be pinged.")
        return p2p()
    if "f" in serverType:
        print("Free to play (F2P) servers will now be pinged.")
        return f2p()

    print("All servers will now be pinged.")
    return servers()


print("Oldschool Runescape Server Pinger v0.1")
print("By Walid Sodki \n")
start()
print("\n*** Ping process is now done. ***")
