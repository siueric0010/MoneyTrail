
#include <SoftwareSerial.h>

SoftwareSerial mySerial(4,3);
void setup() {
  Serial.begin(9600);   // USB serial port of Due (PROGRAMMING)
  mySerial.begin(9600);
  SendCommand("AT", "Ready");
}


void loop() {
  // put your main code here, to run repeatedly:

}

 
boolean SendCommand(String cmd, String ack){
  mySerial.println(cmd); // Send "AT+" command to module
}
 
