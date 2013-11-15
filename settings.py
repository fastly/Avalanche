import logging
from faults import *

# Seed for the random number generator. This makes tests repeatable.
seed = 1

# Time between faults in seconds
delay = 1

# Probability of a fault occuring.
p_fault = 0.5

# if debug is true, log which fault we would do, but don't inject the fault.
debug = False

# only inject faults on these interfaces
interfaces = ["eth0"]

# only inject faults on these  ports
ports = [2001]

# level of logging
log_level = logging.INFO

# List of faults to execute. If it's a list, the probability of each fault
# is uniform. If it's a hash the probability of each fault is the hash value.
faults = {
    Partition: 0.2,
    PacketLoss: 0.2,
    Latency: 0.3,
    Reorder: 0.3,
}
