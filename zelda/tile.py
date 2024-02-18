import pygame 
from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		#file path has to be './zelda/graphics/test/rock.png' in VSCode, why?
		self.image = pygame.image.load('./zelda/graphics/test/rock.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)