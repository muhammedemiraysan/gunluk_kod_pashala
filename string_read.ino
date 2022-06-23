#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
String x;
int i = 2 ;
String solx = "";
String soly = "";
String sagx = "";
String sagy = "";
void setup() {
  lcd.init();
  lcd.init();
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());
  x = Serial.readString();
  lcd.backlight();
  
  while(x[i] != 'n'){
    solx += x[i];
    i++;
  }
  lcd.setCursor(0,0);
  lcd.print(String(solx));
  while(x[i] != 'n'){
    soly += x[i];
    i++;
  }
  i++;
  lcd.setCursor(5,0);
  lcd.print(String(soly));  

  while(x[i] != 'n'){
    sagx += x[i];
    i++;
  }
  i++;
  lcd.setCursor(0,1);
  lcd.print(String(sagx));
  while(x[i] != 'n'){
    sagy += x[i];
    i++;
  }
  lcd.setCursor(5,1);
  lcd.print(String(sagy));  
  
  
  i = 2;
  
  solx = "";
  soly = "";
  sagx = "";
  sagy = "";
  delay(100);
  lcd.clear();
  }
