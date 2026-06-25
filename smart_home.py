# Parent class
class SmartDevice:
    def __init__(self, device_name):
        self.device_name = device_name

    def turn_on(self):
        print(self.device_name, "is now ON.")

    def turn_off(self):
        print(self.device_name, "is now OFF.")


# Child class: Smart Light
class SmartLight(SmartDevice):
    def __init__(self, device_name, brightness):
        super().__init__(device_name)
        self.brightness = brightness

    def adjust_brightness(self):
        print(self.device_name, "brightness set to", self.brightness, "%")


# Child class: Smart Thermostat
class SmartThermostat(SmartDevice):
    def __init__(self, device_name, temperature):
        super().__init__(device_name)
        self.temperature = temperature

    def adjust_temperature(self):
        print(self.device_name, "temperature set to", self.temperature, "°C")


# Creating objects
light = SmartLight("Living Room Light", 75)
thermostat = SmartThermostat("Smart Thermostat", 24)


light.turn_on()
light.adjust_brightness()
light.turn_off()

print()

thermostat.turn_on()
thermostat.adjust_temperature()
thermostat.turn_off()