from GameFrame import Level

class WelcomeScreen(Level):
    """
    Initial Screen for Game
    """
    def __init__(self, screen, joysticks):
        Level._init__(self, screen, joysticks)