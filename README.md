NetworkMonitor
==============

NetworkMonitor for Unix Network Programming in Python


This is a network monitor which is developed with Python3.

The agent can run on every computer with python3 installed. For example we've tested it on a Raspberry Pi. 

The agent captures all the packets on eth0. You can edit the network interface. All the packet data is putted in a mysql database. 

The client can also run on every computer with python3 installed. It connect's to the mysql database and reads the packets. 

We've used the following libaries:

Cursus: To make the client user interface
PyMySQL: Mysql client for python
PyLibPcap-0.6.4: To sniff the packets