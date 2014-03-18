import unittest
import commands
import time
from uiautomator import device as d
import string




class MessageTest(unittest.TestCase):
	
    def setUp(self):
	self.launchmessage()

    def tearDown(self):
	for i in range(5):
	    d.press.back()

    def testsendSMS(self):
	"""
	Summary:testSendSMS: Send a SMS.
	Steps:1. Open Messages app
	      2. Clear all message
	      3. send a SMS
	      4. Delete all message
	      5. exit
	"""
	#step 2
	self.clearall()
	#step 3
	d(description='New message').click.wait()
	d(text='To',index='0').set_text('10086')
	d(text='Type message',index='0').set_text('cxyl')
	d(description='Send').click.wait()
	assert d(resourceId="com.android.mms:id/avatar").wait.exists(timeout=5000)


    def launchmessage(self):
	d(text='Messaging',index='3').click.wait()

    def clearall(self):
	if not d.exists(text='No conversations.'):
	    d(description='More options',index='2').click.wait()
	    d(text='Delete all threads').click.wait()
	    d(text='Delete',index='1').click.wait()
	    assert d.exists(text='No conversations.')
