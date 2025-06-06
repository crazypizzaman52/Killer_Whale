import ctre


class TalonSRXController:
    """Minimal interface for a Talon SRX motor controller"""

    def __init__(self, can_id: int):
        self.motor = ctre.WPI_TalonSRX(can_id)
        self.motor.configFactoryDefault()
        self.motor.setInverted(False)
        self.counts_per_rev = 4096  # Versa Planetary encoder counts per revolution

    def set_percent_output(self, value: float):
        value = max(min(value, 1.0), -1.0)
        self.motor.set(ctre.ControlMode.PercentOutput, value)

    def get_encoder_degrees(self) -> float:
        counts = self.motor.getSelectedSensorPosition()
        return counts * 360.0 / self.counts_per_rev
