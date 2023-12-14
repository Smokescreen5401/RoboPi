from gpiozero import LED, Motor, Button
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import subprocess

control = PiGPIOFactory(host='192.168.4.63')
robot = PiGPIOFactory(host='192.168.4.64')


WS = Button(26,pull_up=False,pin_factory=control)
AS = Button(19,pull_up=False,pin_factory=control)
SS = Button(13,pull_up=False,pin_factory=control)
DS = Button(6,pull_up=False,pin_factory=control)
DB = Button(27,pull_up=False,pin_factory=control)
IG = Button(17,pin_factory=control)



WL = LED(21, active_high=False,pin_factory=control)
AL = LED(20, active_high=False,pin_factory=control)
SL = LED(16, active_high=False,pin_factory=control)
DL = LED(12, active_high=False,pin_factory=control)
#DBL = LED(23, active_high=False,pin_factory=control)




Lmotor = Motor(8,7, pin_factory=robot)
Rmotor = Motor(10, 9,pin_factory=robot)
WL.on()
AL.off()
SL.off()
DL.off()
sleep(3)
WL.off()
AL.off()
SL.off()
DL.off()
sleep(1)
WL.on()
AL.on()
SL.on()
DL.on()
M=0
Wait = 0.1

def stop():
    Lmotor.forward(0)
    Rmotor.forward(0)
    Lmotor.backward(0)
    Rmotor.backward(0)
    WL.on()
    AL.on()
    SL.on()
    DL.on()
    
def Shutdown():
    exit()
    
def F():
    Lmotor.forward(1)
    Rmotor.forward(1)

def L():
    Lmotor.backward(1)
    Rmotor.forward(1)
    
def B():
    Lmotor.backward(1)
    Rmotor.backward(1)
   
def R():
    Lmotor.forward(1)
    Rmotor.backward(1)


    
    

print('Drive control enabled')

while True:
    print(DB.value)
#    while True:
#        DBL.on()
#        sleep(0.5)
#        DBL.off()



    
    
    
    if DB.value == 0:
        print('Drive Disabled')
#        Shutdown()
        
    elif IG.value == 0:
        Shutdown()

    if WS.value == 1:
        WL.off()
        F()
        M = 1
        sleep(Wait)
        print(M)
        
    if AS.value == 1:
        AL.off()
        L()
        M = 2
        sleep(Wait)
        print(M)

    elif SS.value == 1:
        SL.off()
        B()
        M = 3
        sleep(Wait)
        print(M)

    elif DS.value == 1:
        DL.off()
        R()
        M = 4
        sleep(Wait)
        print(M)

        
    else:
        stop()
    
