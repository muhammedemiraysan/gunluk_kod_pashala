#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
byte servoPin1 = 10; byte servoPin2 = 5; byte servoPin3 = 6; byte servoPin4 = 9; byte servoPin5 = 3; byte servoPin6 = 11;
String x;
int i = 2;
int mapsolx;
int mapsoly;
int mapsagx;
int mapsagy;
int servo1a; int servo1b; int servo3a; int servo3b; int servo4a; int servo4b; int servo6a; int servo6b;
int servo2c; int servo5c;
int finalservo1; int finalservo2; int finalservo3; int finalservo4; int finalservo5; int finalservo6;
String solx = "0";
String soly = "0";
String sagx = "0";
String sagy = "0";
Servo servo6; Servo servo1; Servo servo2; Servo servo3; Servo servo4; Servo servo5;
void setup() {
lcd.init();
lcd.init();
pinMode(13,OUTPUT);
Serial.begin(115200); 
Serial.setTimeout(1);
servo1.attach(servoPin1); servo1.writeMicroseconds(1470);
servo2.attach(servoPin2); servo2.writeMicroseconds(1470);
servo3.attach(servoPin3); servo3.writeMicroseconds(1470);
servo4.attach(servoPin4); servo4.writeMicroseconds(1470);
servo5.attach(servoPin5); servo5.writeMicroseconds(1470);
servo6.attach(servoPin6); servo6.writeMicroseconds(1470);
delay(7000);
}
void loop() {
  while (!Serial.available()){;}
  x = Serial.readString();
  while(x[i] != 'n'){
    solx += x[i];
    i++;
  }
  i++;
  while(x[i] != 'n'){
    soly += x[i];
    i++;
  }
  i++;
  while(x[i] != 'n'){
    sagx += x[i];
    i++;
  }
  i++;
  while(x[i] != 'n'){
    sagy += x[i];
    i++;
  }
  mapsolx = map(solx.toInt(),-512,512,-340,330);
  mapsoly = map(soly.toInt(),-512,512,-340,330);
  mapsagx = map(sagx.toInt(),-512,512,-340,330);
  mapsagy = map(sagy.toInt(),-512,512,-340,330);
  servo1a = 1*mapsoly;  
  servo6a = 1*mapsoly;
  servo1b = 1*mapsagx; 
  servo3b = -1*mapsagx; 
  servo4b = 1*mapsagx; 
  servo6b = -1*mapsagx;
  servo2c = 1*mapsagy; 
  servo5c = -1*mapsagy;
  finalservo1 = 1470+servo1a+servo1b;
  finalservo2 = 1470+servo2c;
  finalservo3 = 1470+(-1*servo1a)+servo3b;
  finalservo4 = 1470+(-1*servo1a)+servo4b;
  finalservo5 = 1470+servo5c;
  finalservo6 = 1470+servo1a+servo6b;
  if(finalservo1 > 1800){finalservo1 = 1800;} if(finalservo1 <  1200){finalservo1 = 1200;}
  if(finalservo2 > 1800){finalservo2 = 1800;} if(finalservo2 <  1200){finalservo2 = 1200;}
  if(finalservo3 > 1800){finalservo3 = 1800;} if(finalservo3 <  1200){finalservo3 = 1200;}
  if(finalservo4 > 1800){finalservo4 = 1800;} if(finalservo4 <  1200){finalservo4 = 1200;}
  if(finalservo5 > 1800){finalservo5 = 1800;} if(finalservo5 <  1200){finalservo5 = 1200;}
  if(finalservo6 > 1800){finalservo6 = 1800;} if(finalservo6 <  1200){finalservo6 = 1200;}
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print(String(finalservo1)+"/"+String(finalservo3)+"/"+String(finalservo2));
  lcd.setCursor(0,1);
  lcd.print(String(finalservo4)+"/"+String(finalservo6)+"/"+String(finalservo5));
  i = 2;
  solx = "";
  soly = "";
  sagx = "";
  sagy = "";
  delay(100);
  lcd.clear();
  }
