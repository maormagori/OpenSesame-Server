from os import environ as env
from dotenv import load_dotenv


# Statement for enabling the development environment
DEBUG = True if env.get('ENV', 'DEVELOPMENT') == 'DEVELOPMENT' else False

# The Arduino path on my machine.
ARDUINO_PATH = env.get('ARDUINO_PATH', '/dev/ttyACM0')

FIREBASE_PROJECT_ID = env.get('FIREBASE_PROJECT_ID')
