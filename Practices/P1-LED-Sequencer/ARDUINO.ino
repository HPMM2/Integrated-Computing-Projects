const int sensorPin = A7;  // Pin analógico para leer el sensor de voltaje
const int potPin = A1;     // Pin analógico para leer el potenciómetro
const int ledPin = 2;      // Pin digital para el LED rojo

// Variables
int sensorValue = 0;       // Almacenar el valor del sensor de voltaje
int potValue = 0;          // Almacenar el valor del potenciómetro
float voltage = 0.0;       // Almacenar el voltaje calculado
float refVoltage = 0.0;    // Almacenar el voltaje de referencia

void setup() {
  pinMode(sensorPin, INPUT);
  pinMode(potPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); 
}

void loop() {
  // Leer el valor del sensor de voltaje
  sensorValue = analogRead(sensorPin);
  
  // Convertir el valor a voltaje
  voltage = sensorValue * (5.0 / 1023.0); // El Arduino Nano tiene un rango de 0-5V en el pin analógico
  
  // Leer el valor del potenciómetro y calcular el voltaje de referencia
  potValue = analogRead(potPin);
  refVoltage = potValue * (5.0 / 1023.0); // Convertir el valor del potenciómetro a voltaje
  
  // Imprimir los valores en el puerto serie (para propósitos de depuración)
  Serial.print("Voltage: ");
  Serial.print(voltage);
  Serial.print("V, Reference Voltage: ");
  Serial.print(refVoltage);
  Serial.println("V");
  
  // Comprobar si el voltaje es bajo comparado con el voltaje de referencia
  if (voltage > refVoltage) {
    // Encender el LED rojo
    digitalWrite(ledPin, HIGH);
  } else {
    // Apagar el LED rojo
    digitalWrite(ledPin, LOW);
  }
  
  delay(100); 
}
