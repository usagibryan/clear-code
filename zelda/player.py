import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		#file path has to be './zelda/graphics/test/player.png' in VSCode, why?
		self.image = pygame.image.load('./zelda/graphics/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)