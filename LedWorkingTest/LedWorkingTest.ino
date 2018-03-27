int pins[5]={2,3,4,5,6};
int trigpin=9;
int echopin=8;

int loopCounter=0;

double duration;
double distance;

boolean access=false;
String recvData="";
boolean buzzAlarm=false;

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
  for(int i=0;i<5;i++)pinMode(pins[i],OUTPUT);
  pinMode(trigpin,OUTPUT);
  pinMode(echopin,INPUT);
}


void loop() {
  loopCounter++;
  if(loopCounter==10){
    loopCounter=0;
    }
  if(access==false&&buzzAlarm==false){if(loopCounter==0)Serial.print("0;\n");}
  else if(access==true&&buzzAlarm==false)Serial.print("1;\n");
  else Serial.print("2;\n");
  digitalWrite(trigpin,LOW);
  for(int i=0;i<5;i++)
  {
    digitalWrite(pins[i],LOW);
  }
  if(Serial.available())
  {
    recvData=Serial.readStringUntil('\n');
  }
  if(recvData[0]=='1')
  {
    access=true;
  }
  if(recvData[0]=='2')
  {
    access=false;
    
  }
  
  digitalWrite(trigpin,HIGH);
  delayMicroseconds(10);   //Creating 10 second microPulse
  digitalWrite(trigpin,LOW);
  duration=pulseIn(echopin,HIGH);
  distance=duration*0.034/2;
  //Serial.print(distance);Serial.println(" cm");
  if(access==true)
  {
      if(distance<22&&distance>13){switchOn(2);}
      else if(distance<=13&&distance>6){switchOn(1);}
      else if(distance<=6){switchOn(0);}
      else switchOff();
  }
  else if(access==false)
  {
    
    if(distance<20){
      buzzAlarm=true;
      Serial.print("2;\n");
      digitalWrite(pins[3],HIGH);digitalWrite(pins[4],HIGH);
      delay(400);
      digitalWrite(pins[3],LOW);digitalWrite(pins[4],LOW);
      delay(400);
      
      }
      else
      {
        buzzAlarm=false;
      }
  }
  delay(50);
}
