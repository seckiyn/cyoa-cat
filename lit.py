import pygame
import sys
import os
import logging

# CONSTANTS
PATH = os.path.dirname(os.path.abspath(__file__)) # Path of the script
IMG_FOLDER = "img" # Images folder
BIT_LIST = list() # Change this into better container
SPACING = 20 # Spacing of the bits
# LOGGING
logging.basicConfig(format='%(asctime)s %(message)s',\
        datefmt='%m/%d/%Y %I:%M:%S %p', filename="example.log",\
        level=logging.DEBUG)

def log(message, m_type="info"):
    """ Log the messages """
    if m_type == "info":
        logging.info(message)


def get_path(filename, folder=""):
    """ Return the joined path PATH and filename """
    path = os.path.join(PATH, folder, filename)
    log(f"This is get_path, Filename is {filename}, path is {path}")
    return path

def import_image(filename, folder=""):
    """ Will return image and it's rect """
    path_of_the_file = get_path(filename, folder) # Get the path of the file
    picture = pygame.image.load(path_of_the_file) # Load the image
    picture_rect = picture.get_rect() # 
    log(f"This is import_image, Filename is {filename},path of the file is {path_of_the_file}")
    return picture, picture_rect

def blit_image(surface, bsurface, pos):
    """
        Blit an surface into another
        surface: pygame.Surface -> surface to blit into
        bsurface: pygame.Surface -> surface to blit
        pos: pygame.Rect or tuple -> pos of blit
    """
    surface.blit(bsurface, pos)
    log("This is blit_image, Blitting the image")


def blit_file(surface, filename, pos, folder=""):
    """
        Blit an image directly from filename
        surface: pygame.Surface -> surface to blit into
        filename: str -> filename of the image
        pos: pygame.Rect or tuple -> position to blit
        folder: str -> get folder name
    """
    image, image_rect = import_image(filename, folder) # Get image and image_rect
    blit_image(surface, image, pos) # blit image into surface
    log(f"This is blit_file, filename is {filename}, surface is {surface}, pos is {pos}")

def tuple_to_rect(filename, my_tuple):
    """ Transforms a tuple into pygame.Rect object according to file """
    image, image_rect = import_image(filename, IMG_FOLDER) # Get rect of image
    image_rect.x = my_tuple[0] # Set x to the tuple's x
    image_rect.y = my_tuple[1] # Set y to the tuple's y
    return image_rect
def bit(bit_id, filename, title, starting_pos, explanation=""):
    """
        filename: str -> Name of the image of bit
        title: str -> Title of the bit will show on the ha2
        starting_pos: pygame.Rect or tuple -> Position of the bit
        explanation: str -> Long explanation of the bit
        Will return a dict contains of:
            {
            BIT_ID
            SURFACE/FILENAME
            RECT/POS
            TITLE
            EXPLANATION
            }
    """
    my_bit = {
            "bit_id": bit_id,
            "image_name": filename,
            "title": title,
            "pos": starting_pos,
            "exp": explanation
            }
    return my_bit

def create_bit(bit_id, filename, title, starting_pos=None, explanation=""):
    """ Creates a bit and adds it to the BITS list """
    if not starting_pos: # If there's no position given
        if len(BIT_LIST) > 0: # If there's a bit in bit_list starting pos is spaces according to it
            last_pos = BIT_LIST[-1]["pos"]
            last_pos.y = SPACING # TODO: Get the rects center x pos and add this to is
            starting_pos = last_pos
        else:
            starting_pos = tuple_to_rect(filename, (0, 0)) # If there's no last bit starting pos is origin
    else:
        if type(starting_pos) != pygame.Rect:
            try:
                starting_pos = tuple_to_rect(filename, starting_pos) # Try to change iterable object to Rect
            except TypeError as e:
                raise Exception("Cannot create bit " + str(e)) # If cannot translate to Rect raise an exception
    my_bit = bit(bit_id, filename, title, starting_pos, explanation)
    BIT_LIST.append(my_bit) # Add bit to the bit list
    return my_bit # Return the bit
def place_bit(surface, my_bit):
    """
        Get's a bit dict and places it into surface
        surface: pygame.Surface -> Surface to blit into
    """
    filename = my_bit["image_name"]
    pos = my_bit["pos"]
    blit_file(surface, filename, pos, folder=IMG_FOLDER)

def place_all_bits(surface):
    """ Blit all the bits on the surface """
    for my_bit in BIT_LIST:
        place_bit(surface, my_bit)
def get_bit(bit_id):
    """ Gets bit_id and returns corresponding bit """
    pass
