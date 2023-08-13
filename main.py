from machine import Pin, UART
from time import sleep
import s900l

########################################################################
#Initial variable
led=Pin(25, Pin.OUT)
switch_pin = Pin(22, Pin.IN, Pin.PULL_UP)
gsm_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), timeout=2000)
counter=0
numberDestination = '' #Type number to call 
########################################################################
sleep(10) #Time for connect module GSM to net
while True:
    if switch_pin.value() == 0 and counter>=3:
        led.toggle()
        sleep(1)
        print('Three phone calls are made, the operation is completed')
    if switch_pin.value() == 0 and counter<3:
        print('The termination of the operation of the sprinkler system is detected')
        sleep(30)
        print('The rain shower terminated - I call three times')
        while switch_pin.value() == 0 and counter<3:
            led.value(0)
            print('This is '+ str(counter+1) +' call')
            s900l.call(numberDestination,20)
            counter+=1
            sleep(15)       
    if switch_pin.value() == 1:
        led.value(1)
        print('Ready to work')
        sleep(3)
        counter=0
    
