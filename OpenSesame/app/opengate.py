import atexit
import serial
import config

ARDUINO_PATH = config.ARDUINO_PATH

serialcomm = serial.Serial(ARDUINO_PATH, 9600)
serialcomm.timeout = 1


def openGate():
    serialcomm.write("open".encode())


def closeGate():
    serialcomm.write("close".encode())


@atexit.register
def closeSerial():
    serialcomm.close()
