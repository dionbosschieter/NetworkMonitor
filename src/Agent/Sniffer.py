#! /usr/bin/env python3
import sys
import pcap
import time
import socket
import struct
import pymysql
import Protocol
from multiprocessing import Process
from rpyc.utils.server import ThreadedServer

protocollen = Protocol.protocollen
protocols= Protocol.protocols

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='woensdag25!', db='networkmonitor')
cur = conn.cursor()


if sys.version_info[0] > 2:
    IPPROTO = bytes ((0x08, 0x00))
    bord = int
else:
    IPPROTO = '\x08\x00'
    bord = ord
    
def decode_ip_packet(s):
    d={}

    d['version']=(bord(s[0]) & 0xf0) >> 4
    d['header_len']=bord(s[0]) & 0x0f
    d['tos']=bord(s[1])
    d['total_len']=socket.ntohs(struct.unpack('H',s[2:4])[0])
    d['id']=socket.ntohs(struct.unpack('H',s[4:6])[0])
    d['flags']=(bord(s[6]) & 0xe0) >> 5
    d['fragment_offset']=socket.ntohs(struct.unpack('H',s[6:8])[0] & 0x1f)
    d['ttl']=bord(s[8])
    d['protocol']=bord(s[9])
    d['checksum']=socket.ntohs(struct.unpack('H',s[10:12])[0])
    d['source_address']=pcap.ntoa(struct.unpack('i',s[12:16])[0])
    d['destination_address']=pcap.ntoa(struct.unpack('i',s[16:20])[0])
    if d['header_len']>5:
        d['options']=s[20:4*(d['header_len']-5)]
    else:
        d['options']=None
    d['data']=s[4*d['header_len']:]
    d['srcportnum'] = int(socket.ntohs(struct.unpack('H',d['data'][0:2])[0]))	  
    d['dstportnum'] = int(socket.ntohs(struct.unpack('H',d['data'][2:4])[0]))

    return d

def print_packet(pktlen, data, timestamp):
    if not data:
        return

    if data[12:14]==IPPROTO:
        decoded=decode_ip_packet(data[14:])
        type = ""
        if decoded['srcportnum'] in protocollen:
            type = protocollen[decoded['srcportnum']]

        if decoded['dstportnum'] in protocollen:
            type = protocollen[decoded['dstportnum']]

        """print ('%s.%f %s > %s %s %s %s %s' % (time.strftime('%H:%M',
                                time.localtime(timestamp)),
                                timestamp % 60,
                                decoded['source_address'],
                                decoded['destination_address'],
                                decoded['srcportnum'],
                                decoded['dstportnum'],
                                protocols[decoded['protocol']],
                                type))
        """
        
        query = "INSERT INTO packets (version,header_len,tos,total_len,ttl,protocol,src_port,dst_port,src_ip,dst_ip)"
        query+= " VALUES ("
        query+= str(decoded['version'])+","
        query+= str(decoded['header_len'])+","
        query+= str(decoded['tos'])+","
        query+= str(decoded['total_len'])+","
        query+= str(decoded['ttl'])+",'"

        if type: query+= type+"',"
        else: query+= protocols[decoded['protocol']]+"',"
        
        query+= str(decoded['srcportnum'])+","
        query+= str(decoded['dstportnum'])+",'"
        query+= decoded['source_address']+"','"
        query+= decoded['destination_address']+ "')"

        cur.execute(query)
        conn.commit()

def StartSniffer():
    p = pcap.pcapObject()
    dev = "eth0"
    net, mask = pcap.lookupnet(dev)
    
    p.open_live(dev, 1600, 0, 200)
    
    try:
        while 1:
            p.dispatch(1, print_packet)

    except KeyboardInterrupt:
        print ('%s' % sys.exc_type)
        print ('shutting down')
        cur.close()
        conn.close()
        sys.exit(1)

if __name__=='__main__':
    Process(target = StartSniffer).start()
    #ThreadedServer(Server, port = 18861).start()