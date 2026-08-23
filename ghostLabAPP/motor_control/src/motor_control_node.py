#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Range
from std_msgs.msg import String
import RPi.GPIO as GPIO

MOTOR_LEFT_FORWARD = 17
MOTOR_LEFT_BACKWARD = 27
MOTOR_RIGHT_FORWARD = 22
MOTOR_RIGHT_BACKWARD = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_LEFT_FORWARD, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_BACKWARD, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_FORWARD, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_BACKWARD, GPIO.OUT)

manual_override = False

def move_forward():
    GPIO.output(MOTOR_LEFT_FORWARD, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.LOW)

def turn_right():
    GPIO.output(MOTOR_LEFT_FORWARD, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.HIGH)

def stop():
    GPIO.output(MOTOR_LEFT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_LEFT_BACKWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_FORWARD, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT_BACKWARD, GPIO.LOW)

def motor_callback(msg):
    if manual_override:
        return
    distance = msg.range
    if distance < 20.0:
        rospy.loginfo("Obstacle detected, turning right!")
        stop()
        rospy.sleep(1)
        turn_right()
        rospy.sleep(1)
    else:
        rospy.loginfo("Clear path, moving forward!")
        move_forward()

def manual_command_callback(msg):
    global manual_override
    manual_override = True
    cmd = msg.data
    rospy.loginfo(f"Manual Command: {cmd}")
    if cmd == "forward":
        move_forward()
    elif cmd == "right":
        turn_right()
    elif cmd == "stop":
        stop()
    elif cmd == "auto":
        manual_override = False
        stop()

def motor_node():
    rospy.init_node('motor_controller', anonymous=True)
    rospy.Subscriber('ultrasonic_distance', Range, motor_callback)
    rospy.Subscriber('manual_motor_command', String, manual_command_callback)
    rospy.spin()
    GPIO.cleanup()

if __name__ == "__main__":
    motor_node()
