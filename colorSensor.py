#!/usr/bin/env pybricks-micropython from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks-parameters import Port, Stop, Direction, Button, Color from pybricks.tools import wait, StopWatch, DataLog from pybricks.robotics import DriveBase from pybricks.media.ev3dev import SoundFile, ImageFile
# Objekty kurimo vieta.
ev3 = EV3Brick()
# Inicijuojami motorai.
left_motor = Motor (Port.B)
right_motor = Motor (Port.C)
# Inicijuojami jutikliai
colorSensor = ColorSensor (Port.S1)
# Inicijuojama roboto vaiuokle.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
#colors
JUODA_SPALVA = 7
STALO_REIKSME = 31
VIDURKIS = (JUDA_SPALVA + STALO_REIKSME) / 2
# Programos pagrindine dalis.
robot.straight (100)
ev3.speaker.beep ()
# robot.turn (90)
# ev3.speaker.beep()
while True:
if colorSensor. reflection() > VIDURKIS:
robot.drive (100,0)
else:
robot.straight (-200)
robot. turn (180)