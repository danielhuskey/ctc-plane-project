#importing stuff
import socket
import serial
import time

#try to connect to arduino


def serialconnect():
    try:
        connect_to_arduino('/dev/ttyACM0')
        
    except serial.serialutil.SerialException:
        print("serial not connected AMC0 Trying AMC1")
        try:
            connect_to_arduino('/dev/ttyACM1')
            
        except serial.serialutil.SerialException:
            print("no serial connection to arduino. Exiting") 
            exit()
            
def connect_to_arduino(raspbPath):
    #made new mathod to connect to arduino
    serialconnect.serialcom = serial.Serial(raspbPath, 9600)
    serialconnect.serialcom.timeout = 1
    print("serial success " + raspbPath)
    
def servoTest():
    # moving the servos to make sure its working
    serialconnect.serialcom.write("180")
    time.sleep(2)#sec
    serialconnect.serialcom.write("0")
    print('worked')

#connect to the ground server also handles reconencting to said server if connection is lost. 

def connectServer():
    time.sleep(1)
    connectServer.groundServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Connecting to the server")        
        time.sleep(1)
        connectServer.groundServer.close
        connectServer.groundServer.connect(('192.168.1.90',  2222))
    except socket.error:
        while socket.error == True:
            time.sleep(1)
            connectServer.groundServer.close
            connectServer.groundServer.connect(('192.168.1.90',  2222)) 


#sending commands to the servo

def servoSend():
    try:
        servoInput = connectServer.groundServer.recv(1024)    
        time.sleep(1)
        
        if servoInput == b'':
            print("error moving to 0 servo")
            serialconnect.serialcom.write("0")
            connectServer()
            
        else:
            try:
                serialconnect.serialcom.write(servoInput)
                print(servoInput)
            except socket.error:
                    time.sleep(4)
                    print("socket error trying to reconnect")
                    groundServer.connect((ip,  port))
    except socket.error:
            connectServer()


# Not Used Yet. Conntrol for esc's are the same as servos so just reused code to save time. 
def escSend():
    try:
        escInput = connectServer.groundServer.recv(1024)    
        time.sleep(1)
        
        if servoInput == b'':
            print("error motor power half")
            serialconnect.serialcom.write("50")
             ### Add Try to recconect
            connectServer()
            
        else:
            try:
                serialconnect.serialcom.write(escInput)
                print(escInput)
            except socket.error:
                    time.sleep(4)
                    print("socket error trying to reconnect")
                    groundServer.connect((ip,  port))
    except socket.error:
            reconnect()



#one time tests/ connections
serialconnect()
servoTest()
connectServer()

    
while True:
    servoSend()

