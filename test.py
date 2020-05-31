from MSP import MultiWii
from time import sleep
from sys import exit
import serial.tools.list_ports
if __name__ == "__main__":
	print('Search...')
	ports = serial.tools.list_ports.comports(include_links=False)
	for port in ports:
		print('Puerto disponible: '+port.device)
	board = MultiWii()
	try:
		board.connect(input("Puerto /dev/ttyUSB0 o COM del drone "),115200)
	except Exception as e:
		print(str(e))
		pass
	while True:
		try:
			# print("Altitud del drone",board.getAltitude())
			print('Información de los sensores GY;IMU: ',board.getIMU())
			# print(eval(input("REPL: ")))
			# print('Información de los motores: ',board.getMotors())
			# print("\n")
			sleep(0.1)
		except KeyboardInterrupt:
			# quit
			print("QUITING SAFELY")
			board.disconnect()
			exit(0)
		

	# board.setMotors([1500,1500,1500,1500,0,0,0,0])
	# sleep(1)
	# board.setMotors([1000,1000,1000,1000,0,0,0,0])

	board.disconnect()
	
