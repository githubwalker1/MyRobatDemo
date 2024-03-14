#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :
# @Author  : ys
# @File    :
# @Software:

from ..sdk import imu,hiwonder_servo_controller
import time
import sys

#读取加速度感应器
def get_imu():
    my_imu = imu.IMU()
    try:
        ax, ay, az, bx, by, bz = get_imu.get_data()
        print(ax, ay, az, bx, by, bz,"\n")
    except Exception as e:
        print(str(e))

#读取总线舵机数据
def get_controller():
    servo_control = hiwonder_servo_controller.HiwonderServoController("/dev/tyTHST", 115200)
    print( "get serial servo status")
    try:
        servo_id = servo_control.get_servo_id()
        pos = servo_control.get_servo_position(servo_id)
        dev = servo_control.get_servo_deviation(servo_id)
        if dev > 125:
            dev = -(0xff - (dev - 1))
        angle_range = servo_control.get_servo_range(servo_id)
        vin_range = servo_control.get_servo_vin_range(servo_id)
        temperature_warn = servo_control.get_servo_temp_range(servo_id)
        temperature = servo_control.get_servo_temp(servo_id)
        vin = servo_control.get_servo_vin(servo_id)
        load_tate = servo_control.get_servo_load_state(servo_id)

        print("id:",servo_id,"\n")
        print("pos:", pos, "\n")
        print("dev:", dev, "\n")
        print("angle_range:", angle_range, "\n")
        print("vin_range:", vin_range, "\n")
        print("temperature_warn:", temperature_warn, "\n")
        print("temperature:", temperature, "\n")
        print("vin:", vin, "\n")
        print("lock:", load_tate, "\n")
        print("\n")
    except Exception as e:
        print(str(e),"\n")




def get_data(step):
    while(step):
        try:
            get_imu()
            get_controller()
        except Exception as e:
            print(str(e))




if __name__ == "__main__":
    get_data(5)
    pass