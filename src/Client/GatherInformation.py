import pymysql

class GatherInformation(object):

	def __init__(self, info_container, debug_console, server):
		self.info_container = info_container
		self.debug_console = debug_console
		self.server = server

		debug_console.log("Intializing GatherInformation")

	def connect(self):
		self.debug_console.log("Connecting to: " + self.server)

		self.conn = pymysql.connect(host=self.server, user='root', passwd='woensdag25!', db='networkmonitor')
		self.cur = self.conn.cursor()
		
		self.debug_console.log("Connected to: " + self.server)

	def disconnect(self):
		self.debug_console.log("Disconnecting from: " + self.server)
		self.cur.close()
		self.conn.close()

	def getPackets(self):
		self.debug_console.log("Gathering Packets")
		self.cur.execute("SELECT * FROM packets")

		for row in self.cur:
			self.info_container.addPacket(str(row))
		
		self.debug_console.log("All packets recieved")