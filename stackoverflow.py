import sys
import pygame as py

py.init()
White = (255,255,255)
Black = (0,0,0)
clock = py.time.Clock()
H = 400
W = 600
sc = py.display.set_mode((W,H))
sc.fill(White)
py.display.set_caption('Curve drawing')
py.display.update()
draw = False

fill_coords = []    # points to make filled polygon

while 1:
    for i in py.event.get():
        if i.type == py.QUIT:
            py.image.save(sc,r'C:/Users/Xiaomi' + '/temporary.png')
            py.quit()
            sys.exit()

        elif i.type == py.MOUSEBUTTONDOWN:
            if i.button == 1:
                draw = True
                fill_coords = []                              # restart the polygon
            elif i.button == 2:
                sc.fill(White)
                py.display.update()

        elif i.type == py.MOUSEBUTTONUP:
            if i.button == 1:
                draw = False
                py.draw.polygon( sc, Black, fill_coords ) # filled polygon

        elif i.type == py.MOUSEMOTION:                    # when the mouse moves
            if ( draw ):
                fill_coords.append( i.pos )                   # remember co-ordinate
    mouse_position = py.mouse.get_pos()
    if draw == True:
        py.draw.circle(sc,Black,i.pos,7)
        py.display.update()