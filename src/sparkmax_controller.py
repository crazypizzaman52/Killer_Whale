import can

class SparkMax:
    """Minimal Spark MAX CAN interface"""
    ENCODER_POS_CMD = 0x51
    SET_DUTY_CMD = 0x20

    def __init__(self, can_id: int, bus: can.Bus):
        self.can_id = can_id
        self.bus = bus

    def _send(self, cmd: int, data: bytes = b""):
        arbitration_id = (self.can_id | (cmd << 8))
        msg = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)
        self.bus.send(msg)

    def set_duty_cycle(self, value: float):
        value = max(min(value, 1.0), -1.0)
        # Convert to int16 scaled by 32767
        duty = int(value * 32767)
        data = duty.to_bytes(2, byteorder='little', signed=True)
        self._send(self.SET_DUTY_CMD, data)

    def get_encoder_degrees(self) -> float:
        self._send(self.ENCODER_POS_CMD)
        msg = self.bus.recv(timeout=0.1)
        if msg is None:
            return float('nan')
        raw = int.from_bytes(msg.data[:4], byteorder='little', signed=True)
        # SparkMAX returns rotations*2048 counts/rot.
        rotations = raw / 2048.0
        return rotations * 360.0
