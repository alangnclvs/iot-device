# iot-device
An IoT device that collects temperature and humidity data from sensors and uploads it to ThingSpeak for remote monitoring.
## IoT Device for Temperature, Humidity, and Relay Control

This Python code implements an IoT device that:

* Measures temperature and humidity using a DHT11 sensor
* Uploads data to ThingSpeak
* Controls a relay based on temperature and humidity readings

### Usage

To use the code, you will need to:

1. Enter your ThingSpeak API key and Wi-Fi SSID and password in the `API_KEY`, `WIFI_SSID`, and `WIFI_PASSWORD` constants, respectively.
2. Connect the DHT11 sensor to pin 4 on your ESP32 board.
3. Connect the relay to pin 2 on your ESP32 board.
4. Upload the code to your ESP32 board.

Once the code is uploaded, the device will start measuring temperature and humidity every 15 seconds and uploading the data to ThingSpeak. The device will also turn on the relay if the temperature is greater than 31 degrees Celsius or the humidity is greater than 70%.

You can monitor the temperature and humidity data on the [ThingSpeak website](https://thingspeak.com/). You can also use the ThingSpeak website to create alerts and notifications based on the temperature and humidity readings.


This code was developed as part of my IoT class at PUC-PR (Pontifical Catholic University of Paraná).
