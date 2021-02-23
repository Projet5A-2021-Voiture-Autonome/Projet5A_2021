/*
  Programme pour tester une communication via port USB entre l'Arduino et la Jetson Nano
  Il faut utiliser ce programme sur l'Arduino et lancer le programme test_arduino.py sur la Jetson Nano.
  Sur la Jetson il faut donner l'instruction Y pour faire clignoter une LED de l'Arduino et N pour qu'elle ne s'allume plus.
*/

// the setup function runs once when you press reset or power the board
void setup() {
  // start serial port at 9600 bps:
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  while (!Serial) {
    ; // wait for serial port to connect.
  }
}

// the loop function runs over and over again forever
void loop() {
  char buffer[16];
  if (Serial.available() > 0) {
    int size = Serial.readBytesUntil('\n', buffer, 12);
    if (buffer[0] == 'O') {
      clignotement();
      delay(1000);
    }
    if (buffer[0] == 'N') {
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    }
  }

}

void clignotement() {
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(100);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(100);                       // wait for a second
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(100);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(100);                       // wait for a second
}
