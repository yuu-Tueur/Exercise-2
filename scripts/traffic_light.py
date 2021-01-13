#!/usr/bin/env python3

import rospy

rospy.init_node('trafficlight')

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
