import socket

protocollen = {21: "FTP",
			 22: "SSH",
			 53 : "DNS",
			 80 : "HTTP" ,
			 443 : "HTTPS"}

protocols={socket.IPPROTO_TCP:'tcp',
            socket.IPPROTO_UDP:'udp',
            socket.IPPROTO_ICMP:'icmp'}