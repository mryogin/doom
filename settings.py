import math

#game settings
RES = WIDTH, HEIGHT = 1600,900
FPS = 60
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2


#настройки персонажа:
PLAYER_POS = 1.5, 5, #minimap
PLAYER_ANGLE = 0 #угол направления персонажа
PLAYER_SPEED = 0.004 #скорость движения
PLAYER_ROT_SPEED = 0.002 #скорость вращения
PLAYER_SIZE_SCALE = 60

# mouse settings
MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30,30,30)

#настройки рэйкастинга:
FOV = math.pi / 3 #точка соприкосновения луча с препятствием
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS #угол между лучами
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

# настройки текстур
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2


