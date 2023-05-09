from src.environment.settings import Settings
from src.models.environment import Environment
from src.ui.button import Button
from src.ui.gui_interface import GUIInterface


class GUI(GUIInterface):

    def __init__(self, environment=Environment()):
        super().__init__(environment)
        self.start = False

    def create_ui(self):
        self.add_label("Ant Colony Optimization")
        self.add_label("Ants")
        self.add_button("Start", lambda: setattr(Settings, 'PAUSED', not Settings.PAUSED))
        self.add_button("Reset", lambda: setattr(Settings, 'RESET', True))

    def reset(self):
        pass
