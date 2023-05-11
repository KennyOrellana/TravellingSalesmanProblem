from src.environment.settings import Settings
from src.ui.gui_interface import GUIInterface


class GUI(GUIInterface):

    def on_click_demo(self):
        Settings.DEMO = not Settings.DEMO
        Settings.RESET = True
        Settings.DELAY = Settings.DELAY_DEFAULT

    def create_ui(self):
        self.add_label("ACO", font_size=60, color=Settings.TITLE_COLOR, align='center')
        self.add_label("Ant Colony Optimization", color=Settings.TITLE_COLOR)
        self.add_label("Total ants")
        self.add_label("Distance")
        self.add_toggle_button("Start", "Pause", lambda: setattr(Settings, 'PAUSED', not Settings.PAUSED))
        self.add_button("Reset", lambda: setattr(Settings, 'RESET', True))
        self.add_label("")  # Just to add space
        if Settings.DEMO:
            self.add_button("Demo Mode: ON", self.on_click_demo, width=Settings.BUTTON_WIDTH_FULL)
        else:
            self.add_button("Demo Mode: OFF", self.on_click_demo, width=Settings.BUTTON_WIDTH_FULL)
