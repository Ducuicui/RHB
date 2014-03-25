import unittest
import commands
import time
from uiautomator import device as d
import string

Contact_number='adb shell sqlite3 /data/data/com.android.providers.contacts/databases/contacts2.db "select count(*) from view_v1_people"'


class ContactTest(unittest.TestCase):
	
    def setUp(self):
	self.launchcontact()

    def tearDown(self):
	for i in range(5):
	    d.press.back()
    
    def testaddcontact(self):
	"""
	Summary:testAddContact: Add a contact.
	Steps:
	    1. Open Contacts app
	    2. Add contact
	    3. Exit Contacts app
	"""
	#get contact number before add
	beforeNO = self.getcontactnumber()
	#step 2 if no contact
	if d.exists(text='No contacts.'):
	    d(text='Create a new contact').click.wait()
	    if d.exists(text='Keep local'):
		d(text='Keep local').click.wait()
	    self.inputcontactinfo()
	#step 2 if exists contact
	else:
	    d(description='Add Contact').click.wait()
	    if d.exists(text='Keep local'):
		d(text='Keep local').click.wait()
	    self.inputcontactinfo()
	#get contact number after add
	time.sleep(3)
	afterNO = self.getcontactnumber()
	#assert afterNO = beforeNO + 1
	assert afterNO == beforeNO + 1
	
    def testdeletecontact(self):
	"""
	Summary:testAddContact: Add a contact.
	Steps:
	    1. Open Contacts app
	    2. Delete contact
	    3. Exit Contacts app
	"""
	#get contact number before delete
	beforeNO = self.getcontactnumber()
	#step 2 if beforeNO=0
	if beforeNO == 0:
	    d(text='Create a new contact').click.wait()
	    if d.exists(text='Keep local'):
		d(text='Keep local').click.wait()
	    self.inputcontactinfo()
	    d(resourceId='android:id/up').click.wait()
	    time.sleep(3)
	    beforeNO = self.getcontactnumber()
	#single tap the first contact 
	d.click(338,478)
	#delete contact
	d(description='More options',index='1').click.wait()
	d(text='Delete').click.wait()
	d(text='OK').click.wait()
	time.sleep(3)
	afterNO = self.getcontactnumber()
	#assert afterNO = beforeNO - 1
	assert afterNO == beforeNO - 1
	    

    
    def launchcontact(self):
    	#launch contact 
	d(text='People').click.wait()
	#if google account pop up
	if d.exists(text='Make it Google'):
	    d(text='Not now').click.wait()
	
    def getcontactnumber(self):
	number = commands.getoutput(Contact_number)
	return string.atoi(number)

    def inputcontactinfo(self):
    	#set contact name,phone
	d(text='Name').set_text('China Mobile')
	d(text='Phone',className='android.widget.EditText').set_text('10086')
	d(text='Done').click.wait()
