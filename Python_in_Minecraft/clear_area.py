# Подключить нужные для работы библиотеки
import mcpi.minecraft as minecraft
import mcpi.block as block

# Создаём Minecraft для соединение и взаимолдействия с игрой
mc = minecraft.Minecraft.create()
# Определяем тякущую позицию игрока
pos = mc.player.getTilePos()
# Введем сколько метров кубических под снос
size = 50 
# Сносим площадку
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+size, pos.y+size,
             pos.z+size, block.AIR.id)


