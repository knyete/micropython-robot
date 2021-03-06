#!/usr/bin/env python3

"""
ver 0.7.9.95 robot modelled in objects. Introducing him here.
"""

# import logging

from gingermicrorobot import GingerMicroRobot as Ginger
from dcdrive import DCDrive as DCDrive
from servomotor import ServoMotor as Servo
from hallsensordigital import HallSensorDigital as Hall
from led import Led as Led


def main():
    # Ginger robot pin out
    # servo_direction = machine.PWM(machine.Pin(12), freq=50)
    # servo_head_x = machine.PWM(machine.Pin(14), freq=50)
    # servo_hand_y = machine.PWM(machine.Pin(13), freq=50)
    # servo_catch = machine.PWM(machine.Pin(15), freq=50)

    ginger = Ginger(
        motor=DCDrive(
            name='motor',
            letter='A'
        ),
        servo_direction=Servo(
            name='servo_dir',
            pin=12
        ),
        servo_head_x=Servo(
            name='servo_head_x',
            pin=14
        ),
        servo_hand_y=Servo(
            name='servo_hand_y',
            pin=13
        ),
        servo_catch=Servo(
            name='servo_catch',
            pin=15
        ),
        sensor_hall=Hall(
            pin=4
        ),
        led=Led(
            name='led',
            pin=2,
        )

    )

    # print(ginger)
    # print(dir(ginger.motor))
    # print(ginger.motor.echo())
    # print(ginger.motor.echo(71))
    # print(ginger.motor.duty(71))
    # print(ginger.motor.echo('string71'))
    #
    # print(ginger.servo_catch.echo())
    # print(ginger.servo_catch.echo(72))
    # print(ginger.servo_catch.duty(72))
    # print(ginger.servo_catch.echo('string 72'))
    # print(ginger.servo_catch.duty('string 72'))  # duty should be int or float
    # print(ginger.sensor_hall.sensor)
    # print(ginger.led.light)
    print('--test--')

    # for i in range(50):
    while True:
        if ginger.sensor_hall.hall() == 0:
            ginger.led.light = 0
        else:
            ginger.led.light = 1

        print('sensor:{}, light:{}'.format(
            ginger.sensor_hall.sensor,
            ginger.led.light
        ))


if __name__ == "__main__":
    print(
        'Here I am'
    )

    main()
