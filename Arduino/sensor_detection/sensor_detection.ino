int PWM; // Variable PWM image de la vitesse
int moteur1_PWM = 10;
// defines pins numbers
const int trigPin = 9;
const int echoPin = 8;
// defines variables
long duration;
int distance;
void setup() {
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
Serial.begin(9600); // Starts the serial communication
pinMode(moteur1_PWM, OUTPUT); // Pin 8 Arduino en sortie PWM
}
void loop() {
  PWM = 50;

// Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);
// Calculating the distance
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor
Serial.print("Distance: ");
Serial.println(distance);

  
 if(distance>20){
  avance_motor(PWM);
 }else{
  arret_motor();
 }


}

void avance_motor(int PWM){
  analogWrite(moteur1_PWM,PWM);
  digitalWrite(moteur1_PWM,PWM);
}

void arret_motor(){
  digitalWrite(moteur1_PWM,0);
}
