from abc import ABC, abstractmethod

import pygame

from src.environment.drawer import Drawer
from src.environment.settings import Settings
from src.ui.button import Button
from src.ui.canvas import Canvas
from src.ui.input import InputNumber
from src.ui.label import Label


class GUIInterface(ABC):
    def __init__(self, environment):
        self.environment = environment
        self.canvas = Canvas()
        self.drawer = Drawer(self.canvas, self.environment)
        self.current_x = Settings.BUTTON_PADDING
        self.current_y = Settings.BUTTON_PADDING
        self.buttons = []
        self.inputs = []
        self.labels = []
        self.create_ui()

    @abstractmethod
    def create_ui(self):
        pass

    def tick(self):
        self.drawer.clear_canvas()
        self.drawer.draw_nodes()
        self.draw_sidebar()
        self.draw_buttons()
        self.draw_inputs()
        self.draw_labels()

    def add_button(self, title, callback):
        position = self._get_next_position(Settings.BUTTON_WIDTH, Settings.BUTTON_HEIGHT)
        button = Button(title, position, callback, width=Settings.BUTTON_WIDTH)
        self.buttons.append(button)

    def add_input(self, x, y, width, height, initial_value=0, variable=None):
        position = self._get_next_position(width, height)
        input_number = InputNumber(position[0], position[1], width, height, initial_value, variable=variable)
        self.inputs.append(input_number)

    def add_label(self, text, font_size=Settings.TEXT_SIZE, color=Settings.TEXT_COLOR):
        position = self._get_next_position(Settings.BUTTON_WIDTH, font_size)
        label = Label(position[0], position[1], text, font_size, color)
        self.labels.append(label)

    def draw_sidebar(self):
        sidebar_rect = pygame.Rect(0, 0, Settings.SIDEBAR_WIDTH, self.canvas.get_screen_height())
        pygame.draw.rect(self.drawer.canvas.screen, Settings.SIDEBAR_COLOR, sidebar_rect)

    def draw_summary(self, total_ants):
        if len(self.labels) > 1:
            self.labels[1].text = f"Total ants: {total_ants:,}"
        # self.drawer.draw_summary(total_ants)

    def draw_buttons(self):
        for button in self.buttons:
            button.draw(self.drawer.canvas.screen)

    def draw_inputs(self):
        for input_element in self.inputs:
            input_element.draw(self.drawer.canvas.screen)

    def draw_labels(self):
        for label in self.labels:
            label.draw(self.drawer.canvas.screen)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self._handle_click(event.pos)

    def _handle_click(self, click_position):
        for button in self.buttons:
            if button.rect.collidepoint(click_position):
                button.callback()
                break

        for input_element in self.inputs:
            if input_element.rect.collidepoint(click_position):
                input_element.focus = True
            else:
                input_element.focus = False

    def _get_next_position(self, width, height):
        if self.current_x + width + Settings.BUTTON_PADDING > Settings.SIDEBAR_WIDTH:
            self.current_x = Settings.BUTTON_PADDING
            self.current_y += height + Settings.ROW_PADDING
        position = (self.current_x, self.current_y)
        self.current_x += width + Settings.BUTTON_PADDING
        return position
