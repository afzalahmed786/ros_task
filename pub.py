#!/usr/bin/python
import rospy
from std_msgs.msg import String

rospy.init_node("encryption_node")

the_talker = rospy.Publisher("/encrypted_name",String, queue_size = 10)

def encrypt(word):
    shift_amount = 3
    encrypted_text = ''
    for character in word:
        ascii_code = ord(character)
        shifted_code = ascii_code + shift_amount
        encrypted_character = chr(shifted_code)
        encrypted_text += encrypted_character
    return encrypted_text

rate = rospy.Rate(1)

while not rospy.is_shutdown():
    word= "Afzal"
    encrypted_text = encrypt(word)
    print("Publishing encrypted word: " + encrypted_text)
    the_talker.publish(encrypted_text)
    rate.sleep()
