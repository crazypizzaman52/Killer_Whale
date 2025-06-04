# Killer_Whale Motor Control

This project demonstrates controlling a REV Spark MAX motor controller and a NEO 550 motor using a Raspberry Pi with a CAN HAT and an Xbox controller. It reads the integrated encoder and prints the position in degrees.

## Requirements
- Python 3
- RS485/CAN HAT configured as `can0`
- An Xbox controller connected via USB or Bluetooth
- REV Spark MAX and NEO 550 wired to the CAN bus

Install Python dependencies:

```bash
pip install -r requirements.txt
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

Move the left joystick to control motor speed. The encoder position is displayed in degrees in the console.

## Notes
- The CAN commands used are simplified and may need adjustment depending on firmware.
- Ensure power and wiring are correct before testing.
