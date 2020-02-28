'''============================================================================

Story board for 1200 x 800 screen resolution

Each level board consist of a list of objects, that occur on the level. 
Including background, player and all other objects that occur in the game, but 
also a next_level object, that plays, when the level is successfully completed.

A level board is a dictionary (Associative array) where the index is a class file 
name found in the game_objects directory, or one of the following pseudo 
classes:
next_level
background
music

An entry in the level board dictionary, has a class file name as index, and a 
dictionary of parameters to create that class object:

<class name> : {'rect': <rect>, 'boundry': <rect>, 'color': <color> ...}

Rhe function story.get_level(level) returns the level dictionary

============================================================================'''
import sys
import pygame
from pygame.locals import *
from common import common, animation
from game_objects import setting

def get_level(level):
    board = getattr(sys.modules[__name__], "Level" + str(level),False)
    if board:
        return board().objects
    else:
        return False

# Level 0 =====================================================================
# This level is not used. However the next_level effect will be played, before 
# the game begins.
class Level0:
  def __init__(self):
    self.objects = {}

# Level 1 =====================================================================
class Level1:
  def __init__(self):
    # Load resources
    music               = common.load_music('Test1.ogg')
    next_level_sound    = False

    background_sprite   = animation.Animate('sky.jpg',( 0,0, setting.screen_width, setting.screen_height))
    player_sprite       = animation.Animate('player.png',(500,500,80,80))
    player_shot_sprite  = animation.Animate('shot.png',(0,0,10,10))
    city_sprite         = animation.Animate('city.png',(0,0,80,80))
    alien_sprite        = animation.Animate("alien-{index}.png",(0,0,100,50))
    alien_bomb_sprite   = animation.Animate('bomb.png',(0,0,40,40))
    alien_shot_sprite   = animation.Animate('alien_shot.png')
    level_sprite        = animation.Animate('level1.png',( 0,0, setting.screen_width, setting.screen_height) )

    player_dead_sound   = common.load_sound('big_bang.wav')
    player_shot_sound   = common.load_sound('shot.wav')
    city_dead_sound     = common.load_sound('city_explosion.wav')
    alien_dead_sound    = False #common.load_sound('small_bang.wav')
    alien_shot_sound    = False #common.load_sound('small_shoot_sound.wav')

    self.objects = [
      {'background': {
        'color': pygame.Color('dodgerblue1'),
        'sprite': '',
      }},
      {'player': {
        'rect'            : (500,500,80,80),
        'sprite'           : player_sprite,
        'boundary'        : (0,300,1000,360),
        'speed'           :  10,
        'sound'           : player_dead_sound,
        'shoot_sound'     : player_shot_sound,
        'shot'            : { 
          'rect': (0,0,10,10), 
          'direction': 90, 
          'speed': 5, 
          'sprite': player_shot_sprite, 
          'sound': player_shot_sound,
        },
      }},
      {'city'         : { 'rect': (10,580,80,80),   'sprite': city_sprite, 'sound': city_dead_sound }},
      {'alien'        : {
        'rect'        : (800,30,100,50),
        'sprite'       : alien_sprite,
        'boundary'    : (0,0,1000,200),
        'speed'       : 2,
        'direction'   : 180,
        'move_pattern': 'horisontal',
        'sound'       : alien_dead_sound,
        'shoot_sound' : alien_shot_sound,
        'bomb'        : { 'rect': (0,0,40,40), 'direction': -90, 'speed': 1, 'sprite': alien_bomb_sprite },
        'shot'        : { 'rect': (0,0,10,10), 'direction': -90, 'speed': 3, 'sprite': alien_shot_sprite },
      }}, 
    ]


