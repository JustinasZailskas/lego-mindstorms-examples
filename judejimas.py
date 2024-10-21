#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, 
    InfraredSensor, UltrasonicSensor, GyroSensor
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Objektų kūrimo vieta.
ev3 = EV3Brick()

# Inicijuojami motorai.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Inicijuojama roboto važiuoklė.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Programos pagrindinė dalis.
robot.straight(100)
ev3.speaker.beep()
robot.turn(90)
