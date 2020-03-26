#!/usr/bin/env python

"""
    work.py 
    
"""

import rospy, os, sys
from std_msgs.msg import String
from sound_play.libsoundplay import SoundClient

class Work:
    def __init__(self, script_path):
        rospy.init_node('work')
        rospy.on_shutdown(self.cleanup)
        self.soundhandle = SoundClient()
        
        # Wait a moment to let the client connect to the sound_play server
        rospy.sleep(1)
        
        # Make sure any lingering sound_play processes are stopped.
        self.soundhandle.stopAll()
        
        # Announce that we are ready for input
        rospy.loginfo("Ready, waiting for commands...")
	self.soundhandle.say('Hello, I am Robort. What can I do for you?')
	#rospy.sleep(5)

        # Subscribe to the recognizer output and set the callback function
        rospy.Subscriber('/lm_data', String, self.talkback)


    def talkback(self, msg):
        # Print the recognized words on the screen
        rospy.loginfo(msg.data)

	if msg.data.find('WHAT IS YOUR NAME')>-1:
        	#rospy.sleep(1)
		self.soundhandle.say('I heard you ask about my name.')
                rospy.sleep(3)
                self.soundhandle.say(' My name is Robort. It is happy for me to meet you.')
                rospy.loginfo('I heard you ask about my name. My name is Robort. It is happy for me to meet you.')
		#rospy.sleep(10) 
	elif msg.data.find('HOW OLD ARE YOU')>-1:
        	#rospy.sleep(1)
		self.soundhandle.say('I heard you ask about my age. ')
                rospy.sleep(3)
                self.soundhandle.say('I am five years old.')
		rospy.loginfo('I heard you ask about my age. I am five years old.')
                #rospy.sleep(5) 
	elif msg.data.find('WHERE ARE YOU FROM')>-1:
        	#rospy.sleep(1)
		self.soundhandle.say('I heard you ask about my hometown.')
                rospy.sleep(3)
                self.soundhandle.say('I am from China.')
                rospy.loginfo('I heard you ask about my hometown.I am from China.')
		#rospy.sleep(5)
	elif msg.data.find('WHAT CAN YOU DO')>-1:
        	#rospy.sleep(1)
		self.soundhandle.say('I heard you ask about my ability.')
                rospy.sleep(3)
                self.soundhandle.say('I am good at doing housework.')
                rospy.loginfo('I heard you ask about my ability.I am good at doing housework.')
		#rospy.sleep(5)
        elif msg.data.find('THANK YOU FOR TALKING TO ME')>-1:
                self.soundhandle.say('You are welcome. I have a good chat with you.')
                rospy.loginfo('You are welcome. I have a good chat with you.')
	else:rospy.sleep(3)

    def cleanup(self):
        self.soundhandle.stopAll()
        rospy.loginfo("Shutting down talkback node...")


if __name__=="__main__":
    try:
        Work(sys.path[0])
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Work node terminated.")
