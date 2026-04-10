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

        xdis = self.target_pose.x - self.follower_pose.x
        ydis = self.target_pose.y - self.follower_pose.y

        total_distance = math.sqrt((xdis**2) + (ydis**2))
        angle = math.atan(ydis/xdis)

        
        msg.linear.x =total_distance
        msg.angular.z = angle

        
        if total_distance < 0.1:
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
