
int pins[5]={2,3,4,5,6};
int trigpin=9;
int echopin=8;

double duration;
double distance;
void switchOn(int i)
{
  for(int i1=0;i1<5;i1++)
  {
    if(i1==i)digitalWrite(pins[i1],HIGH);
    else digitalWrite(pins[i1],LOW);
  }
}
void switchOff()
{
  for(int i1=0;i1<5;i1++)
  {
    digitalWrite(pins[i1],LOW);
  }
}
void setup() {
  Serial.begin(9600);
  for(int i=0;i<4;i++)pinMode(pins[i],OUTPUT);
  pinMode(trigpin,OUTPUT);
  pinMode(echopin,INPUT);
}
boolean access=false;
void loop() {
  digitalWrite(trigpin,LOW);
  for(int i=0;i<5;i++)
  {
    digitalWrite(pins[i],LOW);
  }/*
  for(int i=0;i<4;i++)
  {
    digitalWrite(pins[i],HIGH);
    delay(500);
    digitalWrite(pins[i],LOW);
  }*/
  digitalWrite(trigpin,HIGH);
  delayMicroseconds(10);   //Creating 10 second microPulse
  digitalWrite(trigpin,LOW);
  duration=pulseIn(echopin,HIGH);
  distance=duration*0.034/2;
  Serial.print(distance);
  Serial.println(" cm");
  if(access==true)
  {
      if(distance<20&&distance>11){switchOn(2);}
      else if(distance<=11&&distance>6){switchOn(1);}
      else if(distance<=6){switchOn(0);}
      else switchOff();
  }
  else if(access==false)
  {
    
    if(distance<20){
      Serial.println("Intruder");
      digitalWrite(pins[3],HIGH);digitalWrite(pins[4],HIGH);
      delay(400);
      digitalWrite(pins[3],LOW);digitalWrite(pins[4],LOW);
      delay(400);
      
      }
  }
  delay(50);
}
