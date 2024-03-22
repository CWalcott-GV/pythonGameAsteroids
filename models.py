from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_sprite, wrap_position

UP = Vector2(0, -1)
#negative value points upwards.

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self, surface): #added surface argument, need to know area around which the position is wrapped.
        self.position = wrap_position(self.position + self.velocity, surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius


class Spaceship(GameObject): #calls GameObject constructor with specific image with zero velocity
    #this alters the gameobject so we don't have to make it up in the Asteroids_Game method. This means we can give it more
    #attributes in the future. (hint inertia, hull health, weapons)

    SPIN_SPEED = 3
    MANEUVERABILITY = 3
    ACCELERATION = 0.25
    def __init__(self, position):
        self.direction = Vector2(UP)#default facing direction
        super().__init__(position, load_sprite("spaceship_resize"), Vector2(0))

    def rotate(self, clockwise=True): #Change direction by rotating clockwise or counterclockwise.
        sign = 1 if clockwise else -1
        angle = self.SPIN_SPEED * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface): #needs button press handlers
        angle = self.direction.angle_to(UP) #calculates angle in order to point in same direction as 'angle'
        rotated_surface = rotozoom(self.sprite, angle, 1.0) #angles the image of the sprite
        rotated_surface_size = Vector2(rotated_surface.get_size()) #recalculate using size of 'rotated_surface'
        blit_position = self.position - rotated_surface_size * 0.5 #vector manipulation.
        surface.blit(rotated_surface, blit_position) #using blit_position puts new image on screen

    def accelerate(self): #WE SCHMOOVIN'
        self.velocity += self.direction * self.ACCELERATION


class Asteroid(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite("asteroid"), (0,0))