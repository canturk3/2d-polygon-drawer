import pygame, sys
from pygame.locals import *
from sympy import false, true
import time

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLACK = ( 0,   0,   0)
GREEN = (0,255,0)

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410

FPS = 60

RECT_COUNT = 8

class MyApplication:
    def __init__(self) -> None:
        pass
    
    def check_collision(self,event,rectangles):
        for rectangle in rectangles:
            if(rectangle.collidepoint(event.pos)):
                return rectangle
        return None
    
    def draw_lines(self,screen, rectangles):
        count = 0
        prevrect = None
        firstrect = None
        for rectangle in rectangles:
            if count == 0:
                count += 1
                prevrect = rectangle
                firstrect = rectangle
                continue
            pygame.draw.line(screen, BLACK, (prevrect.x,prevrect.y), (rectangle.x,rectangle.y), 1)
            prevrect = rectangle
        pygame.draw.line(screen, BLACK, (firstrect.x,firstrect.y), (prevrect.x,prevrect.y), 1)
        return None
        

    def draw_rects(self,screen,rectangles,color):
        for rectangle in rectangles:
            pygame.draw.rect(screen, color, rectangle)
    
    def create_rects(self,count):
        rectangles = []
        for num in range(count):
            rectangles.append(pygame.rect.Rect(10, 20 * num, 17, 17))
        return rectangles

    def save_lines(self,screen, rectangles,saveButton):
        self.draw_rects(screen,rectangles,WHITE)
        pygame.draw.rect(screen, WHITE, saveButton)
        self.draw_lines(screen,rectangles)
        pygame.display.flip()

        pygame.image.save(screen,'temp.jpeg')

        #pygame.quit()


    def create_rect(self):
        mouse_position = pygame.mouse.get_pos()
        rectangle = pygame.rect.Rect(mouse_position, 17, 17)
        rectangle_draging = False
    
    def run(self):
        pygame.init()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tracking System")

        rectangles = self.create_rects(RECT_COUNT)

        #rectangle = pygame.rect.Rect(176, 134, 17, 17)
        
        
        rectangle_draging = False

        # - mainloop -

        clock = pygame.time.Clock()

        running = True
        rectangle = None

        saveButton = pygame.rect.Rect(SCREEN_WIDTH - 60, SCREEN_HEIGHT - 40, 50, 20)
        
        while running:

            # - events -

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        rectangle = self.check_collision(event,rectangles)          
                        if rectangle != None:
                            rectangle_draging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = rectangle.x - mouse_x
                            offset_y = rectangle.y - mouse_y
                        elif rectangle == None and saveButton.collidepoint(event.pos):
                            self.save_lines(screen,rectangles,saveButton)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:            
                        rectangle_draging = False
                        rectangle = None

                elif event.type == pygame.MOUSEMOTION:
                    if rectangle_draging:
                        mouse_x, mouse_y = event.pos
                        rectangle.x = mouse_x + offset_x
                        rectangle.y = mouse_y + offset_y

            # - updates (without draws) -

            # empty

            # - draws (without updates) -

            screen.fill(WHITE)

            self.draw_rects(screen,rectangles,RED)
            pygame.draw.rect(screen, GREEN, saveButton)


            self.draw_lines(screen,rectangles)
            #pygame.draw.rect(screen, RED, rectangle)

            pygame.display.flip()

            # - constant game speed / FPS -

            clock.tick(FPS)

    # - end -
    
    pygame.quit()