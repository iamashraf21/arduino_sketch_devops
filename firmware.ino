#include <uECC.h>
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode (13, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {

  const struct uECC_Curve_t * curve = uECC_secp256k1();
  
  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(100);                       // wait for a second
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  delay(100);                       // wait for a second
  Serial.println("LED Loop");
}
