import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.declare_parameter('rate_hz', 20.0)
        self.rate = float(self.get_parameter('rate_hz').value)
        self.pub = self.create_publisher(Float32, '/sensor/raw', 10)
        self.timer = self.create_timer(1.0 / self.rate, self.tick)

    def tick(self):
        msg = Float32()
        msg.data = random.uniform(0.0, 100.0)
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
