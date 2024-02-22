import pygame 
from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		#file path either has to be './zelda/graphics/test/rock.png' or just graphics/test/rock.png'
		self.image = pygame.image.load('./zelda/graphics/test/rock.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)