import RPi.GPIO as IO
import time
from numpy import interp
 
IO.setmode(IO.BCM)
IO.setwarnings(False)

servo_channel = 12
IO.setup(servo_channel, IO.OUT) # Set the servo channel to be an output
pwm = IO.PWM(servo_channel, 50) # Create a PWM object which operates at 50Hz
pwm.start(2.5) # Start the PWM output with a duty cycle of 2.5% (0.5ms), which should cause the servo to move to the 0 position

while True:
    for i in range(181):
        duty_cycle = interp(i, [0, 180], [2.5, 12.5]) # Convert a degrees range (0-180) into a duty cycle range (2.5%-12.5%)
        pwm.ChangeDutyCycle(duty_cycle) # Pass the duty cycle percentage to the PWM channel
        time.sleep(0.01) # Allow some time for the servo to reach its target
