from sys import exit
from time import sleep
from math import floor
#import matplotlib.pyplot as plt
import numpy as np
import serial
import serial.tools.list_ports

from ArduinoSerial import Arduino
from MSP import MultiWii

""" Placa """
arduino= Arduino()
drone_board = MultiWii()
#Evita el desborde de input

""" Variables """

def REPL():
	while True:
		try:
			print(eval(input("Python >")))
		except Exception as e:
			print(str(e))
def initialize(portArduino, portMSP):
	try:
		arduino.connect(portArduino,115200)
		drone_board.connect(portMSP,115200)

		arduino.recv_until(b"ready\r\n")
	except Exception as e:
		print(str(e))
		exit(1)
def main():
	print('Search...')
	ports = serial.tools.list_ports.comports(include_links=False)
	for port in ports:
		print('Puerto disponible: '+port.device)
	initialize(input("Puerto arduino: "), input("Puerto MSP: "))
	#REPL
	REPL()
	# if(test1()):
	# 	print("SUCCESS")
		# data = np.load("log-test1.npy")
		# coefficient = np.mean([y/x for x in data[:,1] for y in data[:,0]])
		# print("Coefficient is: {}".format())
		# # m = y/x
		# # coeff = thrust/current
		# linear_interpretation_step = np.arange(0.0,np.max(data[:,1]),0.1)
		# linear_interpretation = [x*coefficient for x in linear_interpretation_step]
		# plt.plot(data[:,0],data[:,1])
		# plt.plot(linear_interpretation_step,linear_interpretation)
		# plt.show()

def test1(stepTime=1.0,step=20.0):
	if(stepTime < 0.3):
		print("Too Fast")
		return False
	ITERS = floor(1000/step)
	print("TEST WILL TAKE {} TIME WITH MOTOR OPERATING, BE CAREFUL.".format(ITERS*stepTime))
	data = np.empty([ITERS,2],dtype=np.half)
	for iteration in range(ITERS):
		try:
			motorSet(2,1000+(step*iteration))
			sleep(stepTime/2.0)
			data[iteration] = query()
			print("{}: {}".format(iteration+1,data[iteration]))
			sleep(stepTime/2.0)
		except (Exception,KeyboardInterrupt):
			print(str(e))
			print("QUITING SAFELY")
			drone_board.setMotors([1000,1000,1000,1000,0,0,0,0])
			drone_board.disconnect()
			arduino.disconnect()
			return False
	print("QUITING BOARD SAFELY")
	drone_board.setMotors([1000,1000,1000,1000,0,0,0,0])
	drone_board.disconnect()
	arduino.disconnect()
	np.save("log-test1",data)
	return True
	
def query():
	"""
	returns pair (thrust, current)
	"""
	received = arduino.sendString('q').decode('ascii').rstrip().split(',')
	thrust,current = map(float,received)
	return (thrust,current)
def motorSet(motor_number,val):
	arr = [1000,1000,1000,1000,0,0,0,0]
	arr[motor_number-1] = floor(val)
	drone_board.setMotors(arr)
	
if __name__ == "__main__":
	main()
