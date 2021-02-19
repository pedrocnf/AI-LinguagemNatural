
#include <SoftwareSerial.h>

SoftwareSerial mySerial(6, 7); 

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; 
  }
  Serial.println("Interface serial ativada - RecSystem");
  mySerial.begin(9600);
}
void loop() {
  if (mySerial.available()) {
    Serial.write(mySerial.read());
  }
  if (Serial.available()) {
    mySerial.write(Serial.read());
  }
}

