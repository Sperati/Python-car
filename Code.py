import pygame

import RPi.GPIO as GPIO
from time import sleep

# setting up gpio board
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

GPIO.setup(31, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

##
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
##


pwm = GPIO.PWM(16, 100)

pwm.start(0)


pwm.ChangeDutyCycle(100)



pygame.init()
done = False
clock = pygame.time.Clock()
pygame.joystick.init()


while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
    if joystick.get_button(13) == True:
        done = True

    if joystick.get_button(3) == True:
        print('Foward')
        GPIO.output(16, GPIO.HIGH)

        GPIO.output(32, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)
        
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(35, GPIO.LOW)
        
        ##
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)

        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        ##
    elif joystick.get_button(1) == True:
        print('Back')
        GPIO.output(16, GPIO.HIGH)

        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
    
        GPIO.output(31, GPIO.LOW)
        GPIO.output(35, GPIO.HIGH)
        
        ##
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.HIGH)

        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
    elif joystick.get_button(0) == True:
        print('Left')
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(35, GPIO.LOW)
        
        ##
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.HIGH)

        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        ##
    elif joystick.get_button(2) == True:
        print('Right')
        
        GPIO.output(16, GPIO.HIGH)


        GPIO.output(32, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)
        
        GPIO.output(31, GPIO.LOW)
        GPIO.output(35, GPIO.HIGH)
        
        ##
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)

        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
    elif joystick.get_button(12) == True:
        # Doesn't really work, and doesn't stop
        GPIO.output(16, GPIO.HIGH)

        GPIO.output(32, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)
        
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(35, GPIO.LOW)
        
        ##
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)

        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        
        sleep(1)
        
        GPIO.output(32, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)
        
        GPIO.output(31, GPIO.LOW)
        GPIO.output(35, GPIO.HIGH)
        
        ##
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)

        GPIO.output(11, GPIO.HIGH)

        sleep(1.5)
        
        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        
        GPIO.output(31, GPIO.LOW)
        GPIO.output(35, GPIO.HIGH)
        
        ##
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.HIGH)

        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        ##
        sleep(1)

        GPIO.output(32, GPIO.HIGH)
        GPIO.output(36, GPIO.LOW)
        
        GPIO.output(31, GPIO.LOW)
        GPIO.output(35, GPIO.HIGH)
        
        ##
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)

        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)

        sleep(1.5)

        
        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        
        GPIO.output(31, GPIO.LOW)
        GPIO.output(35, GPIO.HIGH)
        
        ##
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.HIGH)

        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
  
        
    else:
        GPIO.output(36, GPIO.LOW)
        GPIO.output(35, GPIO.LOW)
        GPIO.output(32, GPIO.LOW)
        GPIO.output(31, GPIO.LOW)

        ##
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)

        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        ##

    
  
    clock.tick(10)
GPIO.cleanup()
pygame.quit ()
