import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		# run configuration current working directory
		# self.image = pygame.image.load('./graphics/test/player.png').convert_alpha()
		self.image = pygame.image.load('./zelda/graphics/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)

		self.direction = pygame.math.Vector2()
		self.speed = 5

		self.obstacle_sprites = obstacle_sprites

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

		self.rect.x += self.direction.x * speed
		self.collision('horizontal')
		self.rect.y += self.direction.y * speed
		self.collision('vertical')
		# self.rect.center += self.direction * speed

	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.x > 0: # moving right
						self.rect.right = sprite.rect.left
					if self.direction.x < 0: # moving left
						self.rect.left = sprite.rect.right
		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.y > 0: # moving bottom
						self.rect.bottom = sprite.rect.top
					if self.direction.y < 0: # moving up
						self.rect.top = sprite.rect.bottom
		
		if direction == 'vertical':
			pass

	def update(self):
		self.input()
		self.move(self.speed)