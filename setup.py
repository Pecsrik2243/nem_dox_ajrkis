from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ros2_py_template'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='todo',
    maintainer_email='todo@todo.com',
    description='ROS2 Python sensor pipeline using the sze-info template layout.',
    license='GPL-3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_publisher = ros2_py_template.sensor_node:main',
            'data_processor = ros2_py_template.processor_node:main',
        ],
    },
)
