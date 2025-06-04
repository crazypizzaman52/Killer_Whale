import time
import can
from xbox_controller import XboxController
from sparkmax_controller import SparkMax


def main():
    bus = can.interface.Bus(channel='can0', bustype='socketcan')
    controller = XboxController()
    spark = SparkMax(can_id=1, bus=bus)

    try:
        while True:
            controller.update()
            axis_value = controller.get_axis(1)  # Left joystick Y-axis
            spark.set_duty_cycle(-axis_value)
            angle = spark.get_encoder_degrees()
            print(f"Angle: {angle:.2f} degrees")
            time.sleep(0.02)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
