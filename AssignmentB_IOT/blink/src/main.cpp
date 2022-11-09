

//----------------------Skeleton Code--------------------//
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

//    Can be client or even host   //
#ifndef STASSID
#define STASSID "Ajay"  // Replace with your network credentials
#define STAPSK  "AJAY2001"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;


void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}

//-------------------------------------------------------//

#include <Arduino.h>

int U;
int V;

int A;
int B;


void led(int A, int B)
{
 digitalWrite(15, A);
 digitalWrite(16, B);

}
void setup() {
pinMode(2, INPUT); // Manual Input to Arduino
pinMode(4, INPUT); // Manual Input to Arduino

pinMode(15, OUTPUT); // To be conncted to LED1 for LHS of Distributive Law
pinMode(16, OUTPUT); // To be conncted to LED2 for RHS of Distributive Law

}

void loop()
{
  X=digitalRead(2);
  Y=digitalRead(4);
  
//For Distributive Law1
  A=A=(!U|V);      // LHS of Distributive Law to be conncted to LED1 for LHS of Distributive Law
  B=((!U&!V)|(!U&V)|(U&V)); // RHS of Distributive Law to be conncted to LED2 for RHS of Distributive Law

  
 led(A, B);

}
