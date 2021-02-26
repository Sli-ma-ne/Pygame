import pygame
import random


class Button:  # кнопки
    def __init__(self, w, h, kartinka1, kartinka2):
        self.w = w
        self.h = h
        self.k1 = kartinka1
        self.k2 = kartinka2
        
    def draw(self, x, y):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x < mouse[0] < x + self.w and y < mouse[1] < y + self.h:
                screen.blit(self.k2, (x, y))
                if click[0] == 1:
                    if zvyk.f:
                        pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300)
                    return True
                else:
                    return False
        else:
            screen.blit(self.k1, (x, y))
            return False
        
        
class ButtonMYZ:  # кнопки
    def __init__(self, w, h, kartinka1, kartinka2, kartinka11, kartinka22):
        self.w = w
        self.h = h
        self.k1 = kartinka1
        self.k2 = kartinka2
        self.k11 = kartinka11
        self.k22 = kartinka22
        self.f = True        
        
    def draw(self, x, y):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x < mouse[0] < x + self.w and y < mouse[1] < y + self.h:
                screen.blit(self.k2, (x, y))
                if click[0] == 1:
                    if zvyk.f:
                        pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300)
                    self.k1, self.k11 = self.k11, self.k1
                    self.k2, self.k22 = self.k22, self.k2
                    if self.f:
                        pygame.mixer.music.pause()
                        self.f = False
                    else:
                        pygame.mixer.music.unpause()
                        self.f = True
                    return True
                else:
                    return False
        else:
            screen.blit(self.k1, (x, y))
            return False
        
        
class ButtonZVYK:  # кнопки
    def __init__(self, w, h, kartinka1, kartinka2, kartinka11, kartinka22):
        self.w = w
        self.h = h
        self.k1 = kartinka1
        self.k2 = kartinka2
        self.k11 = kartinka11
        self.k22 = kartinka22
        self.f = True        
        
    def draw(self, x, y):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x < mouse[0] < x + self.w and y < mouse[1] < y + self.h:
                screen.blit(self.k2, (x, y))
                if click[0] == 1:
                    self.k1, self.k11 = self.k11, self.k1
                    self.k2, self.k22 = self.k22, self.k2
                    if self.f:
                        self.f = False
                    else:
                        pygame.mixer.Sound.play(button_sound)                      
                        self.f = True
                    pygame.time.delay(300)  
                    return True
                else:
                    return False
        else:
            screen.blit(self.k1, (x, y))
            return False


class preg:
    def __init__(self, t, pol):
        self.preg = pygame.image.load('data/preg.png')
        self.pol = [110, 225, 340][pol]
        self.a = -50
        self.t = t
        
    def ris(self, t):  # рисуем
        if self.t <= t // 10 % 50 and self.a < 800:
            self.a += 5
            screen.blit(self.preg, (self.pol, self.a))
            
        #x, y, h, w, sppreg = self.cord()
        #sppreg = [(0, 0, -25, 0), (15, 0, 0, -15)] 
        #for i in sppreg:
            #pygame.draw.rect(screen, GREEN, (x + i[0], y + i[1], w - x + i[3] - i[0], h - y - i[1] + i[2] ), 2)         
            
    def cord(self):  # координаты
        return [self.pol, self.a, self.a + 50, self.pol + 100, [(0, 0, -25, 0), (15, 0, 0, -15)]] 


class car:
    def __init__(self, t, pol):
        n = random.randint(1, 3)
        if n == 1:
            self.car = pygame.image.load('data/car1.png')
        elif n == 2:
            self.car = pygame.image.load('data/car2.png')
        elif n == 3:
            self.car = pygame.image.load('data/car3.png')            
        self.pol = [115, 230, 345][pol]
        self.a = -200
        self.t = t
        
    def ris(self, t):  # рисуем
        if self.t <= (t // 10) % 50 and self.a < 900:
            self.a += 10
            screen.blit(self.car, (self.pol, self.a)) 
            
        #x, y, h, w, spcar = self.cord()
        #spcar = [(0, 10, -20, 0), (5, 5, -15, -5), (10, 0, -10, -10), (15, 0, -5, -15), (25, 0, 0, -25)] 
        #for i in spcar:
            #pygame.draw.rect(screen, GREEN, (x + i[0], y + i[1], w - x + i[3] - i[0], h - y - i[1] + i[2] ), 2)    
            
    def cord(self):  # координаты машин на дороге
        return [self.pol, self.a, self.a + 175, self.pol + 90, [(0, 10, -20, 0), (5, 5, -15, -5), (10, 0, -10, -10), (15, 0, -5, -15), (25, 0, 0, -25)]]    
            
            
def slimane():
    logof = pygame.image.load('data/logo/logof.png')
    SLIMANE = []
    SLIMANE.append((pygame.image.load('data/logo/S.png'), (111, 290)))
    SLIMANE.append((pygame.image.load('data/logo/L.png'), (159, 290)))
    SLIMANE.append((pygame.image.load('data/logo/I.png'), (207, 290)))
    SLIMANE.append((pygame.image.load('data/logo/M.png'), (239, 290)))
    SLIMANE.append((pygame.image.load('data/logo/A.png'), (287, 290)))
    SLIMANE.append((pygame.image.load('data/logo/N.png'), (335, 290)))
    SLIMANE.append((pygame.image.load('data/logo/E.png'), (383, 290)))  
    studios = pygame.image.load('data/logo/studios.png')    
    for i in range(551, 103, -8):
        clock.tick(300)
        screen.blit(logof, (95, 274))
        screen.blit(SLIMANE[0][0], (i, 290))
        pygame.display.flip()
    for i in range(551, 151, -8):
        clock.tick(300)
        screen.blit(logof, (95, 274))
        screen.blit(*SLIMANE[0])
        screen.blit(SLIMANE[1][0], (i, 290))
        pygame.display.flip()
    for i in range(551, 199, -8):
        clock.tick(300)
        screen.blit(logof, (95, 274))
        for j in range(2):
            screen.blit(*SLIMANE[j])
        screen.blit(SLIMANE[2][0], (i, 290))
        pygame.display.flip() 
    for i in range(551, 231, -8):
        clock.tick(300)
        screen.blit(logof, (95, 274))
        for j in range(3):
            screen.blit(*SLIMANE[j])
        screen.blit(SLIMANE[3][0], (i, 290))
        pygame.display.flip() 
    for i in range(551, 279, -8):
        clock.tick(300)
        screen.blit(logof, (95, 274))
        for j in range(4):
            screen.blit(*SLIMANE[j])
        screen.blit(SLIMANE[4][0], (i, 290))
        pygame.display.flip() 
    for i in range(551, 327, -8):
        clock.tick(300)
        screen.blit(logof, (95, 274))
        for j in range(5):
            screen.blit(*SLIMANE[j])
        screen.blit(SLIMANE[5][0], (i, 290))
        pygame.display.flip() 
    for i in range(551, 375, -8):
        clock.tick(300)
        screen.blit(logof, (95, 274))
        for j in range(6):
            screen.blit(*SLIMANE[j])
        screen.blit(SLIMANE[6][0], (i, 290))
        pygame.display.flip() 
    for i in range(551, 127, -8):
        clock.tick(300)
        screen.blit(logof, (95, 274))
        for j in range(7):
            screen.blit(*SLIMANE[j])
        screen.blit(studios, (i, 354))
        pygame.display.flip()
    pygame.time.delay(300)


def prov(xyhw, x12):  # проверяем аварию
    spcarvip = [(0, 20, -20, 0), (5, 10, -5, -5), (10, 5, 0, -10), (15, 0, 0, -15)] 
    x2, y2, h2, w2, m = xyhw
    y12, h12, w12 = 500, 675, x12 + 90
    for i in spcarvip:
        for j in m:
            x1 = x12 + i[0]
            y1 = y12 + i[1]
            w1 = w12 + i[3]
            h1 = h12 + i[2]
            x = x2 + j[0]
            y = y2 + j[1]
            w = w2 + j[3]
            h = h2 + j[2]            
            if x1 < x < w1:
                if y1 < y < h1:
                    return True
            if x1 < w < w1:
                if y1 < h < h1:
                    return True
            if x < x1 < w:
                if y < h1 < h:
                    return True
            if x < w1 < w:
                if y < y1 < h:
                    return True
            if x == x1 and w == w1 and y1 < h < h1:
                    return True     
    return False


def ris():  # рисуем
    global a, x, time
    a = (a + 5) % 500
    screen.blit(bg, (0, a))
    screen.blit(bg, (0, a - 500))
    screen.blit(bg, (0, a + 500))
    screen.blit(carvip, (x, 500))
    # ###############################################################################################################
    # rescarvip(x)
    # ##################################################################################################################
    for i in carta:
        i.ris(time)
    for i in carta:
        if prov(i.cord(), x):
            screen.blit(bym, (x - 5, 480))
            pygame.display.flip()
            if zvyk.f:
                pygame.mixer.Sound.play(bymz)
            pygame.time.delay(300)            
            while True:
                screen.blit(zas, (75, 150))
                timrec = [i.strip() for i in open('data/data.txt')][0]
                if time // 10 > int(timrec):
                    f1 = pygame.font.Font(None, 36)
                    text1 = f1.render(f'Новый рекорд: {time // 10}', 1, (0, 0, 0))
                    screen.blit(text1, (182, 190))  
                else:
                    # pygame.draw.rect(screen, (100, 100, 100), (465, 10, 80, 35))
                    f1 = pygame.font.Font(None, 36)
                    text1 = f1.render(f'Ваш счет: {time // 10}', 1, (0, 0, 0))
                    screen.blit(text1, (182, 190))   
                
                    # pygame.draw.rect(screen, (100, 100, 100), (465, 90, 80, 35))
                    text3 = f1.render(f'Рекорд: {timrec}', 1, (0, 0, 0))
                    screen.blit(text3, (182, 240))                

                if menu.draw(182, 420):
                    if time // 10 > int(timrec):
                        print(str(time // 10), file=open("data/data.txt", "w"))
                    gmenu()
                    break
                if zanovo.draw(182, 310):
                    if time // 10 > int(timrec):
                        print(str(time // 10), file=open("data/data.txt", "w"))                    
                    igra()
                    break 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                clock.tick(FPS)
                pygame.display.flip()
            break
    pygame.draw.rect(screen, (100, 100, 100), (465, 10, 80, 35))
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(str(time // 10), 1, (255, 255, 255))
    screen.blit(text1, (544 - (len(str(time // 10))) * 14, 15))
    
    pygame.draw.rect(screen, (100, 100, 100), (465, 60, 80, 35))
    f2 = pygame.font.Font(None, 26)
    text2 = f2.render('Рекорд:', 1, (255, 255, 255))
    screen.blit(text2, (470, 65))
    
    timrec = [i.strip() for i in open('data/data.txt')][0]
    pygame.draw.rect(screen, (100, 100, 100), (465, 90, 80, 35))
    text3 = f1.render(timrec, 1, (255, 255, 255))
    screen.blit(text3, (540 - (len(timrec)) * 14, 95))
        
    


def igra():  # Цикл игры
    global a, x, time, carta
    x = 230     
    a = 0
    time = 0      
    pygame.key.get_pressed()
    carta = []
    n = random.randint(0, 2)
    for i in carti[n]:
        if i[0] == preg:
            carta.append(preg(*i[1]))
        elif i[0] == car:
            carta.append(car(*i[1]))
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 105:
            x -= 5
        elif keys[pygame.K_RIGHT] and x < 355:
            x += 5
        if keys[pygame.K_ESCAPE]:
            while True:
                pygame.event.get()
                keys = pygame.key.get_pressed()
                if not keys[pygame.K_ESCAPE]:
                    pygame.event.get()
                    break                
            while True:
                screen.blit(zas, (75, 150))
                if igrat.draw(182, 200):
                    break
                if menu.draw(182, 310):
                    gmenu()
                    break
                if zanovo.draw(182, 420):
                    igra()
                    break                
                
                pygame.display.flip()
                

                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    pygame.event.get()
                    pygame.time.delay(300)
                    break
        else:
            ris()
            time += 1
            pygame.display.flip()
        if time % 500 == 0:
            carta = []
            n = random.randint(0, 2)
            for i in carti[n]:
                if i[0] == preg:
                    carta.append(preg(*i[1]))
                elif i[0] == car:
                    carta.append(car(*i[1]))            
    return


def gmenu():
    while True:
        clock.tick(300)
        screen.blit(fon, (-157, -100))
        myz.draw(182, 365)
        zvyk.draw(312, 365)
        if igrat.draw(182, 255):
            igra()
        if prav.draw(182, 475):
            while True:
                screen.blit(zas, (75, 150))
                
                f1 = pygame.font.Font(None, 24)
                text1 = f1.render('Управление стрелками (влево, вправо).', 1, (0, 0, 0))
                screen.blit(text1, (90, 200)) 
                
                text1 = f1.render('Объезжайте препятствия и встречные машины.', 1, (0, 0, 0))
                screen.blit(text1, (90, 225)) 
                
                text1 = f1.render('Если вы врежетесь, то машина не сможет', 1, (0, 0, 0))
                screen.blit(text1, (90, 250))   
                
                text1 = f1.render('продолжить движение.', 1, (0, 0, 0))
                screen.blit(text1, (90, 270))     
                
                text1 = f1.render('Ваша задача проехать как можно больше.', 1, (0, 0, 0))
                screen.blit(text1, (90, 295))    
                
                text1 = f1.render('Желаем удачи!', 1, (0, 0, 0))
                screen.blit(text1, (90, 320))                    
                
                if menu.draw(182, 420):
                    gmenu()
                    break             
                
                pygame.display.flip()
                

                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    pygame.event.get()
                    pygame.time.delay(300)
                    break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        
        pygame.display.update()    
        
    
    
def rescarvip(x):
    y, h, w = 500, 675, x + 90
    spcarvip = [(0, 20, -20, 0), (5, 10, -5, -5), (10, 5, 0, -10), (15, 0, 0, -15)] 
    for i in spcarvip:
        pygame.draw.rect(screen, GREEN, (x + i[0], y + i[1], w - x + i[3] - i[0], h - y - i[1] + i[2] ), 2)    



WIDTH = 550
HEIGHT = 700
FPS = 30
    
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Дорога ярости')
bg = pygame.image.load('data/doroga2.png')
carvip = pygame.image.load('data/carvip.png')
zas = pygame.image.load('data/zas2.png')
bym = pygame.image.load('data/bym.png')
fon = pygame.image.load('data/fon.png')
igrat1 = pygame.image.load('data/igrat1.png')
igrat2 = pygame.image.load('data/igrat2.png')
menu1 = pygame.image.load('data/menu1.png')
menu2 = pygame.image.load('data/menu2.png')
zanovo1 = pygame.image.load('data/zanovo1.png')
zanovo2 = pygame.image.load('data/zanovo2.png')

prav1 = pygame.image.load('data/prav1.png')
prav2 = pygame.image.load('data/prav2.png')

myzvi1 = pygame.image.load('data/myzvi1.png')
myzvi2 = pygame.image.load('data/myzvi2.png')
myzvk1 = pygame.image.load('data/myzvk1.png')
myzvk2 = pygame.image.load('data/myzvk2.png')

zvykvi1 = pygame.image.load('data/zvykvi1.png')
zvykvi2 = pygame.image.load('data/zvykvi2.png')
zvykvk1 = pygame.image.load('data/zvykvk1.png')
zvykvk2 = pygame.image.load('data/zvykvk2.png')

pygame.mixer.music.load('data/fon360.wav')
pygame.mixer.music.set_volume(0.3)

button_sound = pygame.mixer.Sound('data/button.wav')
bymz = pygame.mixer.Sound('data/bymz.wav')

clock = pygame.time.Clock()
   

slimane()

carta1 = [(preg, (0, 0)), (preg, (14, 1)), (preg, (9, 2)), 
          (car, (25, 0)), (car, (28, 1)), (car, (22, 2)), 
          (preg, (29, 0)), (preg, (29, 2)), (car, (40, 1)), 
          (car, (41, 0))]
carta2 = [(preg, (0, 0)), (preg, (0, 2)), (car, (15, 0)),
          (car, (15, 2)), (preg, (17, 1)), (preg, (20, 0)), 
          (car, (28, 2)), (car, (31, 1)), (preg, (34, 0)), 
          (preg, (35, 1))]
carta3 = [(car, (5, 0)), (car, (5, 1)), (preg, (6, 2)),
          (car, (15, 0)), (car, (17, 1)), (car, (23, 2)), 
          (preg, (23, 1)), (preg, (30, 0)), (preg, (34, 2)), 
          (car, (41, 1))]
carti = [carta1, carta2, carta3]


igrat = Button(185, 55, igrat1, igrat2)
menu = Button(185, 55, menu1, menu2)
zanovo = Button(185, 55, zanovo1, zanovo2)
prav = Button(185, 55, prav1, prav2)

myz = ButtonMYZ(55, 55, myzvk1, myzvk2, myzvi1, myzvi2)

zvyk = ButtonZVYK(55, 55, zvykvk1, zvykvk2, zvykvi1, zvykvi2)
# zvyk.f = False

pygame.mixer.music.play(-1)

gmenu()  

pygame.quit()
exit()    