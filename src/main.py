import time
# Use package-relative imports so running as a module works
from .xbox_controller import XboxController
from .talonsrx_controller import TalonSRXController


def main():
    controller = XboxController()
    talon = TalonSRXController(can_id=1)

    try:
        while True:
            controller.update()
            axis_value = controller.get_axis(1)  # Left joystick Y-axis
            talon.set_percent_output(-axis_value)
            angle = talon.get_encoder_degrees()
            print(f"Angle: {angle:.2f} degrees")
            time.sleep(0.02)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
