#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FrequencyControl(Node):
    def __init__(self):
        super().__init__('frequency_control')

        self.publisher_ = self.create_publisher(String, 'chatter', 10)

        # Timer → runs every 0.1 sec (10 Hz)
        self.timer = self.create_timer(0.1, self.publish_message)

        self.count = 0

    def publish_message(self):
        msg = String()
        msg.data = f"Message count: {self.count}"

        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)

        self.count += 1


def main():
    rclpy.init()
    node = FrequencyControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()