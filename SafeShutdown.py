import RPi.GPIO as GPIO
import os
import requests
import time
from multiprocessing import Process
import subprocess


#initialize pins
powerPin = 3 #pin 5
ledPin = 14 #TXD
resetPin = 2 #pin 13
powerenPin = 4 #pin 5

#initialize GPIO settings
def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(powerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(resetPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, GPIO.HIGH)
	GPIO.setup(powerenPin, GPIO.OUT)
	GPIO.output(powerenPin, GPIO.HIGH)
	GPIO.setwarnings(False)

def api_request(command : str):
	supervisor_address = os.environ.get('BALENA_SUPERVISOR_ADDRESS')
	supervisor_api_key = os.environ.get('BALENA_SUPERVISOR_API_KEY')
	uri = '{address}/v1/{cmd}?apikey={key}'
	uri = uri.format(address=supervisor_address, cmd=command, key=supervisor_api_key)
	headers = {'Content-Type': 'application/json'}
	requests.post(uri, headers=headers)

def request_halt():
	print('System halt')
	api_request('halt')

def request_reboot():
	print('System reboot')
	api_request('reboot')

def request_shutdown():
	print('System shutdown')
	api_request('shutdown')


#waits for user to hold button up to 1 second before issuing poweroff command
def poweroff():
	while True:
		GPIO.wait_for_edge(powerPin, GPIO.FALLING)
		request_shutdown()

#blinks the LED to signal button being pushed
def ledBlink():
	while True:
		GPIO.output(ledPin, GPIO.HIGH)
		GPIO.wait_for_edge(powerPin, GPIO.FALLING)
		start = time.time()
		while GPIO.input(powerPin) == GPIO.LOW:
			GPIO.output(ledPin, GPIO.LOW)
			time.sleep(0.2)
			GPIO.output(ledPin, GPIO.HIGH)
			time.sleep(0.2)

#resets the pi
def reset():
	while True:
		#self.assertEqual(GPIO.input(resetPin), GPIO.LOW)
		GPIO.wait_for_edge(resetPin, GPIO.FALLING)
		request_reboot()


if __name__ == "__main__":
	#initialize GPIO settings
	init()
	#create a multiprocessing.Process instance for each function to enable parallelism 
	powerProcess = Process(target = poweroff)
	powerProcess.start()
	ledProcess = Process(target = ledBlink)
	ledProcess.start()
	resetProcess = Process(target = reset)
	resetProcess.start()

	powerProcess.join()
	ledProcess.join()
	resetProcess.join()

	GPIO.cleanup()
