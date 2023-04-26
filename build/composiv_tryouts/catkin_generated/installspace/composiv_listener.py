#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

#code taken from http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    rospy.init_node('composiv_listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()