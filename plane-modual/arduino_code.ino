

#include <Servo.h>

Servo servo0;
Servo servo1;
Servo servo2;
Servo servo3;
Servo motor0;
Servo motor1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  servo0.attach(5);
  servo1.attach(6);
  servo2.attach(7);
  servo3.attach(8); 
  motor0.attach(3);
  motor1.attach(4); 
  motor0.write(0);
  motor1.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
      delay(2.5);
      String testString = Serial.readStringUntil('\n');
      Serial.println(testString);
      String serv0 = testString.substring(0, 2);
      String serv1 = testString.substring(2, 4);
      String serv2 = testString.substring(4, 6);
      String serv3 = testString.substring(6, 8);
      String motors0 = testString.substring(8,11);
      String motors1 = testString.substring(11,14);
      servo0.write(serv0.toInt());
      servo1.write(serv1.toInt());
      servo2.write(serv2.toInt());
      servo3.write(serv3.toInt());
      motor0.write(motors0.toInt());
      motor1.write(motors1.toInt());
      
}

}
