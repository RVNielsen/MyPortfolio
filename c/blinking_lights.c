#include <Adafruit_CircuitPlayground.h>

const int buttonDecide = 19; // location of button to change between increment/decrement mode
const int buttonChange = 4; // location of button to increment/decrement
const int ledPin = 13;  // light location
const int limit = 5; // how many levels of light flash speed before looping back to 0

int buttonStateD = 0; // is decide button pressed
int buttonStateC = 0; // is change button pressed
int delayTime = 300; // how long to wait
int counter = 0; // current level tracker
int checkD = 0; // has decide button already been tracked as pressed
int checkC = 0; // has change button already been tracked as pressed
bool downUp = 0; // 0 if decrement mode, 1 if increment mode

void setup() {
  // light is an output, buttons are inputs
  pinMode(ledPin, OUTPUT);
  pinMode(buttonChange, INPUT);
  pinMode(buttonDecide, INPUT);
  // used for playTone
  CircuitPlayground.begin();
}

void loop() {
  // check if a button has been pressed
  buttonStateD = digitalRead(buttonDecide);
  buttonStateC = digitalRead(buttonChange);

  if(buttonStateD == HIGH && checkD == 0)
  {
    if(downUp == 0)
    {
      downUp = 1;
    }
    else
    {
      downUp = 0;
    }
    // signal that this button press has been noticed
    checkD = 1;
  }
  else if(buttonStateC == HIGH && checkC == 0)
  {
    if(downUp == 0)
    {
      // decrement counter or loop around and make sound
      if(counter != 0)
      {
      
        counter--;
      }
      else
      {
        counter = limit;
        CircuitPlayground.playTone(1500, 300);
      }
    }
    else if(downUp == 1)
    {
      // increment counter or loop around and make sound
      if(counter != limit)
      {
        counter++;
      }
      else
      {
        counter = 0;
        CircuitPlayground.playTone(1000, 300);
      }
    }
    
    // signal that this button pressed has been noticed
    checkC = 1;
  }

  // if the button is let go, accept new presses
  if(buttonStateD == LOW && checkD == 1)
  {
    checkD = 0;
  }
  if(buttonStateC == LOW && checkC == 1)
  {
    checkC = 0;
  }

  // set the light to the correct state
  if(counter == limit)
  {
    digitalWrite(ledPin, HIGH);
  }
  else if(counter == 0)
  {
    digitalWrite(ledPin, LOW);
  }
  else
  {
    digitalWrite(ledPin, HIGH);
    delay(counter * 100);
    digitalWrite(ledPin, LOW);
    delay(counter * 100);
  }
  
}
