#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class Drawshapes(Node):
    def __init__(self):
        super().__init__('draw_shapes')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
    def move(self, linear, angular, duration):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular

        end_time = time.time() + duration

        while time.time() < end_time:
            self.publisher_.publish(msg)
            time.sleep(0.01)   
            
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        
    def draw_square(self):
        for _ in range(4):
            self.move(2.0, 0.0, 2.0)
            self.move(0.0, math.pi/2, 1.0)   

    def draw_triangle(self):
        for _ in range(3):
            self.move(2.0, 0.0, 2.0)
            self.move(0.0, 2*math.pi/3, 1.0)

def main():
    rclpy.init()
    node = Drawshapes()

    time.sleep(2)  
    node.draw_square()

    time.sleep(2)
    node.draw_triangle()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
