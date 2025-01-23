#include <Servo.h>
#include "Ultrasonic.h"

#define RANGERPIN 6

Ultrasonic ultrasonic(RANGERPIN);
Servo myServo;
int ledPin = 3;

void setup() {

  Serial.begin(9600);
  myServo.attach(5);
  myServo.write(90);
  pinMode(ledPin, OUTPUT);
  analogWrite(ledPin, 255);
  delay(100);
  analogWrite(ledPin, 0);

}

void loop() {

  long RangeInCentimeters;
  RangeInCentimeters = ultrasonic.MeasureInCentimeters(); // two measurements should keep an interval
  Serial.print(RangeInCentimeters);//0~400cm
  Serial.println();
  delay(100);

  if ( RangeInCentimeters == 10 ) {

    myServo.write(0);
    analogWrite(ledPin, 85);
    delay(1000);

    myServo.write(90);
    analogWrite(ledPin, 170);
    delay(1000);
  
    myServo.write(180);
    analogWrite(ledPin, 255);
    delay(1000);

    myServo.write(90);
    analogWrite(ledPin, 0);
    delay(500);
      
  }
} 