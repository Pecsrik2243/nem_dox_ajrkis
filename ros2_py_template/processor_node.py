import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from collections import deque

class DataProcessor(Node):
    def __init__(self):
        super().__init__('data_processor')
        self.declare_parameter('window_size', 10)
        self.window = int(self.get_parameter('window_size').value)
        self.buf = deque(maxlen=self.window)
        self.sub = self.create_subscription(Float32, '/sensor/raw', self.on_msg, 10)
        self.pub = self.create_publisher(Float32, '/sensor/avg', 10)

    def on_msg(self, msg: Float32):
        self.buf.append(msg.data)
        avg = sum(self.buf) / len(self.buf)
        out = Float32()
        out.data = float(avg)
        self.pub.publish(out)

def main(args=None):
    rclpy.init(args=args)
    node = DataProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
