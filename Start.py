from gpiozero import Button, LED
import subprocess
from time import sleep
import os

# Set up GPIO pins
JL = LED(24,active_high = False)
DL = LED(23,active_high = False)
JB = Button(22, pull_up = False)
DB = Button(27,pull_up = False)
AC = Button(18)
ST = Button(5)
IG = Button(17)
J = 0
D = 0

# Run Jitsi Meet.py program
def Jitsi():
    print('Video call')
    os.system('python Jitsi.py')


def Drive():
    print('Drive')
    os.system('python MT.py')
        
    
def Shutdown():
    os.system('sudo shutdown now')

JL.on()
DL.on()
sleep(0.5)
JL.off()
DL.off()
sleep(0.5)
while True:
#    if AC.value == 1 and IG.value != 1 and ST.value != 1:
#        print('Shutdown')
#        sleep(5)
#        Shutdown()
        
    if ST.value == 1 and JB.value == 0 and DB.value == 0:
        JL.on()
        DL.on()
        sleep(0.2)
        JL.off()
        DL.off()
        sleep(0.2)
        
    elif ST.value == 1 and DB.value == 0:
        DL.on()
        sleep(0.2)
        DL.off()
        sleep(0.2)
        
    elif ST.value == 1 and JB.value == 0:
        JL.on()
        sleep(0.2)
        JL.off()
        sleep(0.2)
        
    elif ST.value == 1 and JB.value == 1 and DB.value == 1:
        JL.on()
        DL.on()
        Jitsi()
        Drive()
    
    elif ST.value == 1 and DB.value == 1:
        DL.on()
        Drive()
        
   0 elif ST.value == 1 and JB.value == 1:
        JL.on()
        Jitsi()
    DL.off()
    JL.off()
DL.off()
JL.off()
        
        
        
