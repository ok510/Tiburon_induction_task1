#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class FollowTheGirl(Node):
    def __init__(self):
        super().__init__('follow_the_girl')

        
        self.publisher_ = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)

        
        self.target_pose = Pose()   
        self.follower_pose = Pose()  

        
        self.create_subscription(Pose, '/turtle1/pose', self.target_callback, 10)
        self.create_subscription(Pose, '/turtle2/pose', self.follower_callback, 10)

    def target_callback(self, msg):
        self.target_pose = msg

    def follower_callback(self, msg):
        self.follower_pose = msg
        self.follow()

    def follow(self):
        msg = Twist()

        dx = self.target_pose.x - self.follower_pose.x
        dy = self.target_pose.y - self.follower_pose.y

        distance = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)

        
        msg.linear.x = 1.5 * distance
        msg.angular.z = 4.0 * (angle - self.follower_pose.theta)

        
        if distance < 0.1:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher_.publish(msg)


def main():
    rclpy.init()
    node = FollowTheGirl()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
