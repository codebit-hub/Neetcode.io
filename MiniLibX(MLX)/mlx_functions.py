import pygame
import sys


# --- Core MLX Structure ---
class MLXContext:
	def __init(self):
		"""Initiating windows, hook events"""

		pygame.init()
		self.windows = []
		self.hooks = {}
		self.loop_hook = None
		
