# Подключить нужные для работы библиотеки
from mcpi.minecraft import Minecraft
import mcpi.block as block

# Создаём Minecraft для соединение и взаимолдействия с игрой
mc = Minecraft.create()
# Определяем тякущую позицию игрока
pos = mc.player.getTilePos()
# Задаем координаты для постройки
x = pos.x
y = pos.y
z = pos.z
#  Задаем размеры постройки
width = 5
length = 5
thickness = 2
# создаем  каменный блок
mc.setBlocks(x-thickness, y-1, z-thickness, 
             x + length, y, z + width,
             block.COBBLESTONE.id)
# наполним бассейн внутри
mc.setBlocks(x, y, z,
             x + length-thickness, y, z + width-thickness,
             block.WATER.id)
