#include <DHT.h>

#define DHTPIN 2     // Pin al que está conectado el sensor
#define DHTTYPE DHT11   

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {

  float temperatura = dht.readTemperature();


  if (isnan(temperatura)) {
    Serial.println("Error");
    return;
  }

  // Se muestra solo la temperatura en el monitor serial
  Serial.println(temperatura);

  delay(2000); // Espera 2 segundos antes de realizar la próxima lectura
}
