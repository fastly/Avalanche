# Avalanche

Avalanche is a script that injects random, repeatable network faults on specific ports. It is useful for testing distributed systems.

## Running

    sudo ./avalanche

## Possible Faults:

By default, Avalanche inserts a fault with probability specified in settings.py (p_fault). Given that a fault is inserted, one of the following faults is picked with the probability specified in the config file:

- High latency
- 100% packet loss
- Smaller percentage of packet loss
- Reorder packets
