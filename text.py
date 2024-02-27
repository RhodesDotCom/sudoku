import pygame


class Text:
    """Centered Text Class"""
    def __init__(self, text, x, y, font='arialblack', size=30, colour=(0, 0, 0)):
        self.x = x # Horizontal center of box
        self.y = y # Vertical center of box
        # Start PyGame Font
        pygame.font.init()
        font = pygame.font.SysFont(font, size)
        self.text = font.render(text, True, colour)
        self.size = font.size(text)  # (width, height)

    # Draw Method
    def draw(self, screen):
        draw_x = self.x - (self.size[0] / 2.)
        draw_y = self.y - (self.size[1] / 2.)
        coords = (draw_x, draw_y)
        screen.blit(self.text, coords)