import board
import neopixel
import time

NUM_LEDS = 157
BRIGHTNESS = 0.1

pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, brightness=BRIGHTNESS, auto_write=True)

print("Starting LED test...")

try:
    while True:
        pixels.fill((255, 0, 0))
        time.sleep(2)
        pixels.fill((0, 255, 0))
        time.sleep(2)
        pixels.fill((0, 0, 255))
        time.sleep(2)

except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    print("LEDs off. Exiting.")