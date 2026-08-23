cmake_minimum_required(VERSION 3.0.2)
project(ghost_lab_ui)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  sensor_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)
