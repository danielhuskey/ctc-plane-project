#importing stuff
import socket
import time
import RPi.GPIO as GPIO
ip = '192.168.1.90'
port = 2222
servoPIN0 = 14
servoPIN1 = 24
servoPIN2 = 16
servoPIN3 = 26

servo0 = GPIO.PWM(servoPIN0, 50)
servo1 = GPIO.PWM(servoPIN1, 50)
servo2 = GPIO.PWM(servoPIN2, 50)
servo3 = GPIO.PWM(servoPIN3, 50)

servo0.start(2.5)
servo1.start(2.5)
servo2.start(2.5)
servo3.start(2.5)

def gpio_setup(pin0, pin1, pin2, pin3):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin0, GPIO.OUT)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)
    
def servoTest():
    # moving the servos to make sure its working
    servo0.ChangeDutyCycle(2+(0/18))
    servo1.ChangeDutyCycle(2+(0/18))
    servo2.ChangeDutyCycle(2+(0/18))
    servo3.ChangeDutyCycle(2+(0/18))
    time.sleep(.2)
    servo0.ChangeDutyCycle(2+(90/18))
    servo1.ChangeDutyCycle(2+(90/18))
    servo2.ChangeDutyCycle(2+(90/18))
    servo3.ChangeDutyCycle(2+(90/18))
    time.sleep(.2)
    servo0.ChangeDutyCycle(2+(180/18))
    servo1.ChangeDutyCycle(2+(180/18))
    servo2.ChangeDutyCycle(2+(180/18))
    servo3.ChangeDutyCycle(2+(180/18))
    time.sleep(.2)
    servo0.ChangeDutyCycle(2+(0/18))
    servo1.ChangeDutyCycle(2+(0/18))
    servo2.ChangeDutyCycle(2+(0/18))
    servo3.ChangeDutyCycle(2+(0/18))
    print('worked')

def connectServer():
    #connect to the ground server also handles reconencting to said server if connection is lost. 
    connectServer.groundServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Connecting to the server")        
        connect_to_ground_server()
    except socket.error:
        while socket.error == True:
            time.sleep(1)
            connect_to_ground_server()

def connect_to_ground_server():
    #connecting to gound server
    connectServer.groundServer.close
    connectServer.groundServer.connect((ip,  port))

def sepperating_commands():
    #sepperting the commands to the plane into their own parts
    total_Controler_Input = connectServer.groundServer.recv(1024)
    controller_Input_Spilt = total_Controler_Input.split(',')
    motor0Power.sepperating_commands = controller_Input_Spilt[0]
    motor1Power.sepperating_commands = controller_Input_Spilt[1]
    servo0angle.sepperating_commands = controller_Input_Spilt[2]
    servo1angle.sepperating_commands = controller_Input_Spilt[3]
    servo2angle.sepperating_commands = controller_Input_Spilt[4]
    servo3angle.sepperating_commands = controller_Input_Spilt[5]

def write_to_servo()    
    servo0.ChangeDutyCycle(2+(servo0angle.sepperating_commands/18))
    servo1.ChangeDutyCycle(2+(servo1angle.sepperating_commands/18))
    servo2.ChangeDutyCycle(2+(servo2angle.sepperating_commands/18))
    servo3.ChangeDutyCycle(2+(servo3angle.sepperating_commands/18))

#one time tests/ connections
gpio_setup(servoPIN0,servoPIN1,servoPIN2,servoPIN3)
serialconnect()
servoTest()
connectServer()

    
while True:
    servoSend()

