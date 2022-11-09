#include <Arduino.h>
int X,Y,Z;
int A,B,C,D,E,F,G,H;
void disp_7447(int H, int G, int F, int E, int D,int C, int B, int A)
{
  digitalWrite(12, A); 
  digitalWrite(13, B); 
  digitalWrite(14, C); 
  digitalWrite(15, D); 
  digitalWrite(16, E); 
  digitalWrite(17, F); 
  digitalWrite(18, G); 
  digitalWrite(19, H);  

}
void setup() {
    pinMode(12, OUTPUT);  
    pinMode(13, OUTPUT);
    pinMode(14, OUTPUT);
    pinMode(15, OUTPUT);  
    pinMode(16, OUTPUT);
    pinMode(17, OUTPUT);
    pinMode(18, OUTPUT);  
    pinMode(19, OUTPUT);
    pinMode(2, INPUT);
    pinMode(4, INPUT);  
    pinMode(5, INPUT);}

void loop() {
X=digitalRead(2);
Y=digitalRead(4);
Z=digitalRead(5);

A= !X&&!Y&&!Z;
B= !X&&!Y&&Z;
C= !X&&Y&&!Z;
D= !X&&Y&&Z;
E= X&&!Y&&!Z;
F= X&&!Y&&Z;
G= X&&Y&&!Z;
H= X&&Y&&Z;

disp_7447(A,B,C,D,E,F,G,H);  
}
