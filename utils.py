from pygame.image import load
from pygame.math import Vector2

import random

def load_sprite(name, with_alpha=True):
    #Sprite loader. follows path of given object name to the asset/sprites/ subfolder.
    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

def wrap_position(position, surface):
    #The method has the spaceship object wrap when the image goes off screen

    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)

def get_random_position(surface):
    #The method pulls a random position using the built-in function of random within randrange for the height
    #and width of surface.


    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height())
    )

def get_random_velocity(min_speed, max_speed):

    #The method will generate a random value between min_speed and max_speed and a random angle between 0 and 360 degrees.
     #Then it will create a vector with that value, rotated by that angle.
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)