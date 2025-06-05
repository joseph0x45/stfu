# import time
# import board
# import neopixel
# import board
# import digitalio
#
# pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
#
# while True:
#     pixel.fill((255, 0, 0))
#     time.sleep(0.5)
#     pixel.fill((0, 0, 0))
#     time.sleep(0.5)

import board
import digitalio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard_device = Keyboard(usb_hid.devices)

shotcuts = {
    "Teams":[Keycode.CONTROL, Keycode.SHIFT, Keycode.M],
    "Discord":[Keycode.CONTROL, Keycode.SHIFT, Keycode.M],
}
apps = ["Discord", "Teams"]
index = 0
current_app =  apps[index]

app_switch_pin = digitalio.DigitalInOut(board.D0)
app_switch_pin.direction = digitalio.Direction.INPUT
app_switch_pin.pull = digitalio.Pull.UP

mic_toggle_pin = digitalio.DigitalInOut(board.D1)
mic_toggle_pin.direction = digitalio.Direction.INPUT
mic_toggle_pin.pull = digitalio.Pull.UP

while True:
    if not app_switch_pin.value:
        index += 1
        if index == len(apps):
            index = 0
        current_app = apps[index]
        print(f"current app: {current_app}")
        time.sleep(0.5)
    elif not mic_toggle_pin.value:
        keyboard_device.press(*shotcuts[current_app])
        keyboard_device.release_all()
        time.sleep(0.5)
    else:
        time.sleep(0)
