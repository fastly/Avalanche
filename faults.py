import random

class Partition:
    # Partition the current server from all other servers

    def action(self):
        return "netem loss 100%"

    def desc(self):
        return "network partition"

class PacketLoss:
    # Drop packets with some probability

    def __init__(self):
        # percentage probability of dropping a packet
        self.loss = random.randint(5, 10)

    def action(self):
        return "netem loss %d%%"%(self.loss)

    def desc(self):
        return "drop packets with probability %d%%"%(self.loss)

class Latency:
    # Add latency to all packets

    def __init__(self):
        # per-packet delay in ms
        self.latency = random.randint(100, 1000)

    def action(self):
        return "netem delay %dms"%(self.latency)

    def desc(self):
        return "delay of %dms"%(self.latency)

class Reorder:
    # Reorder packets

    def __init__(self):
        # probability of continuing the delay
        self.correlation = 50

        # initial packet delay
        self.delay = 10

        # probability of reordering a packet
        self.reorder = random.randint(10, 75)

    def action(self):
        return "netem delay %sms reorder %d%% %d%%" % (self.delay, 100-self.reorder, self.correlation)

    def desc(self):
        return "reorder after delay of %dms with probability %d and correlation %d" % (self.delay, 100-self.reorder, self.correlation)
