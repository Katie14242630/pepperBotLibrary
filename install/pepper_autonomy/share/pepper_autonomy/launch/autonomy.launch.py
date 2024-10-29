import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
  pkg_move_pepper = get_package_share_directory('move_pepper')
  pkg_pepper_autonomy = get_package_share_directory('pepper_autonomy')

  autonomy_node_cmd = Node(
      package="pepper_autonomy",
      executable="autonomy_node",
      name="autonomy_node",
       parameters=[{
       "location_file": "/home/student/ros2_ws/src/pepperBotLibrary/src/pepper_autonomy/config/sim_lib_locations.yaml"

       }]
  )

  ld = LaunchDescription()

  # Add the commands to the launch description
  ld.add_action(autonomy_node_cmd)

  return ld
