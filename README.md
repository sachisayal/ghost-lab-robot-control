# GHOST Lab Robot Control System

A ROS-based robotics control application developed for experimentation within the GHOST Lab. The system integrates a graphical control interface, motor control functionality, and ultrasonic sensing into separate ROS packages for modular robot operation.

The project was designed to support Raspberry Pi-based robotics experimentation by allowing sensor data, motor commands, and user controls to operate as independent components within a ROS architecture.

## Features

- Graphical user interface for robot control
- ROS-based modular architecture
- Raspberry Pi integration
- Motor control through a dedicated ROS node
- Ultrasonic distance sensing
- Independent sensor, motor, and user-interface components
- ROS launch configuration for ultrasonic sensor operation
- Python-based hardware control
- Support for real-time robot interaction and testing

## System Components

The application is divided into three primary components.

### GHOST Lab UI

The `ghost_lab_ui` package contains the graphical control interface used to interact with the robot.

Primary file:

```text
ghost_lab_ui/src/gui_control_panel.py
