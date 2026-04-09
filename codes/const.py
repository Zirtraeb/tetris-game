


COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_PINK = (255, 192, 203)
COLOR_YELLOW = (255, 255, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_CYAN = (0, 255, 255)

COLORS = [COLOR_WHITE, COLOR_RED, COLOR_GREEN, COLOR_BLUE, COLOR_PINK, COLOR_YELLOW, COLOR_ORANGE, COLOR_CYAN]


#G

GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_SIZE = 30


#K
K_UP = "↑ : Rotate"
K_DOWN = "↓ : Soft Drop"
K_SIDES = "← → : Move"
K_SPACE = "Space : Hard Drop"

K_CONTROLS = f"{K_UP}  |  {K_DOWN}  |  {K_SIDES}  |  {K_SPACE}"



#MENU
MENU_OPTION = ["Start Game"]



#S
SHAPES = [

    [[[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]], 
    [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]],
    
    # O-Shape (1 rotation)
    [[[1, 1], [1, 1]]],
    
    # T-Shape (4 rotations)
    [[[0, 1, 0], [1, 1, 1], [0, 0, 0]], 
    [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
    [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
    [[0, 1, 0], [1, 1, 0], [0, 1, 0]]]
]

SIDEBAR_WIDTH = 200




#W
WINDOW_WIDTH = GRID_WIDTH * GRID_SIZE + SIDEBAR_WIDTH
WINDOW_HEIGHT = GRID_HEIGHT * GRID_SIZE


