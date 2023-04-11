#Fun little input-generated word search 
import random
import string
import math

LIST_OF_WORDS = ["apples",  "java", "illegal", "agile", "cradle", "michael", "casper"]


X_LENGTH = Y_LENGTH = math.floor(len(max(LIST_OF_WORDS, key=len)) * (.5 * (len(LIST_OF_WORDS))))

GRID_HEIGHT = GRID_LENGTH = X_LENGTH * 2

TAKEN_SPACES = []

DIRECTION_MAP = {"up" : (-1, 0), "down" : (1, 0), "left" : (0,-1), "right" : (0,1)}

def random_alphabet_generator():
    """Randomly generates a single letter from the alphabet 

    Returns:
        str: Randomly picked letter 
    """
    return random.choice(string.ascii_lowercase)

def pretty_print(grid):
    """Prints the grid in an X,Y grid with each row on a new line, each letter space-separated
    Args:
        grid (list): 2D non-empty List
    """
    print("\n".join(' '.join(*zip(*row)) for row in grid))
    
def choose_random_direction():
    
    all_directions = list(DIRECTION_MAP.keys())
    return random.choice(all_directions)
    
    
def calculate_next_coordinates(x,y,direction):
    x_adjustment, y_adjustment = DIRECTION_MAP.get(direction)
    new_x = x + x_adjustment
    new_y = y + y_adjustment
    return new_x, new_y
    
def check_line_of_word(starting_point, word_length, direction):
    """Checks to make sure that the path the word will be on will not collide with another word.

    Args:
        starting_point (tuple): X,Y coordinates
        word_length (_type_): Length of the word
        direction (_type_): Direction the word will be placed; up, down, ect.

    Returns:
        bool: True if the line will not collide. False otherwise.
    """
    starting_x, starting_y = starting_point
    for _ in range(word_length):
        x,y = calculate_next_coordinates(starting_x, starting_y, direction)
        if not available_grid_space(x, y):
            return False
    return True

def available_grid_space(x_loc,y_loc):
    """Checks given x and y coordinates to determine if they have already been used by another word.

    Args:
        x_loc (str): the X coordinate
        y_loc (str): the Y coordinate

    Returns:
        boolean: Returns True if the spot is unused by other words, False if otherwise.
    """
    if len(TAKEN_SPACES) != 0:
        for taken_spot in TAKEN_SPACES:
            taken_x = taken_spot[0]
            taken_y = taken_spot[1]
            if x_loc != taken_x or taken_y != y_loc:
                return True
            else:
                return False
    else:
        return True
    

def generate_coordinates(len_word, direction):
    """Generates coordinates based on the direction and grid height / length

    Args:
        len_word (int): length of the word
        direction (str): direction it'll be printed

    Returns:
        tuple: (X,Y) values
    """
    if direction == "up":
        y_coordinate = random.randrange(GRID_HEIGHT)
        x_coordinate = random.randrange(len_word, GRID_LENGTH)
        if available_grid_space(x_loc=x_coordinate, y_loc=y_coordinate) and check_line_of_word((y_coordinate, x_coordinate), len_word, direction):
            return x_coordinate,y_coordinate
        else:
            print(f"Could not start word at [{x_coordinate}][{y_coordinate}], trying again.")
            
    if direction == "down":
        y_coordinate = random.randrange(GRID_HEIGHT)
        x_coordinate = random.randrange(GRID_LENGTH-len_word)
        if available_grid_space(x_loc=x_coordinate, y_loc=y_coordinate) and check_line_of_word((y_coordinate, x_coordinate), len_word, direction):
            return x_coordinate,y_coordinate
        else:
            print(f"Could not start word at [{x_coordinate}][{y_coordinate}], trying again.")
            
    if direction == "left":
        y_coordinate = random.randrange(len_word, GRID_HEIGHT)
        x_coordinate = random.randrange(GRID_LENGTH)
        if available_grid_space(x_loc=x_coordinate, y_loc=y_coordinate) and check_line_of_word((y_coordinate, x_coordinate), len_word, direction):
            return x_coordinate,y_coordinate
        else:
            print(f"Could not start word at [{x_coordinate}][{y_coordinate}], trying again.")
            
    if direction == "right":
        y_coordinate = random.randrange(GRID_HEIGHT-len_word)
        x_coordinate = random.randrange(GRID_LENGTH)
        if available_grid_space(x_loc=x_coordinate, y_loc=y_coordinate) and check_line_of_word((y_coordinate, x_coordinate), len_word, direction):
            return x_coordinate,y_coordinate
        else:
            print(f"Could not start word at [{x_coordinate}][{y_coordinate}], trying again.")
            
        

def determine_start(word, direction):
    """Determines starting position of the word given the direction
    
        Args:
        word (str): the given word
        direction (str): Random direction (left, right, up, down)

    Returns:
        tuple: X and Y Coordinate of the starting position
    """
    len_word = len(word)
    while True:
        return generate_coordinates(len_word, direction)
        

def populate_grid_with_words(grid):
    """Populuates the grid with words 

    Args:
        grid (2D Array): the 2D, already randomy-filled grid.
    """
    for word in LIST_OF_WORDS:
        word_len = len(word)
        char = 0
        direction = choose_random_direction()
        x,y = determine_start(word, direction)
        print(TAKEN_SPACES)
        while True:
            if char == word_len:
                break
            letter = word[char]
            grid[x][y] = letter
            char +=1
            TAKEN_SPACES.append(tuple((x,y)))
            x,y = calculate_next_coordinates(x,y, direction)


def fill_grid():
    return [[random_alphabet_generator() for x in range(GRID_LENGTH)] for i in range(GRID_HEIGHT)]


if __name__ == "__main__":
    word_grid = fill_grid()
    populate_grid_with_words(word_grid)
    pretty_print(word_grid)
    
