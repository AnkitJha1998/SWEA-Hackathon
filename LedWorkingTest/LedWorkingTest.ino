int pins[4]={2,3,5,6};
void setup() {
  Serial.begin(9600);
  for(int i=0;i<4;i++)pinMode(pins[i],OUTPUT);
}

void loop() {
  for(int i=0;i<4;i++)
  {
    digitalWrite(pins[i],LOW);
  }
  for(int i=0;i<4;i++)
  {
    digitalWrite(pins[i],HIGH);
    delay(500);
    digitalWrite(pins[i],LOW);
  }

}
