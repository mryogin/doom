import math

#game settings
RES = WIDTH, HEIGHT = 1600,900
FPS = 60

#настройки персонажа:
PLAYER_POS = 1.5, 5, #minimap
PLAYER_ANGLE = 0 #угол направления персонажа
PLAYER_SPEED = 0.004 #скорость движения
PLAYER_ROT_SPEED = 0.002 #скорость вращения


#настройки рэйкастинга:
FOV = math.pi / 3 #точка соприкосновения луча с препятствием
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS #угол между лучами
MAX_DEPTH = 20

