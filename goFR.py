#!/usr/bin/env python

# An example of TurtleBot 2 drawing a 0.4 meter square.
# Written for indigo

import rospy
from geometry_msgs.msg import Twist
from math import radians
count = 0

class goFR():
    def __init__(self):
        # initiliaze
        rospy.init_node('drawasquare', anonymous=False)

        # What to do you ctrl + c
        rospy.on_shutdown(self.shutdown)

        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

	# 5 HZ
        r = rospy.Rate(5);

	# create two different Twist() variables.  One for moving forward.  One for turning 45 degrees.

        # let's go forward at 0.2 m/s
        move_cmd = Twist()
        move_cmd.linear.x = 0.2
	# by default angular.z is 0 so setting this isn't required

        #let's turn at 45 deg/s
        turn_cmd = Twist()
        turn_cmd.linear.x = 0
        turn_cmd.angular.z = radians(45); #45 deg/s in radians/s

	#two keep drawing squares.  Go forward for 2 seconds (10 x 5 HZ) then turn for 2 second

        while not rospy.is_shutdown():
	    # go forward 0.4 m (2 seconds * 0.2 m / seconds)
	    rospy.loginfo("Going Straight")
            for x in range(0,10) :
                self.cmd_vel.publish(move_cmd)
                r.sleep()
	    # turn 90 degrees
	    rospy.loginfo("Turning")
            for x in range(0,10) :
                self.cmd_vel.publish(turn_cmd)
                count=count+1;
                r.sleep()

                rospy.loginfo("finish")

    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop Drawing Squares")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        goFR()
    except:
        rospy.loginfo("node terminated.")
