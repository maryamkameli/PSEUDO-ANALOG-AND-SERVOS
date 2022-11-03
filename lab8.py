import RPi.GPIO as IO
import time
from numpy import interp
from grove.adc import ADC

IO.setmode(IO.BCM)
IO.setwarnings(False)

class GrovePotentiometerSensor:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC(0x08)
 
    @property
    def angle(self):
        value = self.adc.read(self.channel)
        return value
servo_channel = 12
IO.setup(servo_channel, IO.OUT) # Set the servo channel to be an output
pwm = IO.PWM(servo_channel, 50)# Create a PWM object which operates at 50Hz
pwm.start(2.5) # Start the PWM output with a duty cycle of 2.5% (0.5ms),
#which should cause the servo to move to the 0 position

led_channel = 5
IO.setup(led_channel, IO.OUT)
led = IO.PWM(led_channel, 100)
led.start(0)
potentiometer = GrovePotentiometerSensor(0) 
def potentiometer_read():                                                                           
    # Your code here: Use the potentiometer_adc variable above
    #to read the value of the potentiometer and return it
    return(potentiometer.angle)
    

def main():
    # Your code here: Initialize the PWM channels. Look at servo.py for help.
    # The frequency of the servo channel should be 50Hz
    # The frequency of the LED channel should be 100Hz
    # The initial duty cycle of the servo channel should be 2.5%
    # The initial duty cycle of the LED channel should be 0%
    

    while True:
        pt = potentiometer_read()
        
        duty_cycle = interp(pt, [0, 180], [2.5, 12.5]) # Convert a degrees range (0-180) into a duty cycle range (2.5%-12.5%)
        pwm.ChangeDutyCycle(duty_cycle) # Pass the duty cycle percentage to the PWM channel
         # Allow some time for the servo to reach its target

        duty_cycle1 = interp(pt, [0, 180], [0, 100]) # Convert a degrees range (0-180) into a duty cycle range (2.5%-12.5%)
        led.ChangeDutyCycle(duty_cycle1)
        time.sleep(0.01)
        
           # Convert a degrees range (0-180) into a duty cycle range (2.5%-12.5%)
           # Pass the duty cycle percentage to the PWM channel
            
        # Your code here: Get the potentiometer value (0-999), and convert it to
        # appropriate values for the servo and LED duty cycles
        # The servo needs a duty cycle between 2.5% and 12.5%
        # The LED needs a duty cycle between 0% and 100%
        
        
       

if __name__ == "__main__":
    main()
