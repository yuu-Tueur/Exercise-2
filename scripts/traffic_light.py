#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
rospy.init_node('trafficlight')
pub = rospy.Publisher('count_up', Int32, queue_size = 1)
rate = rospy.Rate(10)

try:
	while True:
		print('blue')
		rospy.sleep(10.0)
		print('yellow')
		rospy.sleep(2.0)
		print('red')
		rospy.sleep(10.0)

except KeyboardInterrupt:
	sys.exit()
