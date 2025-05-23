import pygame
from settings import *
import os

class Overlay:
	def __init__(self,player):

		# general setup
		self.display_surface = pygame.display.get_surface()
		self.player = player

		# imports 
		base_path = os.path.dirname(os.path.abspath(__file__))
		overlay_path = os.path.join(base_path, 'graphics/overlay/')
		self.tools_surf = {tool: pygame.image.load(os.path.join(overlay_path, f'{tool}.png')).convert_alpha() for tool in player.tools}
		self.seeds_surf = {seed: pygame.image.load(os.path.join(overlay_path, f'{seed}.png')).convert_alpha() for seed in player.seeds}

	def display(self):

		# tool
		tool_surf = self.tools_surf[self.player.selected_tool]
		tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
		self.display_surface.blit(tool_surf,tool_rect)

		# seeds
		seed_surf = self.seeds_surf[self.player.selected_seed]
		seed_rect = seed_surf.get_rect(midbottom = OVERLAY_POSITIONS['seed'])
		self.display_surface.blit(seed_surf,seed_rect)