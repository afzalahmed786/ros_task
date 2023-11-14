#!/usr/bin/python
import rospy
from std_msgs.msg import String

rospy.init_node("pubsub_node")

the_pub2 = rospy.Publisher("/decrypted_name",String, queue_size = 10)


def decrypt(word):
    shift_amount = 3
    encrypted_text = ''
    for character in word:
        ascii_code = ord(character)
        shifted_code = ascii_code - shift_amount
        encrypted_character = chr(shifted_code)
        encrypted_text += encrypted_character
    return encrypted_text


def callback(msg):
    print("Subscribed word: " + msg.data)
    decrypted_text = decrypt(msg.data)
    print("Publishing decrypted word: " + decrypted_text)
    the_pub2.publish(decrypted_text)
    
the_sub = rospy.Subscriber("/encrypted_name",String, callback)

rospy.spin()