import time
from discovery import AnalogIO

class Stepper:
    # Define constants
    DEG_PER_STEP = 1.8
    STEPS_PER_REVOLUTION = int(360 / DEG_PER_STEP)
    # Define sequence for 28BYJ-48 stepper motor
    seq = [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1]
        # [1, 0, 0, 0],
        # [0, 1, 0, 0],
        # [0, 0, 1, 0],
        # [0, 0, 0, 1],
    ]
    
    def __init__(self):
        self.analog = AnalogIO()

    # Function to rotate the stepper motor one step
    def step(self, step_sequence):
        self.analog.digital_signal(0, bool(step_sequence[0]))
        self.analog.digital_signal(1, bool(step_sequence[1]))
        self.analog.digital_signal(2, bool(step_sequence[2]))
        self.analog.digital_signal(3, bool(step_sequence[3]))

    def rotate(self, delay, steps, clockwise=True):
        for _ in range(steps):
            for code in (Stepper.seq if clockwise else Stepper.seq[::-1]):
                self.step(code)
                self.analog.probe_inputs()
            time.sleep(delay)

    def disconnect(self):
        self.analog.disconnect()

# if __name__ == "__main__":
#     try:
#         stepper = Stepper()

#         # # Set the delay between steps
#         delay = 1

#         # while True:
#         #     # Rotate one revolution forward (clockwise)
#         stepper.rotate(delay, 2, clockwise=True)

#         # Pause for 2 seconds
#         time.sleep(2)

#         # Rotate one revolution backward (anticlockwise)
#         stepper.rotate(delay, 2, clockwise=False)
        
#         stepper.disconnect()
#     except KeyboardInterrupt:
#         stepper.disconnect()