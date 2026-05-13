#include <Adafruit_NeoPixel.h>
#include <DHT.h>

#define LED_PIN 6     //PIN D6
#define NUM_LEDS 33   //NUMERO DE LEDS EN LA TIRA 
#define DHTPIN 2      //PIN D2
#define DHTTYPE DHT11
#define sensorPin A7  //PIN A7

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);
DHT dht(DHTPIN, DHTTYPE);

bool blinking = false;  // VARIABLE PARA PARPADEO

void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.show();  // LEDS APAGADOS INICIO
  dht.begin();
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    executeCommand(command);
  }

  float temperature = dht.readTemperature();
  if (!isnan(temperature)) {
    Serial.println(temperature);
  } else {
    Serial.println("Error");
  }
  
  // LEER VOLTAJE
  int sensorValue = analogRead(sensorPin);
  
  // CONVERTIR VOLTAJE
  float voltage = sensorValue * (5.0 / 1023.0); 
  
  voltage = voltage * 5; 
  
  // IMPRIMIR
  Serial.println(voltage);
  
  delay(1000); 
}

void executeCommand(char command) {
  if (blinking) {
    turnOffLEDs();
    blinking = false;
  }
  
  switch (command) {
    case 'E': // APAGA LOS LEDS
      turnOffLEDs();
      break;
    case 'B': // LUZ CALIDA
      setColorWithFrequency(255, 50, 0, 40.0);
      blinking = true;
      break;
    case 'W': // LUZ FRIA
      setColorWithFrequency(255, 255, 255, 40.0);
      blinking = true;
      break;
  }
}

void setColorWithFrequency(int red, int green, int blue, float frequency) {
  int delayTime = round(1000.0 / (2 * frequency)); // Calcula el tiempo de espera en milisegundos para el parpadeo
  unsigned long startTime = millis();  // Guarda el tiempo de inicio
  unsigned long duration = 2 * 60 * 60 * 1000; // Duración en milisegundos (2 horas)

  while (millis() - startTime < duration && !Serial.available()) { // Parpadear durante 2 horas o hasta que llegue CASE E
    for (int i = 0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, strip.Color(red, green, blue));
    }
    strip.show();
    delay(delayTime);
    for (int i = 0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, 0);
    }
    strip.show();
    delay(delayTime);
  }
}

void turnOffLEDs() {
  for (int i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, 0);
  }
  strip.show();
}
