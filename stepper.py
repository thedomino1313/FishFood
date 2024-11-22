import time
from discovery import AnalogIO
import uvicorn

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

# Function to rotate the stepper motor one step
def step(analog_device: AnalogIO, step_sequence):
    analog_device.digital_signal(0, bool(step_sequence[0]))
    analog_device.digital_signal(1, bool(step_sequence[1]))
    analog_device.digital_signal(2, bool(step_sequence[2]))
    analog_device.digital_signal(3, bool(step_sequence[3]))

def rotate(delay, steps, analog_device: AnalogIO, clockwise=True):
    for _ in range(steps):
        for code in (seq if clockwise else seq[::-1]):
            step(analog_device, code)
            analog_device.probe_inputs()
        time.sleep(delay)

if __name__ == "__main__":
    uvicorn.run("frontend.app:app",host="localhost", port = 8001,reload=True)
    # try:
    #     analog = AnalogIO()

    #     # # Set the delay between steps
    #     delay = 1

    #     # while True:
    #     #     # Rotate one revolution forward (clockwise)
    #     rotate(delay, 2, analog, clockwise=True)

    #     # Pause for 2 seconds
    #     time.sleep(2)

    #     # Rotate one revolution backward (anticlockwise)
    #     rotate(delay, 2, analog, clockwise=False)
        
    #     analog.disconnect()
    # except KeyboardInterrupt:
    #     analog.disconnect()