class Comet(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("comet.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.x = 0
        self.y = 0
        self.dx = 2
        self.dy = 2
        self.mass = 10
        self.distance = 0
        self.angle = 0

    def rotate(self):
        last_center = self.rect.center
        self.image = pg.transform.rotate(self.image_copy, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = last_center

    def stpoint_set(self):
        rand = random.randint(1, 4)
        if rand == 1:
            self.y = 0
            self.x = random.randint(0, 320)
            self.angle = 0
        elif rand == 2:
            self.x = 640
            self.y = random.randint(0, 450)
            self.angle = 90
        elif rand == 3:
            self.x = random.randint(270, 640)
            self.y = 800
            self.angle = 180
        elif rand == 4:
            self.x = 0
            self.y = random.randint(350, 800)
            self.angle = 90

    def fly(self):
        last_center = (self.x, self.y)
        self.x += self.dx
        self.y += self.dy
        pg.draw.line(self.background, WHITE, last_center, (self.x, self.y))

    def gravity(self, satellite):
        """Calculate impact of gravity on the satellite."""
        G = 1.0  # gravitational constant for game
        dist_x = self.x - satellite.x
        dist_y = self.y - satellite.y
        distance = math.hypot(dist_x, dist_y)
        # normalize to a unit vector
        dist_x /= distance
        dist_y /= distance
        # apply gravity
        force = G * (satellite.mass * self.mass) / (math.pow(distance, 2))
        satellite.dx += (dist_x * force)
        satellite.dy += (dist_y * force)

    def update(self):
        self.fly()


