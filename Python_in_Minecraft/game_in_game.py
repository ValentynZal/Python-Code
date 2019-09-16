# подключим библиотеки
import mcpi.minecraft as minecraft
import mcpi.block as block
import minecraftstuff
import time
import random
import threading


# констатнты арены
ARENAX = 10
ARENAZ = 20
ARENAY = 3

# функция создающая арену
def createArena(pos):
    # создаем соединение с Майнкрафт
    mc = minecraft.Minecraft.create()
    
    # создаем пол арены
    mc.setBlocks(pos.x - 1 , pos.y, pos.z - 1,
                 pos.x + ARENAX + 1, pos.y - 3, pos.z + ARENAZ + 1,
                 block.GRASS.id)

    # создаем стены арены
    mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1,
                 pos.x + ARENAX + 1, pos.y + ARENAY, pos.z + ARENAZ + 1,
                 block.GLASS.id)
    mc.setBlocks(pos.x, pos.y + 1, pos.z,
                 pos.x + ARENAX, pos.y + ARENAY, pos.z + ARENAZ,
                 block.AIR.id)

# создаем припятствия
# функция реализующая стены
def theWall(arenaPos, wallZPos):
    mc = minecraft.Minecraft.create()

    # создаем подвижную стену
    wallPos = minecraft.Vec3(arenaPos.x, arenaPos.y + 1, arenaPos.z + wallZPos)
    wallBlocks = []
    for x in range(0, ARENAX + 1):
        for y in range(1, ARENAY):
            wallBlocks.append(minecraftstuff.ShapeBlock(x,
                                                        y,
                                                        0,
                                                        block.BRICK_BLOCK.id))
    wallShape = minecraftstuff.MinecraftShape(mc, wallPos, wallBlocks)

    # передвигаем стену вверх-вниз
    while not gameOver:
        wallShape.moveBy(0,1,0)
        time.sleep(1)
        wallShape.moveBy(0,-1,0)
        time.sleep(1)

# функция реализующая речку
def theRiver(arenaPos, riverZPos):
    mc = minecraft.Minecraft.create()
    
    # констатнты реки
    RIVERWIDTH = 4
    BRIDGEWIDTH = 2

    # создаем реку
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos,
                 arenaPos.x + ARENAX, arenaPos.y, arenaPos.z + riverZPos + RIVERWIDTH - 1,
                 block.AIR.id)
    # наполняем реку
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos,
                 arenaPos.x + ARENAX, arenaPos.y - 2, arenaPos.z + riverZPos + RIVERWIDTH - 1,
                 block.WATER.id)
    # создаем мост
    bridgePos = minecraft.Vec3(arenaPos.x, arenaPos.y, arenaPos.z + riverZPos + 1)
    bridgeBlocks = []
    for x in range(0, BRIDGEWIDTH):
        for z in range(0, RIVERWIDTH - 2):
            bridgeBlocks.append(minecraftstuff.ShapeBlock(x,
                                                          0,
                                                          z,
                                                          block.WOOD_PLANKS.id))
    bridgeShape = minecraftstuff.MinecraftShape(mc, bridgePos, bridgeBlocks)

    # перемещаем мост влевло-вправо
    steps = ARENAX - BRIDGEWIDTH
    while not gameOver:
        for left in range(0, steps):
            bridgeShape.moveBy(1,0,0)
            time.sleep(1)
        for right in range(0, steps):
            bridgeShape.moveBy(-1,0,0)
            time.sleep(1)

def theHoles(arenaPos, holesZPos):
    mc = minecraft.Minecraft.create()
    
    # константы ям
    HOLES = 15
    HOLESWIDTH = 3
    
    while not gameOver:
        # создадим ямы которые генерируются случайным образом, а затем исчезают
        holes = []
        # генерим координаты ям
        for count in range(0,HOLES):
            x = random.randint(arenaPos.x, arenaPos.x + ARENAX)
            z = random.randint(arenaPos.z + holesZPos, arenaPos.z + holesZPos + HOLESWIDTH)
            holes.append(minecraft.Vec3(x, arenaPos.y, z))
        # перед тем как открыть яму зачерняем область
        for hole in holes:
            mc.setBlock(hole.x, hole.y, hole.z, block.WOOL.id, 15)
        time.sleep(0.25)
        # открываем яму
        for hole in holes:
            mc.setBlocks(hole.x, hole.y, hole.z,
                         hole.x, hole.y - 2, hole.z,
                         block.AIR.id)
        time.sleep(2)
        # закрываем яму
        for hole in holes:
            mc.setBlocks(hole.x, hole.y, hole.z,
                         hole.x, hole.y - 2, hole.z,
                         block.GRASS.id)
        time.sleep(0.25)

# Функция создающая диаманды
def createDiamonds(arenaPos, number):
    mc = minecraft.Minecraft.create()

    # генерим диаманды
    for diamond in range(0, number):
        x = random.randint(arenaPos.x, arenaPos.x + ARENAX)
        z = random.randint(arenaPos.z, arenaPos.z + ARENAZ)
        mc.setBlock(x, arenaPos.y + 1, z, block.DIAMOND_BLOCK.id)

# ========================================================================
# Главная программа
mc = minecraft.Minecraft.create()

# установим флаг концы игры
gameOver = False

# определяем местоположение арены
arenaPos = mc.player.getTilePos()

#строим арену
createArena(arenaPos)

# создаем подвижную стену
WALLZ = 10
threading.Thread(target=theWall,
        args= (arenaPos, WALLZ),
    ).start()

# создаем реку
RIVERZ = 4
threading.Thread(target=theRiver,
        args= (arenaPos, RIVERZ),
    ).start()

# создаем ямы
HOLESZ = 15
threading.Thread(target=theHoles,
        args= (arenaPos, HOLESZ),
    ).start()

# константы уровней
LEVELS = 3
DIAMONDS = [3,5,9]
TIMEOUTS = [30,25,20]

#переменные уровней и очков
level = 0
points = 0

''' цикл игры '''
while not gameOver:
    # создаем диаманты
    createDiamonds(arenaPos, DIAMONDS[level])
    diamondsLeft = DIAMONDS[level]
    
    # переносим игрока в отправную точку начала игры
    mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)

    # запускаем таймер
    start = time.time()

    # установим флаг прохождения уровня
    levelComplete = False
    ''' цикл уровня '''
    while not gameOver and not levelComplete:
        time.sleep(0.1)

        # игрок ударил блок?
        hits = mc.events.pollBlockHits()
        for hit in hits:
            blockHitType = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
            if blockHitType == block.DIAMOND_BLOCK.id:
                # растворить блок
                mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, block.AIR.id)
                # уменьшить счетчик диамантов
                diamondsLeft = diamondsLeft - 1

        # определим местоположение игрока
        pos = mc.player.getTilePos()
        
        # игрок упал вниз?
        if pos.y < arenaPos.y:
            # вернуть игрока в стартовую точку
            mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)
            
        # игрок собрал все диаманты и достиг края арены?
        if pos.z == arenaPos.z + ARENAZ and diamondsLeft == 0:
            levelComplete = True

        # время истекло?
        secondsLeft = TIMEOUTS[level] - (time.time() - start)
        if secondsLeft < 0:
            gameOver = True
            mc.postToChat("Out of time...")

    # уровень пройден?
    if levelComplete:
        # подсчитываем очки
        # 1 диамант - 1 очко
        # домножить очки на оставшиеся секунды
        points = points + (DIAMONDS[level] * int(secondsLeft))
        mc.postToChat("Level Complete - Points = " + str(points))
        # перейдем к следующему уровню
        level = level + 1
        # если последний уровень - игра окончена
        if level == LEVELS:
            gameOver = True
            mc.postToChat("Congratulations - All levels complete")

# вывести количество очков
mc.postToChat("Game Over - Points = " + str(points))
