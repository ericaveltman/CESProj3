#include <WebServer.h>
#include <WiFi.h>
#include <WiFiUdp.h>

// the IP of the machine to which you send msgs - this should be the correct IP in most cases (see note in python code)
#define CONSOLE_IP "192.168.1.2"
#define CONSOLE_PORT 4210
const char* ssid = "ESP32";
const char* password = "12345678";
WiFiUDP Udp;
IPAddress local_ip(192, 168, 1, 1);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);
WebServer server(80);

int photoResistor = 33;
int switch1 = 18;

void setup() {
  Serial.begin(115200);
  
  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  server.begin();
  
//pinMode(photoResistor, INPUT_PULLUP);
pinMode(switch1, INPUT_PULLUP);

}

void loop() {

int switchVal = digitalRead(switch1);
int lightVal = analogRead(photoResistor);
//Serial.print(lightVal);
//Serial.print('\n');

  Udp.beginPacket(CONSOLE_IP, CONSOLE_PORT);
  Udp.print(String(lightVal) + "," + String(switchVal));
  //Udp.print(String(switchVal).c_str());
  Udp.endPacket();
//  Serial.print(lightVal);
//  Serial.print('\n');


delay(1000);
}
