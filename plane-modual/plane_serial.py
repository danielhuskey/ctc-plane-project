#importing stuff
import socket
import serial
import time

ip = '192.168.1.90'
port = 2222
serrial_connection_attampt = 1

def serialconnect():
    #try to connect to arduino
    try:
        connect_to_arduino('/dev/ttyACM0')
    except serial.serialutil.SerialException:
        print("serial not connected AMC0 Trying AMC1")
        try:
            connect_to_arduino('/dev/ttyACM1') 
        except serial.serialutil.SerialException:
            while serrial_connection_attampt !< 5:
            serrial_connection_attampt = serrial_connection_attampt + 1
            time.sleep(1)
            connect_to_arduino('/dev/ttyACM0') 
            connect_to_arduino('/dev/ttyACM1')
            if serrial_connection_attampt = 5:
                print("no serial connection to arduino. Exiting") 
                exit()            

def connect_to_arduino(raspbPath):
    #made new mathod to connect to arduino
    serialconnect.serialcom = serial.Serial(raspbPath, 115200)
    serialconnect.serialcom.timeout = 1
    print("serial success " + raspbPath)
    
def servoTest():
    # moving the servos to make sure its working
    serialconnect.serialcom.write("180")#moves the servo to 180 degrees
    time.sleep(2)#sec
    serialconnect.serialcom.write("0") #moves the servo to 0 degrees
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
    servoPitch.sepperating_commands = controller_Input_Spilt[2]
    servoRoll.sepperating_commands = controller_Input_Spilt[3]


def sening_commands_to_arduino ():
    #sending commands to the servo
    try:
        servoInput = servoRoll.sepperating_commands  
        time.sleep(1)
        
        if servoInput == b'':
            # if the servo input is empty except this and try to reconnect
            print("error moving to 0 servo")
            serialconnect.serialcom.write("0")# move the servo to 0 to try to level out and fligh stright
            connectServer()  
        else:
            try:
                serialconnect.serialcom.write(servoInput)
                print(servoInput)
            except socket.error:
                    time.sleep(4)
                    print("socket error trying to reconnect")
                    connect_to_ground_server()
    except socket.error:
            connectServer()





#one time tests/ connections
serialconnect()
servoTest()
connectServer()

    
while True:
    servoSend()

