#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Range
import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    pulse_start = time.time()
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

def sensor_node():
    rospy.init_node('ultrasonic_sensor', anonymous=True)
    pub = rospy.Publisher('ultrasonic_distance', Range, queue_size=10)
    rate = rospy.Rate(10)

    sensor_msg = Range()
    sensor_msg.header.frame_id = 'ultrasonic_frame'
    sensor_msg.field_of_view = 0.5
    sensor_msg.min_range = 2.0
    sensor_msg.max_range = 400.0

    try:
        while not rospy.is_shutdown():
            distance = get_distance()
            sensor_msg.range = distance
            sensor_msg.header.stamp = rospy.Time.now()
            pub.publish(sensor_msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    sensor_node()
