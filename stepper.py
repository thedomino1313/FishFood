import time
from discovery import AnalogIO

class Stepper:
    # Define constants
    STEPS_PER_REVOLUTION = 510
    # Define sequence for 28BYJ-48 stepper motor
    seq = [
        [1, 1, 0, 0],
        # [0, 1, 0, 0],
        [0, 1, 1, 0],
        # [0, 0, 1, 0],
        [0, 0, 1, 1],
        # [0, 0, 0, 1],
        [1, 0, 0, 1]
        # [1, 0, 0, 0]
    ]
    
    def __init__(self):
        self.analog = AnalogIO()

    # Function to rotate the stepper motor one step
    def step(self, step_sequence, delay):
        self.analog.digital_signal(0, bool(step_sequence[0]))
        self.analog.digital_signal(1, bool(step_sequence[1]))
        self.analog.digital_signal(2, bool(step_sequence[2]))
        self.analog.digital_signal(3, bool(step_sequence[3]))
        time.sleep(delay)

    def rotate(self, delay, steps, clockwise=True):
        for _ in range(steps):
            for code in (Stepper.seq if clockwise else Stepper.seq[::-1]):
                self.step(code, delay)

    def disconnect(self):
        self.analog.disconnect()

if __name__ == "__main__":
    try:
        stepper = Stepper()
        # stepper.power()
        input()
        # # Set the delay between steps
        delay = 0.01

        # Rotate one revolution forward (clockwise)
        stepper.rotate(delay, 5, clockwise=False)

        # Pause for 2 seconds
        # time.sleep(2)

        # Rotate one revolution backward (anticlockwise)
        # stepper.rotate(delay, 2, clockwise=False)
        
        stepper.disconnect()
    except KeyboardInterrupt:
        stepper.disconnect()