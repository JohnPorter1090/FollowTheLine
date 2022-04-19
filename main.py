#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile






# Create your objects here.
ev3 = EV3Brick()

color_sensor = ColorSensor(Port.S3)
gyro_sensor = GyroSensor(Port.S2)

motorb = Motor(Port.B)
motorc = Motor(Port.C)

robot = DriveBase(motorb, motorc, wheel_diameter=55.5,
axle_track=104)

loop = True

while loop:
    if color_sensor.color() != color.BLACK:
        if color_sensor.color() == color.RED:
            robot.turn(180)
        elif color_sensor.color() != color.BLACK:
            robot.turn(15)
    else:
        robot.straight(10)


