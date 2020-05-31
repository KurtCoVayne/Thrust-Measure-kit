#include "HX711.h"

const int DOUT = 2;
const int CLK = 3;
const int AMPERAGE_PIN = A1;
float SENSIBILITY = 0.100;
HX711 scale;

void setup()
{
  Serial.begin(115200);
  scale.begin(DOUT, CLK);
  Serial.println(scale.read());
  pinMode(13,OUTPUT);
  scale.set_scale(226040); // Establecemos la escala
  scale.tare(50);     //El peso actual es considerado Tara.
  Serial.println("ready");
}

void loop()
{
  if (Serial.available() > 0)
  {
    char incomingByte = Serial.read();
    if (incomingByte == 'q')
    {
      digitalWrite(13,HIGH);
      Serial.print(scale.get_units(20), 3);
      Serial.print(",");
      Serial.println(getAmperage(20), 3);
    }
  }
  digitalWrite(13,LOW);
  delay(0);
}
float getAmperage(int samplesNumber)
{
  float voltage;
  float corrienteSum = 0;
  for (int i = 0; i < samplesNumber; i++)
  {
    voltage = analogRead(AMPERAGE_PIN) * 5.0 / 1023.0;
    corrienteSum += (voltage - 2.5) / SENSIBILITY;
  }
  return (corrienteSum / samplesNumber);
}
