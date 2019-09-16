# Подключить нужные для работы библиотеки
from mcpi.minecraft import Minecraft
import mcpi.block as block

# Создаём Minecraft для соединение и взаимолдействия с игрой
mc = Minecraft.create()
# Определяем тякущую позицию игрока
pos = mc.player.getTilePos()
# 
SIZE = 8
# Задаем координаты для постройки
x = pos.x
y = pos.y
z = pos.z
# создаем  каменный блок
mc.setBlocks(x-1, y-1, z-1, 
             x + SIZE + 1, y + SIZE, z + SIZE + 1,
             block.STONE_BRICK.id)
# делаем блок полым внутри
mc.setBlocks(x, y, z,
             x + SIZE-1, y + SIZE-1, z + SIZE-1,
             block.AIR.id)
# # покроем дом крышей
mc.setBlocks(x-1, y + SIZE, z-1,
             x + SIZE + 1, y + SIZE, z + SIZE + 1,
             block.WOOD.id) 
# # покрываем пол ковром
mc.setBlocks(x-1, y-1, z-1,
             x+SIZE+1, y-1, z+SIZE+1,
             block.WOOL.id, 14)
