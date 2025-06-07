# Killer_Whale Motor Control

This project demonstrates controlling a CTRE Talon SRX motor controller with a BAG motor and a Versa Planetary encoder using a Raspberry Pi with a CAN HAT and an Xbox controller. It reads the encoder position and prints it in degrees.

## Requirements
- Python 3
- RS485/CAN HAT configured as `can0`
- An Xbox controller connected via USB or Bluetooth
- CTRE Talon SRX with BAG motor and Versa Planetary encoder wired to the CAN bus

Install Python dependencies (including RobotPy's CTRE bindings). When running
the program with `sudo`, the packages must be available for the root
environment as well:

```bash
pip install -r requirements.txt
# or, if running the program with sudo
sudo pip install -r requirements.txt
```

## Running
Enable your CAN interface (example for SocketCAN):

```bash
sudo ip link set can0 up type can bitrate 1000000
```

Run the main script with root privileges to access CAN:

```bash
sudo python3 -m src.main
```

Make sure to use the `-m` flag so Python runs the package modules correctly.

Move the left joystick to control motor speed. The encoder position is displayed in degrees in the console.

## Notes
- The CAN commands used are simplified and may need adjustment depending on firmware.
- Ensure power and wiring are correct before testing.
