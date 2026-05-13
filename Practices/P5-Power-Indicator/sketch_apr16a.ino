const int sensorPin = A7;  
const int potPin = A1;     

// Variables
int sensorValue = 0;       
int potValue = 0;          
float voltage = 0.0;       
float refVoltage = 0.0;    

void setup() {
  pinMode(sensorPin, INPUT);
  pinMode(potPin, INPUT);
  Serial.begin(9600); 
}

void loop() {

  sensorValue = analogRead(sensorPin);
  

  voltage = sensorValue * (5.0 / 1023.0); // El Arduino Nano tiene un rango de 0-5V en el pin analógico
  
 
  potValue = analogRead(potPin);
  refVoltage = potValue * (5.0 / 1023.0); 
  
  Serial.print(voltage);
  Serial.print(",");
  Serial.println(refVoltage);
  
  delay(100); 
}

