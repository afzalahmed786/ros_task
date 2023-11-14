#!/usr/bin/python
import rospy
from std_msgs.msg import String

rospy.init_node("the_listen_node")

def callback(msg):
    print("Subscribed word: " + msg.data)

the_listener = rospy.Subscriber("/decrypted_name",String, callback)

rospy.spin()