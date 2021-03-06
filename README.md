# CESProj3

This project is a music "box" that plays different sounds depending on the amount of light in the room. If it is dark, it plays ocean sounds (like you would use to fall asleep) and if its light, it plays upbeat music (that can be nice to have playing in the background during the day).

## What You Need 
### Software
- Python 3
- Arduino IDE<br />

### Hardware
- ESP32
- switch
- photoresistor
- 10k resistor
- battery

### Connections:
Photoresistor: One end is connected to GPIO 33 via a jumper cable and the other end is connected to Ground. A 10k resistor is placed along the same rail as the photoresistor and the other end is attached to power. <br/>
Switch: The center pin is connected to Ground and one of the other pins is connected to GPIO 18.<br/>
## How To Run (Step by Step):
### ESP32 code<br />
Upload the .ino file to your ESP32 (or other micro controller). 
### Python
Download the simpleaudio library using the command <br>
`pip install simpleaudio` <br>

The way the code is written, you have to have the wav files in the same folder as the python script. You can change the files as you please, as long as you replace file name. Note: Only .wav files work
