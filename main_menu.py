import pygame
from settings import *
import sys
import os
from timer import Timer

class MainMenu:
	def __init__(self, start_game):
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font('font/LycheeSoda.ttf', 50)
		self.title_font = pygame.font.Font('font/LycheeSoda.ttf', 100)
		self.start_game = start_game
		self.options = ["Start Game", "Options", "Quit"]
		self.selected_index = 0

		# Load the "Corn" graphic
		base_path = os.path.dirname(os.path.abspath(__file__))
		self.corn_surf = pygame.image.load(os.path.join(base_path, 'graphics/overlay/corn.png')).convert_alpha()

		# Timer for input delay
		self.input_timer = Timer(200)

	def display(self):
		self.display_surface.fill('black')
		# display the title: "PyDew Valley 2" with double the font size 
		title_surf = self.title_font.render("PyDew Valley: GAIC 25", True, 'White')
		title_rect = title_surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
		self.display_surface.blit(title_surf, title_rect)
		
		for index, option in enumerate(self.options):
			color = 'White' if index == self.selected_index else 'Gray'
			text_surf = self.font.render(option, True, color)
			text_rect = text_surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + index * 60))
			self.display_surface.blit(text_surf, text_rect)

			# Draw the "Corn" graphic next to the selected option
			if index == self.selected_index:
				corn_rect = self.corn_surf.get_rect(midright=(text_rect.left - 10, text_rect.centery))
				self.display_surface.blit(self.corn_surf, corn_rect)

	def input(self):
		keys = pygame.key.get_pressed()
		self.input_timer.update()

		if self.input_timer.active:
			return

		if keys[pygame.K_UP]:
			self.selected_index = (self.selected_index - 1) % len(self.options)
			self.input_timer.activate()
		elif keys[pygame.K_DOWN]:
			self.selected_index = (self.selected_index + 1) % len(self.options)
			self.input_timer.activate()
		elif keys[pygame.K_RETURN]:
			if self.selected_index == 0:
				self.start_game()
			elif self.selected_index == 2:
				pygame.quit()
				sys.exit()

	def update(self):
		self.input()
		self.display()
