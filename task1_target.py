#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math
from turtlesim.msg import Pose

class go_to_goal(Node):
    def __init__(self):
        super().__init__('go_to_goal')

        self.publisher_=self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.subscription = self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)
        self.pose=Pose()
        
        self.location_x = float(input("enter x-coordiante :"))
        self.location_y = float(input("enter y-coordinate :"))
        
    def pose_callback(self,msg):
        self.pose = msg
        self.move_to_goal()
        
    def move_to_goal(self):
        msg = Twist()
        xdis = self.location_x- self.pose.x
        ydis = self.location_y- self.pose.y
        totaldis = math.sqrt((xdis**2)+(ydis**2))
        angle = math.atan(ydis/xdis)
        msg.angular.z = angle
        msg.linear.x = totaldis
        if totaldis<0.1:
            msg.linear.x=0.0
            msg.angular.z=0.0
            
        self.publisher_.publish(msg)
        
def main():
    rclpy.init()
    node = go_to_goal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ =='__main__':
    main()