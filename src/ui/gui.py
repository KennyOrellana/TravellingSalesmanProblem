from src.environment.settings import Settings
from src.models.environment import Environment
from src.ui.button import Button
from src.ui.gui_interface import GUIInterface


class GUI(GUIInterface):

    def create_ui(self):
        self.add_label("AOC", font_size=60, color=Settings.TITLE_COLOR, align='center')
        self.add_label("Ant Colony Optimization", color=Settings.TITLE_COLOR)
        self.add_label("Ants")
        self.add_toggle_button("Start", "Pause", lambda: setattr(Settings, 'PAUSED', not Settings.PAUSED))
        self.add_button("Reset", lambda: setattr(Settings, 'RESET', True))