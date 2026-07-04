# 1. THE RECEIVER
class SmartBulb:
    def __init__(self, name, starting_brightness):
        self.name = name
        self.brightness = starting_brightness
        self.cct_kelvin = 4000 # Default daylight color

    # The bulb's own ability to change its state
    def dim_to_sleep_mode(self):
        self.brightness = 1
        self.cct_kelvin = 2700 # Warm, relaxing light
        print(f"💡 {self.name} adjusted: Brightness is now {self.brightness}%, Color is {self.cct_kelvin}K.")
    
    #The bulb oFF CODE
    def turn_off(self):
        self.brightness = 0
        self.cct_kelvin = 0
        print(f"The {self.name} is now turned off")


# 2. THE SENDER
class RemoteControl:
    def __init__(self, brand):
        self.brand = brand

    # Here is the interaction! The remote needs to know WHICH bulb to talk to.
    def press_sleep_button(self, target_bulb):
        print(f"🎛️ Remote ({self.brand}) sending sleep signal to {target_bulb.name}...")
        
        # The remote triggers the bulb's method. 
        # It says: "Hey target_bulb, do your dim_to_sleep_mode thing!"
        target_bulb.dim_to_sleep_mode()
    
    #CODE TO SEND THE TURNOFF SIGNAL TO BULB
    def turn_off_signal(self,target_bulb):
        target_bulb.turn_off()


# --- BRINGING THEM TO LIFE ---

# We create the objects
bedroom_light = SmartBulb("Philips 10W", starting_brightness=80)
my_remote = RemoteControl("HomeHub")

# We make them interact
my_remote.press_sleep_button(bedroom_light)
my_remote.turn_off_signal(bedroom_light)