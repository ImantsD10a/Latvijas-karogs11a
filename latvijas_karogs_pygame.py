import sys, math, os, pygame

WIDTH, HEIGHT = 600, 350
FPS = 60
DARK_RED = (140, 0, 26)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SOUND_FILENAME = 'fails.wav'
try:
    pygame.mixer.pre_init(44100, -16, 2, 512)
except:
    pass
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('')
clock = pygame.time.Clock()
sound_bounce = None
if os.path.exists(SOUND_FILENAME):
    try:
        sound_bounce = pygame.mixer.Sound(SOUND_FILENAME)
    except:
        pass
circle_radius = 18
circle_x = 40
circle_y = HEIGHT // 2 + 20
speed_x = 180
pulse_base = 36
pulse_amp = 12
pulse_speed = 2.0
running = True

def draw_latvian_flag(surface, top_y, flag_height):
    unit = flag_height / 5.0
    h_top = int(round(unit * 2))
    h_mid = int(round(unit * 1))
    h_bot = flag_height - h_top - h_mid
    w = WIDTH
    x = 0
    pygame.draw.rect(surface, DARK_RED, (x, top_y, w, h_top))
    pygame.draw.rect(surface, WHITE, (x, top_y + h_top, w, h_mid))
    pygame.draw.rect(surface, DARK_RED, (x, top_y + h_top + h_mid, w, h_bot))

while running:
    dt = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    circle_x += speed_x * dt
    bounced = False
    if circle_x + circle_radius >= WIDTH:
        circle_x = WIDTH - circle_radius
        speed_x = -abs(speed_x)
        bounced = True
    if circle_x - circle_radius <= 0:
        circle_x = circle_radius
        speed_x = abs(speed_x)
        bounced = True
    if bounced and sound_bounce is not None:
        try:
            sound_bounce.play()
        except:
            pass

    screen.fill(BLACK)
    flag_top = 0
    flag_height = HEIGHT
    draw_latvian_flag(screen, flag_top, flag_height)
    pygame.draw.circle(screen, WHITE, (int(round(circle_x)), int(round(circle_y))), circle_radius)

    t = pygame.time.get_ticks() / 1000.0
    size = int(round(pulse_base + pulse_amp * math.sin(2 * math.pi * pulse_speed * t)))
    if size < 8:
        size = 8

    pygame.display.flip()

pygame.quit()
sys.exit()
