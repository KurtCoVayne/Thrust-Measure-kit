#include "HX711.h"
const int DOUT=A1;
const int CLK=A0;


HX711 balanza;
void setup() {
  Serial.begin(9600);
  balanza.begin(DOUT, CLK);
  Serial.print("Lectura del valor del ADC:t");
  Serial.println(balanza.read());
  Serial.println("No ponga ningún objeto sobre la balanza");
  Serial.println("Destarando...");
  balanza.set_scale(); //La escala por defecto es 1
  balanza.tare(20);  //El peso actual es considerado Tara.
  Serial.println("Coloque un peso conocido:");  
}

void loop() {
  if (balanza.wait_ready_timeout(1000)) {
Serial.print("Valor de lectura: t");
  Serial.println(balanza.get_value(10),0);
  delay(100);
} 
  
  else {
    Serial.println("FATAL ERROR HX711 not found.");
}
}
