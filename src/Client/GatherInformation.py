import pymysql

class GatherInformation(object):

	def __init__(self, info_container, debug_console, server):
		self.info_container = info_container
		self.debug_console = debug_console
		self.server = server

		debug_console.log("Intializing GatherInformation")
		self.connected = False
		
		self.packetdescription = ["ver",
			"header_len","tos","length",
			"ttl","type","src_port",
			"dst_port","src_ip","dst_ip"]

	def toggleconnect(self):
		if(self.connected):
			self.disconnect()
		else:
			self.connect()

	def connect(self):
		self.debug_console.log("Connecting to: " + self.server)

		#change these values
		self.conn = pymysql.connect(host=self.server, user='root', passwd='woensdag25!', db='networkmonitor')
		self.cur = self.conn.cursor()
		
		self.debug_console.log("Connected to: " + self.server)

		self.connected = True

	def disconnect(self):
		self.debug_console.log("Disconnecting from: " + self.server)
		self.cur.close()
		self.conn.close()
		self.connected = False

	def getPackets(self):
		if(self.connected):
			self.debug_console.log("Gathering Packets")
			self.cur.execute("SELECT * FROM packets")

			for row in self.cur:
				packet = ""#+str(row[0])
				packet += " Date: " + str(row[1])
				for i in range(0, len(self.packetdescription)):
					packet+= " " + self.packetdescription[i] + ": " + str(row[i+2])
				self.info_container.addPacket(packet)
			
			self.debug_console.log("All packets recieved")
		else: 
			self.debug_console.log("Cant get new packets, not connected")