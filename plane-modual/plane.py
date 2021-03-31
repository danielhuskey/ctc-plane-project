#importing stuff
import socket
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
ip = '192.168.1.90'
port = 2222
servoPIN0 = 14
servoPIN1 = 15
servoPIN2 = 16
servoPIN3 = 24
motorPIN0 = 25
motorPIN1 = 12



def gpio_setup(pin0, pin1, pin2, pin3, pin4, pin5):
    
    GPIO.setup(pin0, GPIO.OUT)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)
    GPIO.setup(pin4, GPIO.OUT)
    GPIO.setup(pin5, GPIO.OUT)
gpio_setup(servoPIN0,servoPIN1,servoPIN2,servoPIN3, motorPIN0, motorPIN1)


servo0 = GPIO.PWM(servoPIN0, 50)
servo1 = GPIO.PWM(servoPIN1, 50)
servo2 = GPIO.PWM(servoPIN2, 50)
servo3 = GPIO.PWM(servoPIN3, 50)
motor0 = GPIO.PWM(motorPIN0, 50)
motor1 = GPIO.PWM(motorPIN1, 50)
servo0.start(2.5)
servo1.start(2.5)
servo2.start(2.5)
servo3.start(2.5)
motor0.start(2.5)
motor1.start(2.5



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

def write_to_servo():    
    total_Controler_Input = connectServer.groundServer.recv(1024)
    controller_Input_Spilt = total_Controler_Input.split(',')
    
    servo0angle = controller_Input_Spilt[0]
    servo1angle = controller_Input_Spilt[1]
    servo2angle = controller_Input_Spilt[2]
    servo3angle = controller_Input_Spilt[3]
    motor0power = controller_Input_Spilt[4]
    motor1power = controller_Input_Spilt[5]

    servo0.ChangeDutyCycle(2+(int(servo0angle)/18))
    servo1.ChangeDutyCycle(2+(int(servo1angle)/18))
    servo2.ChangeDutyCycle(2+(int(servo2angle)/18))
    servo3.ChangeDutyCycle(2+(int(servo3angle)/18))
    motor0.ChangeDutyCycle(2+(int(motor0power)/18))
    motor1.ChangeDutyCycle(2+(int(motor1power)/18))
#one time tests/ connections


servoTest()
connectServer()

    
while True:
    write_to_servo()


