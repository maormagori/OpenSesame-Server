import atexit
import serial
from app import app
config = app.config
ARDUINO_PATH = config['ARDUINO_PATH']

serialcomm = serial.Serial(ARDUINO_PATH, 9600)
serialcomm.timeout = 1

# TODO: Rename functions to match python names


def openGate():
    serialcomm.write("open".encode())


def closeGate():
    serialcomm.write("close".encode())


@atexit.register
def closeSerial():
    serialcomm.close()
