import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		#file path either has to be './zelda/graphics/test/player.png' or just graphics/test/player.png'
		self.image = pygame.image.load('./zelda/graphics/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)

		self.direction = pygame.math.Vector2()
		self.speed = 5

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_LEFT]:
			self.direction.x = -1
		elif keys[pygame.K_RIGHT]:
			self.direction.x = 1
		else:
			self.direction.x = 0

	def move(self,speed):
		# Speed must be normalized or else player moves too fast diagonally.
		# This is due to trigonometry. This gets the length of the vector, checks if it
		# has length and then sets it to 1 (a vector of 0 can't be normalized)
		# See: https://youtu.be/QU1pPzEGrqw?si=vALR5kxqrVU2lVH3&t=2225
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.rect.center += self.direction * speed

	def update(self):
		self.input()
		self.move(self.speed)