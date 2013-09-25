#!/usr/bin/env python3

import ctypes,sys
from ctypes.util import find_library
from pcap_struct import *
from pcap_func import *

errbuf = ctypes.create_string_buffer(256)
dev = pcap_lookupdev(errbuf)
net = ctypes.c_uint32()
mask = ctypes.c_uint32()
to_ms = ctypes.c_int(1000)
snaplen = ctypes.c_int(1518)
promisc = ctypes.c_int(1)

num_packets = 5;

if(dev):
    print("{0} is the default interface".format(dev))
else:
    print("Was not able to find default interface")
dev = b'en1'
    
if(pcap_lookupnet(dev,ctypes.addressof(net),ctypes.addressof(mask),errbuf)<0):
    print("could not get netmask for device {0}".format(errbuf.value))
    net = 0
    mask = 0
else:
    print("Got Required netmask")

    
print("Device {0}".format(dev))
print("Number of packets {0}".format(num_packets))


handle = pcap_open_live(dev,snaplen,promisc,to_ms,errbuf)
if(handle is False):
    print("Couldnt open device {0}: {1}\n".format(dev,errbuff))
    sys.exit(1)

pcap_loop(handle, num_packets, got_packet, 0);


pcap_close(handle)

print("Capture complete")