from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='ros2_py_template', executable='sensor_publisher', parameters=[{'rate_hz': 20.0}]),
        Node(package='ros2_py_template', executable='data_processor', parameters=[{'window_size': 10}]),
    ])
