# GHOST Lab Robot Control System

A ROS-based robotics application developed for research and experimentation within the **GHOST Lab**. The project integrates a graphical user interface, motor control, and ultrasonic distance sensing into separate software components for modular robot interaction and hardware control.

The system was developed using **Python, ROS, Raspberry Pi hardware, GPIO-based sensing and control, and CMake-based package configuration**.

This repository serves as an archive of the implementation developed during GHOST Lab research and preserves the original robot-control, sensing, and user-interface components.

---

## Project Overview

The GHOST Lab Robot Control System was designed to connect three primary components of a robotics platform:

1. A **graphical control interface** for interacting with the robot
2. A **motor control node** for controlling robot movement
3. An **ultrasonic sensor node** for collecting environmental distance measurements

Each component is separated into its own package or module so that sensing, actuation, and user interaction can be developed and tested independently.

The modular architecture also provides a foundation for future robotics capabilities such as autonomous navigation, obstacle detection, sensor fusion, and higher-level robot control.

---

## Key Features

- ROS-based modular robotics architecture
- Python-based robot control
- Raspberry Pi hardware integration
- Graphical robot control interface
- Dedicated motor-control functionality
- Ultrasonic distance sensing
- GPIO-based hardware interaction
- ROS launch configuration
- Independent sensing, control, and interface components
- Real-time robot interaction
- Modular design for future robotics expansion

---

## System Architecture

The application separates user interaction, robot movement, and environmental sensing into individual components.

```text
                    ┌──────────────────────────┐
                    │    GUI Control Panel     │
                    │ gui_control_panel.py     │
                    └────────────┬─────────────┘
                                 │
                                 │
                                 ▼
                       ROS Communication
                                 │
                  ┌──────────────┴──────────────┐
                  │                             │
                  ▼                             ▼
        ┌───────────────────┐         ┌──────────────────────┐
        │   Motor Control   │         │  Ultrasonic Sensor   │
        │                   │         │                      │
        │ motor_control_    │         │ ultrasonic_sensor_   │
        │ node.py           │         │ node.py              │
        └─────────┬─────────┘         └──────────┬───────────┘
                  │                              │
                  ▼                              ▼
              Robot Motors               Distance Measurements
```

This separation makes the system easier to debug, test, modify, and extend.

---

# Project Components

## 1. GHOST Lab User Interface

The `ghost_lab_ui` component contains the graphical interface used to interact with the robot.

### Primary File

```text
ghost_lab_ui/src/gui_control_panel.py
```

The control panel acts as the user-facing component of the system and provides a centralized interface for robot interaction.

### Responsibilities

- Provide graphical controls for robot operation
- Translate user actions into robot-control commands
- Provide a centralized interface for interacting with hardware functionality
- Support manual testing of robot behavior

---

## 2. Motor Control

The `motor_control` component contains the robot motor-control logic.

### Primary File

```text
motor_control/src/motor_control_node.py
```

The motor-control node is responsible for translating software commands into motor behavior.

### Responsibilities

- Receive movement/control commands
- Manage robot motor behavior
- Interface software commands with physical robot movement
- Support independent testing of motor-control functionality

---

## 3. Ultrasonic Sensor

The `ultrasonic_sensor` package handles environmental distance sensing.

### Primary Files

```text
ultrasonic_sensor/src/ultrasonic_sensor_node.py
ultrasonic_sensor/launch/ultrasonic_sensor.launch
ultrasonic_sensor/package.xml
ultrasonic_sensor/CMakeLists.txt
```

The ultrasonic sensor node collects distance measurements from the connected ultrasonic sensor.

These measurements can be used to give the robot basic awareness of nearby objects and provide a foundation for obstacle detection or autonomous movement.

### Responsibilities

- Interface with ultrasonic sensing hardware
- Collect distance measurements
- Process sensor readings
- Make sensor information available to the robotics system
- Support future obstacle-detection functionality

---

# Repository Structure

```text
ghost-lab-robot-control/
│
├── ghost_lab_ui/
│   ├── CMakeLists.txt
│   └── src/
│       └── gui_control_panel.py
│
├── motor_control/
│   ├── CMakeLists.txt
│   └── src/
│       └── motor_control_node.py
│
├── ultrasonic_sensor/
│   ├── CMakeLists.txt
│   ├── package.xml
│   │
│   ├── launch/
│   │   └── ultrasonic_sensor.launch
│   │
│   └── src/
│       └── ultrasonic_sensor_node.py
│
├── .gitignore
└── README.md
```

---

# File Descriptions

## `gui_control_panel.py`

Contains the graphical interface used to interact with the robot-control system.

```text
ghost_lab_ui/src/gui_control_panel.py
```

This component provides the user-facing portion of the application and connects manual user input with robot functionality.

---

## `motor_control_node.py`

Contains the logic responsible for controlling the robot's motors.

```text
motor_control/src/motor_control_node.py
```

This component handles the movement portion of the system and connects software commands with physical robot actuation.

---

## `ultrasonic_sensor_node.py`

Contains the Python logic used to interface with the ultrasonic sensor.

```text
ultrasonic_sensor/src/ultrasonic_sensor_node.py
```

The node collects distance measurements that can be used by other components of the robotics system.

---

## `ultrasonic_sensor.launch`

ROS launch configuration for the ultrasonic sensor component.

```text
ultrasonic_sensor/launch/ultrasonic_sensor.launch
```

The launch file simplifies starting the ultrasonic sensing functionality within the ROS environment.

---

## `package.xml`

Contains package metadata and dependency information for the ultrasonic sensor ROS package.

```text
ultrasonic_sensor/package.xml
```

---

## `CMakeLists.txt`

Each project component contains a `CMakeLists.txt` file used for ROS/CMake package configuration.

Current locations include:

```text
ghost_lab_ui/CMakeLists.txt
motor_control/CMakeLists.txt
ultrasonic_sensor/CMakeLists.txt
```

---

# Technologies

## Programming

- Python

## Robotics

- ROS
- Robotics middleware
- ROS nodes
- ROS launch files

## Hardware

- Raspberry Pi
- GPIO
- Ultrasonic sensor
- Motor-control hardware

## Development

- Linux
- CMake
- Git
- GitHub

## Concepts

- Robotics software development
- Hardware-software integration
- Sensor integration
- Motor control
- GUI development
- Real-time interaction
- Modular software architecture

---

# Hardware Architecture

At a high level, the project connects software components running on a Raspberry Pi with sensing and actuation hardware.

```text
                    User
                     │
                     ▼
              GUI Control Panel
                     │
                     ▼
                ROS System
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
    Motor Control         Ultrasonic Sensor
          │                     │
          ▼                     ▼
       Motors              Environment
```

The Raspberry Pi acts as the computing platform coordinating these components.

---

# Software Design

The application follows a modular design in which individual responsibilities are separated into different components.

### User Interface Layer

Handles interaction between the user and the robotics system.

```text
ghost_lab_ui
```

### Control Layer

Handles robot motor behavior.

```text
motor_control
```

### Sensing Layer

Handles environmental distance sensing.

```text
ultrasonic_sensor
```

This separation makes individual components easier to modify without requiring major changes to the rest of the system.

---

# Getting Started

> **Note:** This repository preserves the original research implementation. Exact hardware configuration, ROS version, GPIO mappings, dependencies, and package configuration should be verified before attempting to run the project on different hardware.

---

## Prerequisites

A typical environment for this project requires:

- Linux-based operating system
- Raspberry Pi
- Python
- ROS installation compatible with the project
- CMake
- Appropriate GPIO libraries
- Motor-control hardware
- Ultrasonic sensor
- Git

---

# Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/ghost-lab-robot-control.git
```

Navigate into the repository:

```bash
cd ghost-lab-robot-control
```

---

# ROS Workspace Setup

The project packages should be placed within the source directory of the appropriate ROS workspace.

Example structure:

```text
ros_ws/
│
├── src/
│   ├── ghost_lab_ui/
│   ├── motor_control/
│   └── ultrasonic_sensor/
│
├── build/
├── install/
└── log/
```

The exact workspace build command depends on the ROS environment used by the original project.

For ROS environments using `colcon`, a typical build process is:

```bash
cd ~/ros_ws
colcon build
```

Then source the workspace:

```bash
source install/setup.bash
```

For ROS environments using another build system, use the appropriate build workflow for that ROS installation.

---

# Running the Components

The exact commands required to run the project depend on the ROS version and original package configuration.

The primary executable components are:

```text
ghost_lab_ui/src/gui_control_panel.py
motor_control/src/motor_control_node.py
ultrasonic_sensor/src/ultrasonic_sensor_node.py
```

The ultrasonic sensor component also includes:

```text
ultrasonic_sensor/launch/ultrasonic_sensor.launch
```

which can be used with the appropriate ROS launch command for the environment.

---

# Example System Workflow

A typical interaction with the application follows this process:

```text
1. Robot hardware is powered on
        ↓
2. Raspberry Pi initializes
        ↓
3. ROS environment starts
        ↓
4. Ultrasonic sensor node starts
        ↓
5. Motor-control node starts
        ↓
6. GUI control panel starts
        ↓
7. User provides movement commands
        ↓
8. Motor-control logic executes commands
        ↓
9. Ultrasonic sensor collects distance information
        ↓
10. Robot responds to user input and sensor information
```

---

# Development Objectives

The application was created to explore software and hardware integration in a robotics environment.

The primary objectives included:

- Creating modular robotics software components
- Developing a graphical robot-control interface
- Integrating motor-control functionality
- Integrating ultrasonic sensing
- Connecting Python software with physical hardware
- Supporting real-time robot interaction
- Creating a foundation for more advanced autonomous functionality

---

# Skills Demonstrated

This project demonstrates experience with:

- Python development
- ROS
- Robotics software architecture
- Raspberry Pi development
- GPIO programming
- Hardware-software integration
- Sensor integration
- Ultrasonic sensing
- Motor control
- Graphical user interfaces
- Event-driven interaction
- Modular software development
- Linux development environments
- CMake
- Git version control

---

# Research Context

This application was developed as part of research and experimentation within the **GHOST Lab**.

The broader research environment involved work related to robotics, human-robot interaction, robot situational awareness, and methods for improving autonomous robot behavior.

This repository specifically preserves the robot-control application containing the graphical interface, motor-control functionality, and ultrasonic sensing components.

---

# Potential Future Development

The system provides a foundation that could be expanded with additional robotics capabilities.

Potential improvements include:

- Autonomous obstacle avoidance
- Additional ultrasonic sensors
- Camera integration
- Computer vision
- Sensor fusion
- LiDAR integration
- Real-time telemetry visualization
- Improved graphical controls
- Autonomous navigation
- Path planning
- Mapping and localization
- ROS navigation integration
- Robot state monitoring
- Additional motor-control modes
- Remote robot operation
- Natural-language robot control
- Higher-level autonomous decision making

---

# Troubleshooting

## ROS Package Not Detected

Verify that the package is located inside the correct ROS workspace source directory.

Example:

```text
~/ros_ws/src/
```

Then rebuild and source the workspace.

---

## Python Node Does Not Run

Verify that:

- Python is installed
- Required packages are installed
- The script has the appropriate permissions
- The ROS environment has been sourced
- Hardware-dependent libraries are available

---

## GPIO Errors

GPIO functionality generally requires running the project on compatible Raspberry Pi hardware with the appropriate GPIO libraries installed.

Verify:

- GPIO pin configuration
- Hardware connections
- Sensor wiring
- Motor-controller wiring
- Required Python GPIO libraries

---

## Ultrasonic Sensor Does Not Return Data

Check:

- Trigger and echo pin connections
- Power and ground connections
- GPIO assignments
- Sensor compatibility
- Node configuration

---

## Motors Do Not Respond

Check:

- Motor-controller connections
- Power supply
- GPIO assignments
- Motor-control node configuration
- ROS communication between components

---

# Hardware Safety

When working with motors, Raspberry Pi GPIO pins, external power supplies, and sensors:

- Verify wiring before powering the system
- Avoid supplying incorrect voltage to GPIO pins
- Use an appropriate motor controller rather than driving motors directly from Raspberry Pi GPIO
- Ensure grounds are connected correctly
- Disconnect power before changing hardware connections

---

# Repository Notes

This repository primarily serves as an **archive of the original GHOST Lab implementation**.

Because the project was developed within a specific research and hardware environment, some dependencies, configuration files, hardware mappings, or ROS-specific settings may need to be recreated or adjusted before the application can be run on a new system.

The original source files have been preserved wherever possible so the project can be referenced, restored, or expanded in the future.

---

# Package Configuration Note

The archived project currently contains a visible `package.xml` for the `ultrasonic_sensor` package.

If `ghost_lab_ui` and `motor_control` were originally configured as complete ROS packages, their corresponding `package.xml` files should also be preserved if available.

The repository should retain original project files rather than creating replacement package configuration files unless the required dependencies and original ROS configuration are known.

---

# Version Control

Generated ROS workspace files should not be committed to the repository.

The repository `.gitignore` excludes common generated files such as:

```text
build/
install/
log/
__pycache__/
.DS_Store
```

Source code, ROS configuration, launch files, and package definitions should remain tracked.

---

# Project Status

**Archived / Research Project**

The repository preserves the GHOST Lab robot-control application for future reference and continued development.

---

# Author

**Sachi Sayal**

M.S. Artificial Intelligence in Business  
Arizona State University

B.S. Data Science  
Computer Science Concentration  
Arizona State University

---

# Acknowledgment

Developed as part of robotics research and experimentation within the **GHOST Lab**.

---

## Disclaimer

This repository contains research and educational robotics software. Hardware-specific functionality may require modification depending on the Raspberry Pi model, ROS environment, GPIO configuration, motor controller, sensors, and other equipment being used.
