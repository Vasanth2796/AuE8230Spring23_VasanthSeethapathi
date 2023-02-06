#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def Move():
     rospy.init_node("Ninja_Turtle", anonymous=False, log_level=rospy.INFO, disable_signals=False)    
     Publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=20)
     vel_msg=Twist() 
     Rate=rospy.Rate(1)
     
     Vel_X=0.2
     Vel_Y=0.2 
     vel_msg.linear.y=0
     vel_msg.linear.z =0
     vel_msg.angular.x=0
     vel_msg.angular.y=0
     ang= 90*(2*(22/7)/360) # 90 degrees angle for reference to take the turns
     
     IT = float(rospy.Time.now().to_sec())
     CD= 0
     while CD < 2:
           vel_msg.linear.x=Vel_X
           vel_msg.angular.z=0
           Publisher.publish(vel_msg)
           FT=float(rospy.Time.now().to_sec())
           CD =Vel_X*(FT-IT)+CD # Using the delta time (Final Time - Initial Time) calculating the linear distance moved by Turtle
           Rate.sleep()

     vel_msg.linear.x=0 # After reaching the desired distance, the turtle must stop at that position.
     vel_msg.angular.z=Vel_Y
     
     IT = float(rospy.Time.now().to_sec())
     CA = 0
     while (CA<ang):
          Publisher.publish(vel_msg)
          FT = float(rospy.Time.now().to_sec())
          CA = Vel_Y*(FT-IT) # Using the delta time (Final Time - Initial Time) calculating the angule moved by Turtle
          
     vel_msg.angular.z = 0  # After 90 degrees turn, there should not be changes in heading angle 
     Publisher.publish(vel_msg)
   
while True:     # infinite Loop       
      Move()
