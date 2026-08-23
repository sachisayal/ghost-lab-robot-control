#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Range
import tkinter as tk

class RobotControlUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ghost Lab Robot Control")
        self.distance = tk.StringVar()
        self.distance.set("Distance: -- cm")

        self.label = tk.Label(master, textvariable=self.distance, font=("Helvetica", 16))
        self.label.pack(pady=10)

        tk.Button(master, text="Move Forward", command=self.move_forward).pack(fill='x')
        tk.Button(master, text="Turn Right", command=self.turn_right).pack(fill='x')
        tk.Button(master, text="Stop", command=self.stop).pack(fill='x')
        tk.Button(master, text="Return to Auto Mode", command=self.set_auto).pack(fill='x')

        self.pub = rospy.Publisher("manual_motor_command", String, queue_size=10)
        rospy.Subscriber("ultrasonic_distance", Range, self.update_distance)

    def update_distance(self, msg):
        self.distance.set(f"Distance: {msg.range:.2f} cm")

    def move_forward(self):
        self.pub.publish("forward")

    def turn_right(self):
        self.pub.publish("right")

    def stop(self):
        self.pub.publish("stop")

    def set_auto(self):
        self.pub.publish("auto")

if __name__ == '__main__':
    rospy.init_node("robot_gui", anonymous=True)
    root = tk.Tk()
    app = RobotControlUI(root)
    root.mainloop()
