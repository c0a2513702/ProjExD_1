import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)

    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)

    kk_rect = kk_img.get_rect()
    kk_rect.center = (300, 200)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 3200
        tmr += 1
        clock.tick(200)
        screen.blit(bg_img,[-x, 0])
        screen.blit(bg_img2,[-x+1600, 0])
        screen.blit(bg_img,[-x+3200, 0])

        

        key = pg.key.get_pressed()

        dx = -1
        dy = 0
        if key[pg.K_RIGHT]:
            dx = 1
        if key[pg.K_UP]:
            dy = -1
        if key[pg.K_DOWN]:
            dy = 1
        if key[pg.K_LEFT]:
            dx = -2

        kk_rect.move_ip(dx, dy)
        #if key[pg.K_UP]:
        #    kk_rect.move_ip(0, -1)
        #if key[pg.K_DOWN]:
        #    kk_rect.move_ip(0, 1)
        #if key[pg.K_LEFT]:
        #    kk_rect.move_ip(-1, 0)
        #if key[pg.K_RIGHT]:
        #    kk_rect.move_ip(1, 0)

        screen.blit(kk_img, kk_rect)
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()