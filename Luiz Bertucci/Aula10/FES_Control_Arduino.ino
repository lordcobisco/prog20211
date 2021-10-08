
bool st1 = 0;
bool st2 = 0;

void setup() {
  Serial.begin(9600);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  char leitura = Serial.read();  
  if (leitura == 'M'){
       digitalWrite(7, LOW);
       digitalWrite(6, HIGH);
       delay(741);
       digitalWrite(6, LOW);
       delay(741);
       digitalWrite(6, HIGH);
       delay(741);
       digitalWrite(6, LOW);
       delay(741);
       digitalWrite(6, HIGH);
       delay(741);
       digitalWrite(6, LOW);
       delay(741);
       digitalWrite(6, HIGH);
       delay(741);
       digitalWrite(6, LOW);
       delay(741);
  }
  if (leitura == 'A'){
       digitalWrite(6, HIGH);
       digitalWrite(7, LOW);
       delay(741);
       digitalWrite(6, LOW);
       digitalWrite(7, HIGH);
       delay(741);
       digitalWrite(6, HIGH);
       digitalWrite(7, LOW);
       delay(741);
       digitalWrite(6, LOW);
       digitalWrite(7, HIGH);
       delay(741);
       digitalWrite(6, HIGH);
       digitalWrite(7, LOW);
       delay(741);
       digitalWrite(6, LOW);
       digitalWrite(7, HIGH);
       delay(741);
       digitalWrite(6, HIGH);
       digitalWrite(7, LOW);
       delay(741);
       digitalWrite(6, LOW);
       digitalWrite(7, LOW);
       delay(741);
       
    }
  if (leitura == 'H'||'Q'){
       digitalWrite(6, LOW);
       digitalWrite(7, LOW);
  }   
   
}
