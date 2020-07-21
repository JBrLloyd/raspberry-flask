from time import sleep
import RPi.GPIO as GPIO
from flask import Blueprint, request


api_blueprint = Blueprint('api', __name__)


def cyclePin(pin_num):
  GPIO.output(pin_num, True)
  sleep(0.25)
  GPIO.output(pin_num, False)


def cyclePins(pin1, pin2, num_cycles):
  for i in range(0, num_cycles):
    cyclePin(pin1)
    cyclePin(pin2)


def turnOnLed(num_of_cycles):
  GPIO.setmode(GPIO.BCM)

  red_led = 24
  GPIO.setup(red_led, GPIO.OUT)
  blue_led = 21
  GPIO.setup(blue_led, GPIO.OUT)

  # print(f'Setting GPIO pin {pin_out} to output')

  try:
    print(f'Turning GPIO pins on!')
    cyclePins(red_led, blue_led, num_of_cycles)
  except:
    print("Exception occurred!")
  finally:
    GPIO.cleanup()
    print("Script finished executing...")


@api_blueprint.route('/api/lightsOn', methods=['POST'])
def lightsOn():
  if request.json and 'cycles' in request.json:
    turnOnLed(request.json['cycles'])
  return "success"
