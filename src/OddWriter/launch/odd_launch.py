
#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='OddWriter',           # ← замени на своё имя пакета
            executable='odd2',
            name='even_pub',
            output='screen',
        ),
        Node(
            package='OddWriter',
            executable='odd_listener',
            name='overflow_listener',
            output='screen',
        ),
    ])