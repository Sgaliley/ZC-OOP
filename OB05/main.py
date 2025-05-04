import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы экрана
WIDTH = 800
HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaga Clone")
clock = pygame.time.Clock()

# Загрузка изображений
player_img = pygame.Surface((50, 40))
player_img.fill(RED)
enemy_img = pygame.Surface((40, 30))
enemy_img.fill(WHITE)
bullet_img = pygame.Surface((5, 15))
bullet_img.fill(WHITE)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.lives = 3

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        self.rect.clamp_ip(screen.get_rect())

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 3)
        self.speedx = random.randrange(-1, 2)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

def show_start_screen():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 64)
    text = font.render("Galaga Game", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
    screen.blit(text, text_rect)
    
    font = pygame.font.Font(None, 32)
    text = font.render("Press any key to start", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
    screen.blit(text, text_rect)
    pygame.display.flip()
    wait_for_key()

def show_game_over_screen(score):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 64)
    text = font.render("GAME OVER", True, RED)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
    screen.blit(text, text_rect)
    
    font = pygame.font.Font(None, 32)
    text = font.render(f"Score: {score}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 + 20))
    screen.blit(text, text_rect)
    
    text = font.render("Press R to restart", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 + 60))
    screen.blit(text, text_rect)
    pygame.display.flip()
    wait_for_restart()

def wait_for_key():
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False

def wait_for_restart():
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                waiting = False

def create_enemies(level):
    for _ in range(10 + level * 5):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

# Основная игровая функция
def game():
    global all_sprites, enemies, bullets
    
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    player = Player()
    all_sprites.add(player)
    
    score = 0
    level = 1
    
    create_enemies(level)
    
    running = True
    while running:
        clock.tick(FPS)
        
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
        
        # Обновление
        all_sprites.update()
        
        # Проверка столкновений пуль и врагов
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 100
            # Добавляем нового врага, если уровень не завершен
            if len(enemies) == 0:
                level += 1
                if level <= 5:
                    create_enemies(level)
                else:
                    # Все уровни пройдены
                    show_game_over_screen(score)
                    return
        
        # Проверка столкновений игрока и врагов
        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            player.lives -= 1
            if player.lives <= 0:
                show_game_over_screen(score)
                return
            else:
                player.rect.centerx = WIDTH / 2
                player.rect.bottom = HEIGHT - 10
        
        # Рендеринг
        screen.fill(BLACK)
        all_sprites.draw(screen)
        
        # Отображение счета и жизней
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}  Lives: {player.lives}  Level: {level}", True, WHITE)
        screen.blit(text, (10, 10))
        
        pygame.display.flip()

# Основной цикл игры
while True:
    show_start_screen()
    game()