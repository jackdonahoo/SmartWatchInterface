# Button Pin Detector for WaveShare RP2040
# This script tests multiple GPIO pins to find which one the button is connected to

from machine import Pin
import time

# Test these common button pins
test_pins = [3, 14, 15, 16, 17, 20, 21, 22]

print("Button Pin Detector")
print("=" * 40)
print("Press the S3 button to detect its pin...")
print()

# Setup all test pins with pull-up resistors
buttons = {}
for pin_num in test_pins:
    try:
        buttons[pin_num] = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        print(f"GP{pin_num}: Initialized")
    except:
        print(f"GP{pin_num}: Failed to initialize")

print()
print("Monitoring... (Press Ctrl+C to stop)")
print("-" * 40)

last_states = {pin: 1 for pin in buttons.keys()}

while True:
    for pin_num, button in buttons.items():
        current_state = button.value()
        
        # Detect change from HIGH to LOW (button press with pull-up)
        if current_state == 0 and last_states[pin_num] == 1:
            print(f"*** BUTTON DETECTED ON GP{pin_num} ***")
        
        # Detect change from LOW to HIGH (button release)
        elif current_state == 1 and last_states[pin_num] == 0:
            print(f"    Button released on GP{pin_num}")
        
        last_states[pin_num] = current_state
    
    time.sleep(0.05)  # Check every 50ms

