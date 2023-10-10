# Import necessary libraries and modules
import dht
import machine
import time
import urequests
import network

# Constants
API_KEY = ""  # Enter your ThingSpeak API key here
WIFI_SSID = ""  # Enter your Wi-Fi SSID here
WIFI_PASSWORD = ""  # Enter your Wi-Fi password here


# Define a class for DHT sensor
class DHTSensor:
    def __init__(self, pin):
        self.pin = pin
        self.sensor = dht.DHT11(self.pin)

    def measure(self):
        try:
            self.sensor.measure()
            temperature = self.sensor.temperature()
            humidity = self.sensor.humidity()
            return temperature, humidity
        except Exception as e:
            print(f"Error measuring temperature and humidity: {e}")
            return None, None


# Define a class for managing Wi-Fi connections
class WifiManager:
    def _init_(self, ssid, password):
        self.ssid = ssid
        self.password = password

    def connect(self):
        sta = network.WLAN(network.STA_IF)
        if not sta.isconnected():
            sta.active(True)
            sta.connect(WIFI_SSID, WIFI_PASSWORD)
            print("\nConnecting to Wi-FI...")
            while not sta.isconnected():
                pass
            print("\nWi-Fi connection successful!")
        else:
            print("\nAlready connected to Wi-Fi!")
        return sta


# Define a class for uploading data to ThingSpeak
class ThingSpeakUploader:
    def __init__(self, api_key):
        self.api_key = api_key

    def upload_data_to_thingspeak(self, temperature, humidity):
        try:
            url = (
                f"https://api.thingspeak.com/update?api_key={API_KEY}"
                f"&field1={temperature}"
                f"&field2={humidity}"
            )
            response = urequests.get(url)
            response.close()
            print("\nSending data to ThingSpeak...        ")
            print("Data sent successfully!\n")
        except OSError as e:
            print(f"Network error: {e}")
        except Exception as e:
            print(f"Error sending data to ThingSpeak: {e}")


# Define a class for the IoT device
class IoTDevice:
    def __init__(self):
        self.dht_sensor = DHTSensor(machine.Pin(4))
        self.relay = machine.Pin(2, machine.Pin.OUT)
        self.wifi_manager = WifiManager(WIFI_SSID, WIFI_PASSWORD)
        self.thingspeak_uploader = ThingSpeakUploader(API_KEY)

    def main(self):
        sta = self.wifi_manager.connect()

        print("\nInitiating data transmission to ThingSpeak...\n")

        while True:
            if sta.isconnected():
                temperature, humidity = self.dht_sensor.measure()

                if temperature is not None and humidity is not None:
                    print(f"Temperature: {temperature}ºC")
                    print(f"Humidity: {humidity}%")

                    if temperature > 31 or humidity > 70:
                        self.relay.value(1)
                    else:
                        self.relay.value(0)

                    self.thingspeak_uploader.upload_data_to_thingspeak(
                        temperature, humidity
                    )

            time.sleep(15)


# Run the main loop
if __name__ == "__main__":
    device = IoTDevice()
    device.main()
