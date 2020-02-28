"""============================================================================


  Alien space ship

  parameters:
    rect      : Start position and size 
    image     : Image
    boundery  : boundary of movement
    speed     : 2
    direction : in degrees 0-359 counting counter clockwise and 0 = right
    axix      : x, y or xy

============================================================================"""
import pygame
import math
import random
from common import globals, common, animation
from game_objects import setting

class Alien:
  def __init__(self, 
    rect, 
    sprite='player.png', 
    crosshair_image='crosshair.png', 
    boundary = False, 
    direction = 0, 
    move_pattern = 'horisontal',
    speed = 1, 
    sound = False,
    shoot_sound = False,
    bomb = False,
    shot = False,
    ):

    self.sprite     = sprite
    self.rect       = pygame.Rect(rect)
    self.speed      = speed
    self.direction  = direction
    if boundary:
      self.boundary = pygame.Rect(boundary)
    else:
      self.boundary = globals.game.rect
    self.bomb       = bomb
    self.shot       = shot
    self.delete     = False

  def draw(self):
    if self.direction > 0:
      globals.game.window.blit(pygame.transform.flip(self.sprite.get_surface(),True,False),self.rect)
    else:  
      globals.game.window.blit(self.sprite.get_surface(),self.rect)
    
  def update(self):
    # Movement
    if common.rect_touch(self.rect, self.boundary):
      self.direction = (self.direction + 180) % 360 // 1

    self.rect = common.move_rect(self.rect, self.direction, self.speed, self.boundary)  

  
  def hit(self, object_type):
    if object_type == 'shot':
      self.delete = True
      globals.game.score += 100
