###################################################################
# Experimental primitive proto GUI for switching relays on/off via
# GPIO ports on Rpi 3 Model B. The relay block used
# had 8 relays and 8 input pins. This code creates a
# Tkinter frame with 8 buttons which are bound to event
# handler methods which toggle the GPIO pins LOW/HIGH
# when clicked. The particular relay block being used
# switched the relays on when the GPIO pins are set LOW.
#
# Testing Carried Out:
# -------------------
# Tested code on an Rpi 3 Model B using mouse to click the 
# buttons and relays switched on and off successfully.Also tested
# from a smart phone using VNC Viewer to click the buttons remotely
# over Wifi connection and this also successfully switched the 
# relays on and off.
#
#
# Bampot1 3/10/2020
##################################################################
import RPi.GPIO as GPIO
from Tkinter import *
a=Tk()
a.title("Test GUI for GPIO Relay Switching")

relay8_input = 11 # define GPIO pin to activate relays, physical numbering
relay7_input = 13 
relay6_input = 15
relay5_input = 29
relay4_input = 31
relay3_input = 33
relay2_input = 35
relay1_input = 37 

def setup():
	GPIO.cleanup() 
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(relay1_input, GPIO.OUT)
	GPIO.setup(relay2_input, GPIO.OUT)  
	GPIO.setup(relay3_input, GPIO.OUT)  
	GPIO.setup(relay4_input, GPIO.OUT)  
	GPIO.setup(relay5_input, GPIO.OUT)  
	GPIO.setup(relay6_input, GPIO.OUT)  
	GPIO.setup(relay7_input, GPIO.OUT)  
	GPIO.setup(relay8_input, GPIO.OUT)  
	GPIO.output(relay1_input, GPIO.HIGH)
	GPIO.output(relay2_input, GPIO.HIGH)
	GPIO.output(relay3_input, GPIO.HIGH)  
	GPIO.output(relay4_input, GPIO.HIGH)
	GPIO.output(relay5_input, GPIO.HIGH)  
	GPIO.output(relay6_input, GPIO.HIGH) 
	GPIO.output(relay7_input, GPIO.HIGH)
	GPIO.output(relay8_input, GPIO.HIGH)  
	
def destroy():
	GPIO.cleanup()


def rel1():
	if GPIO.input(relay1_input)==GPIO.LOW : # relay on
		GPIO.output(relay1_input,GPIO.HIGH) # switch it off
		print("Relay 1 off")
	else : # relay off
		GPIO.output(relay1_input,GPIO.LOW) # switch it on
		print("Relay 1 On")
	
def rel2():
	if GPIO.input(relay2_input)==GPIO.LOW: # relay on
		GPIO.output(relay2_input,GPIO.HIGH) # switch it off
		print("Relay 2 off")
	else : # relay off
		GPIO.output(relay2_input,GPIO.LOW) # switch it on
		print("Relay 2 On")
		
def rel3():
	if GPIO.input(relay3_input)==GPIO.LOW: # relay on
		GPIO.output(relay3_input,GPIO.HIGH) # switch it off
		print("Relay 3 off")
	else : # relay off
		GPIO.output(relay3_input,GPIO.LOW) # switch it on
		print("Relay 3 On")
		
def rel4():
	if GPIO.input(relay4_input)==GPIO.LOW: # relay on
		GPIO.output(relay4_input,GPIO.HIGH) # switch it off
		print("Relay 4 off")
	else : # relay off
		GPIO.output(relay4_input,GPIO.LOW) # switch it on
		print("Relay 4 On")
		
def rel5():
	if GPIO.input(relay5_input)==GPIO.LOW: # relay on
		GPIO.output(relay5_input,GPIO.HIGH) # switch it off
		print("Relay 5 off")
	else : # relay off
		GPIO.output(relay5_input,GPIO.LOW) # switch it on
		print("Relay 5 On")
		
def rel6():
	if GPIO.input(relay6_input)==GPIO.LOW: # relay on
		GPIO.output(relay6_input,GPIO.HIGH) # switch it off
		print("Relay 6 off")
	else : # relay off
		GPIO.output(relay6_input,GPIO.LOW) # switch it on
		print("Relay 6 on")
		
def rel7():
	if GPIO.input(relay7_input)==GPIO.LOW: # relay on
		GPIO.output(relay7_input,GPIO.HIGH) # switch it off
		print("Relay 7 off")
	else : # relay off
		GPIO.output(relay7_input,GPIO.LOW) # switch it on
		print("Relay 7 On")
		
def rel8():
	if GPIO.input(relay8_input)==GPIO.LOW: # relay on
		GPIO.output(relay8_input,GPIO.HIGH) # switch it off
		print("Relay 8 off")
	else:                                                                                                                                                                                                                                
		GPIO.output(relay8_input,GPIO.LOW) # switch it on
		print("Relay 8 On")
		
		
	
		
frame = LabelFrame(a, padx=5, pady=5)
frame.pack(padx=200, pady=200)

relay1 = Button(frame, text="Relay 1 On/Off")
relay2 = Button(frame, text="Relay 2 On/Off")
relay3 = Button(frame, text="Relay 3 On/Off")
relay4 = Button(frame, text="Realy 4 On/Off")
relay5 = Button(frame, text="Relay 5 On/Off")
relay6 = Button(frame, text="Relay 6 On/Off")
relay7 = Button(frame, text="Relay 7 On/Off")
relay8 = Button(frame, text="Relay 8 On/Off")

relay1.pack()
relay2.pack()
relay3.pack()
relay4.pack()
relay5.pack()
relay6.pack()
relay7.pack()
relay8.pack()

relay1.config(command=rel1)
relay2.config(command=rel2)
relay3.config(command=rel3)
relay4.config(command=rel4)
relay5.config(command=rel5)
relay6.config(command=rel6)
relay7.config(command=rel7)
relay8.config(command=rel8)
setup()

a.mainloop()



