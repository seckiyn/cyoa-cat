import pygame
import sys
import os
import logging

PATH = os.path.dirname(os.path.abspath(__file__)) # Path of the script
IMG_FOLDER = "img"
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

def bit(filename, title, starting_pos, explanation=""):
    """
        filename: str -> Name of the image of bit
        title: str -> Title of the bit will show on the ha2
        starting_pos: pygame.Rect or tuple -> Position of the bit
        explanation: str -> Long explanation of the bit
        Will return a dict contains of:
            {
            SURFACE
            RECT/POS
            TITLE
            EXPLANATION
            }
    """
    pass

def place_bit(surface, my_bit):
    """
        Get's a bit dict and places it into surface
        surface: pygame.Surface -> Surface to blit into
    """
    pass
