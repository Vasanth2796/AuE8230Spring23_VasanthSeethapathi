#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys

def circle(line_velocity, ang_velocity):
    rospy.init_node('turtlemove', anonymous=True)
    Publish = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    Rate = rospy.Rate(10)
    
    Velocity = Twist()
    
    while True:
        Velocity.linear.x  = line_velocity
        Velocity.linear.y  = 0
        Velocity.linear.z  = 0
        
        Velocity.angular.x  = 0
        Velocity.angular.y  = 0
        Velocity.angular.z  = ang_velocity
        
        Publish.publish(Velocity)
        
        Rate.sleep()
        
        
circle(2.0,2.0)  
