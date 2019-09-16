# Подключить нужные для работы библиотеки
import mcpi.minecraft as minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing
import time
import datetime
import math

# Функция которая определяет точку на окружности
def findPointOnCircle(cx, cy, radius, angle):
    ''' finds position on the circle '''
    x = cx + math.sin(math.radians(angle)) * radius
    y = cy + math.cos(math.radians(angle)) * radius
    x = int(round(x, 0))
    y = int(round(y, 0))
    return(x,y)

# Создаём Minecraft для соединение и взаимолдействия с игрой
mc = minecraft.Minecraft.create()
# Создаём MinecraftDrawing обЪект для доступа к функциям рисования
mcdrawing = MinecraftDrawing(mc)
# Определяем тякущую позицию игрока
pos = mc.player.getTilePos()
#  Переменные определяющие положение центра окружности
clockMiddle = pos
clockMiddle.y = clockMiddle.y + 25
#  Константы часов
CLOCK_RADIUS = 20
HOUR_HAND_LENGTH = 10
MIN_HAND_LENGTH = 18
SEC_HAND_LENGTH = 20

# Рисуем окружность циферблата часов
mcdrawing.drawCircle(clockMiddle.x, clockMiddle.y, clockMiddle.z,
                     CLOCK_RADIUS, block.DIAMOND_BLOCK.id)

# Запускаем бесконечный цикл
while True:
    # Определяем тякущие время
    timeNow = datetime.datetime.now()
    # часы
    hours = timeNow.hour
    if hours >= 12:
        hours = timeNow.hour - 12
    # минуты
    minutes = timeNow.minute
    # секунды 
    seconds = timeNow.second

    # Стрелка часов
    # Определяем угол поворота стрелки часов
    hourHandAngle = (360 / 12) * hours
    # Определяем точку соприкосновения стрелки с окружностью циферблата
    hourHandX, hourHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y,
                                             HOUR_HAND_LENGTH, hourHandAngle)
    # Рисуем стрелку часов
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z,
                       hourHandX, hourHandY, clockMiddle.z,
                       block.DIRT.id)

    # Стрелка минут
    minHandAngle = (360 / 60) * minutes
    minHandX, minHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y,
                                           MIN_HAND_LENGTH, minHandAngle)
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z-1,
                       minHandX, minHandY, clockMiddle.z-1,
                       block.WOOD_PLANKS.id)

    # Стрелка секунд
    secHandAngle = (360 / 60) * seconds
    secHandX, secHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y,
                                           SEC_HAND_LENGTH, secHandAngle)
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1,
                       secHandX, secHandY, clockMiddle.z+1,
                       block.STONE.id)

    # Секундная задержка
    time.sleep(1)

    # Сотрём стрлки, наложив сверху на них стрелки из AIR блоков.
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z,
                       hourHandX, hourHandY, clockMiddle.z,
                       block.AIR.id)
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z-1,
                       minHandX, minHandY, clockMiddle.z-1,
                       block.AIR.id)
    mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1,
                       secHandX, secHandY, clockMiddle.z+1,
                       block.AIR.id)