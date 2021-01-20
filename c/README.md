# Blinking Lights: Adafruit Circuit Playground
This program uses both buttons on the microcontroller as well as the light. The light blinks at a rate determined by information given by the two buttons. The left button controls the mode. When pressed, it switches between increasing and decreasing mode. In increasing mode, if the right button is pressed, the light blinks faster. In decreasing mode, the opposite effect happens. There are 5 frequency levels for the blinking light: on, very slow, slow, fast, very fast, off. When the right button press causes the mode to loop back around (from "off" forward to "on" or "on" back to "off"), a tone sounds on the Adafruit device. When moving from off to on, the tone is higher than from on to off. 
## Installation
This program is intended to be run in Arduino on an Adafruit Circuit Playground:

1.  Connect the Adafruit to a port on the computer

2.  Select verify at the top of the page with the code

3.  Select upload and click the reset button on the Adafruit while Arduino searches for the device

## Usage
Left button press - change mode (increasing or decreasing blinking frequency)

Right button press - move a blinking frequency level up or down depending on the mode 
