const int analogPin = A0; // El pin al que está conectado el potenciómetro
const int digitalPin = 2; // El pin digital que enviará el valor al Raspberry Pi

void setup() {
  pinMode(analogPin, INPUT);
  pinMode(digitalPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int analogValue = analogRead(analogPin);
  int digitalValue = map(analogValue, 0, 1023, 0, 254); // Mapear de 0 a 1023 a 0 a 254
  analogWrite(digitalPin, digitalValue);
  Serial.println(digitalValue);
  delay(100);
}
