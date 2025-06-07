try:
    import pygame
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "pygame is required for the Xbox controller. Install dependencies via 'pip install -r requirements.txt' (use sudo if necessary)."
    ) from e

class XboxController:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() == 0:
            raise RuntimeError("No Xbox controller found")
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def update(self):
        pygame.event.pump()

    def get_axis(self, axis: int) -> float:
        return self.joystick.get_axis(axis)

    def is_button_pressed(self, button: int) -> bool:
        return self.joystick.get_button(button)
