import pygame 
from settings import *
from support import import_folder
from sprites import Generic
from random import randint, choice

class Sky:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.full_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.start_color = [255, 255, 255]
		self.end_color = (38, 101, 189)
		self.cycle_duration = 300  # Duration of the day/night cycle in seconds (e.g., 5 minutes)
		self.elapsed_time = 0
		self.phase = 'day_to_night'  # Initial phase

	def display(self, dt):
		self.elapsed_time += dt
		progress = min(self.elapsed_time / self.cycle_duration, 1)

		if self.phase == 'day_to_night':
			for index, value in enumerate(self.end_color):
				self.start_color[index] = max(value, 255 - (255 - value) * progress)
			if progress >= 1:
				self.phase = 'night_to_day'
				self.elapsed_time = 0
		elif self.phase == 'night_to_day':
			for index, value in enumerate(self.end_color):
				self.start_color[index] = min(255, value + (255 - value) * progress)
			if progress >= 1:
				self.phase = 'day_to_night'
				self.elapsed_time = 0

		self.full_surf.fill(self.start_color)
		self.display_surface.blit(self.full_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

class Drop(Generic):
	def __init__(self, surf, pos, moving, groups, z):
		
		# general setup
		super().__init__(pos, surf, groups, z)
		self.lifetime = randint(400,500)
		self.start_time = pygame.time.get_ticks()

		# moving 
		self.moving = moving
		if self.moving:
			self.pos = pygame.math.Vector2(self.rect.topleft)
			self.direction = pygame.math.Vector2(-2,4)
			self.speed = randint(200,250)

	def update(self,dt):
		# movement
		if self.moving:
			self.pos += self.direction * self.speed * dt
			self.rect.topleft = (round(self.pos.x), round(self.pos.y))

		# timer
		if pygame.time.get_ticks() - self.start_time >= self.lifetime:
			self.kill()

class Rain:
	def __init__(self, all_sprites):
		self.all_sprites = all_sprites
		self.rain_drops = import_folder('./graphics/rain/drops/')
		self.rain_floor = import_folder('./graphics/rain/floor/')
		self.floor_w, self.floor_h =  pygame.image.load('./graphics/world/ground.png').get_size()

	def create_floor(self):
		Drop(
			surf = choice(self.rain_floor), 
			pos = (randint(0,self.floor_w),randint(0,self.floor_h)), 
			moving = False, 
			groups = self.all_sprites, 
			z = LAYERS['rain floor'])

	def create_drops(self):
		Drop(
			surf = choice(self.rain_drops), 
			pos = (randint(0,self.floor_w),randint(0,self.floor_h)), 
			moving = True, 
			groups = self.all_sprites, 
			z = LAYERS['rain drops'])

	def update(self):
		self.create_floor()
		self.create_drops()