# подключаем необходимые библиотеки
import mcpi.minecraft as minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing
import math
import time

# функциия котороя определяет расстояние между 2 точками
def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))
# Константа расстояния
TOO_FAR_AWAY = 15
# Создаём Minecraft для соединение и взаимолдействия с игрой
mc = minecraft.Minecraft.create()
# Создаём MinecraftDrawing обЪект для доступа к функциям рисования
mcdrawing = MinecraftDrawing(mc)
# зададим настроение друга
blockMood = "happy"
# Зададим исходные координаты друга
friend = mc.player.getTilePos()
friend.x = friend.x + 5
friend.y = mc.getHeight(friend.x, friend.z)
# Создаем друга
mc.setBlock(friend.x, friend.y, friend.z,
            block.DIAMOND_BLOCK.id)
# Первая фраза нашего друга
mc.postToChat("<block> hello friend!")
# Задаем направление движения(координаты) для нашего друга
target = friend.clone()

while True:
    # Определяем местоположение игрока
    pos = mc.player.getTilePos()
    # Определяем расстояние между игроком и другом
    distance = distanceBetweenPoints(pos, friend)

    # блок кода который исходя из расстояния определяет настроение друга
    if blockMood == "happy":
        if distance < TOO_FAR_AWAY:
            target = pos.clone()
        elif distance >= TOO_FAR_AWAY:
            blockMood = "sad"
            mc.postToChat("<block> You are to far(( \
                          Come back to me!")
    elif blockMood == "sad":
        if distance <= 1:
            blockMood = "happy"
            mc.postToChat("<block> Thanks, bro. Let`s go))")

    if friend != target:
        # сохраняем маршрут
        blocksBetween = mcdrawing.getLine(friend.x, friend.y, friend.z,
                                          target.x, target.y, target.z)
        # перемещаем друга по маршруту в цикле шаг за шагом
        for blockBetween in blocksBetween[:-1]:
            # подчистим сьарое местоположение друга
            mc.setBlock(friend.x, friend.y, friend.z, 
                        block.AIR.id)
            # определяем координаты координаты шага
            friend = blockBetween.clone()
            friend.y = mc.getHeight(friend.x, friend.z)
            # переносим друга согласно новым координатам
            mc.setBlock(friend.x, friend.y, friend.z, 
                        block.DIAMOND_BLOCK.id)
            # задержечка - определяет скорость друга
            time.sleep(0.25)
        # Задаем новое направление  для нашего друга
        target = friend.clone()

    time.sleep(0.25)