#-All game constants and reusable functions-#
import sys
import time

def AnimatedText(message,speed):
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
AnimatedText(message = str(), speed = float())
