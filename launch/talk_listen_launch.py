from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package = 'my_py_pkg',
            executable = 'talker',
        ),
        Node(
            package = 'my_py_pkg',
            executable = 'listener',
            output = 'screen',
        )
    ])


