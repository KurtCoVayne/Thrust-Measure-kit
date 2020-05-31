from serial import Serial
from threading import Thread, Event
from time import sleep, time
class Arduino(object):
	def __init__(self):
		self._serial = Serial()

	# def __del__(self):
	# 	if self._monitorThread.isAlive():
	# 		self._exitNow.set()
	# 	elif self._serial.isOpen():
	# 		self._serial.close()

# connection methods #################################################################################
	def disconnect(self):
		self._serial.close()

	def connect(self, portName, baudRate):
		"""Connect to Arduino

		Args:
			portName (str): The serial port name to use for the connection (e.g., "COM3" in Windows or "/dev/ttyUSB0", "/dev/TTYAMA0", etc. in Linux)
			baudRate (int): The communications speed (generally 115200 for CleanFlight)

		Returns:
			bool: True if successful, False otherwise
		"""
		self._serial.port = portName
		self._serial.baudrate = baudRate
		self._serial.open()
		return self._serial.is_open
	
	def sendString(self,s:str):
		self._serial.write(bytes(s,'ascii'))
		return self._serial.readline()

	def recv_until(self,s:str):
		r = self._serial.readline()
		while not r == s:
			r = self._serial.readline()