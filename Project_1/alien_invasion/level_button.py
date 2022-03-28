import pygame.font

class Level_button:

    def __init__(self, ai_game, x, y, msg):
        """Initialize level button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 100, 100
        self.button_color = (0, 255, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 34)

        # build the buttons rect object
        self.rect = pygame.Rect(x, y, self.width, self.height)

        # Get button rect x and y positions 
        self.x = self.rect.x
        self.y = self.rect.y

        # prepare button message 
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """"Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_level_button(self):
        """Draw blank button then draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)