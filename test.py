import robot as temi
from interface import CommandInterface

temi_serial = '01234'

print('test')
mqtt = CommandInterface()
mqtt.connect()

robot = temi.Robot(mqtt, temi_serial)

robot.speak("Hello", "en");
robot.goto("whiteboard")
robot.call("man")

