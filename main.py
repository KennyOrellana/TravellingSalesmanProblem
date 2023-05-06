import sys

import pygame

from src.models.node import Node
from src.ui.canvas import Canvas
from src.ui.manager import Manager


def main():
    pygame.init()

    canvas = Canvas()
    nodes = [
        Node(100, 100),
        Node(200, 200),
        Node(300, 300),
        Node(400, 400),
    ]
    manager = Manager(canvas, nodes)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        canvas.clear()
        manager.draw_nodes()
        pygame.display.update()


if __name__ == "__main__":
    main()
