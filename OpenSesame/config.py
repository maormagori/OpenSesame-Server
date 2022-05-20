from os import environ as env

# Statement for enabling the development environment
DEBUG = True if env.get('ENV', 'DEVELOPMENT') == 'DEVELOPMENT' else False

# The Arduino path on my machine.
ARDUINO_PATH = env.get('ARDUINO_PATH', '/dev/ttyACM0')
