import pygame

background_colour = (255,255,255)
(width, height) = (1000, 500)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)

pygame.display.flip()

points = [(894.0689090058631, 408.3687753792454), (909.8151682068354, 408.1277122971988), (908.6435723272109, 412.0533130109118), (909.0184806199247, 416.0570023964966), (905.5974179214032, 418.7360087120641), (904.660142923965, 423.87244939228674), (903.9571888087132, 426.5744850379532), (902.7855929290891, 428.4212231577408), (902.0357678123543, 435.03815180972896), (901.6608595196404, 438.8935937624062), (900.8173094625539, 443.265379987578), (894.631275710587, 443.32801231660744), (894.7250006509387, 430.39524332973326), (893.2722214189524, 430.0865199517088), (893.459679830963, 422.46317543387994), (894.5375507702354, 417.0302709246746), (893.8345881236769, 413.8710006549952), (893.5534047713146, 410.2393653052067), (894.0689090058631, 408.3687753792454)]

# Add some colors"""
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

def drawState(screen, color, points):
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

running = True
while running:
  drawState(screen,black,points)
  pygame.draw.lines(screen, black, False, [(0,0),(1000,500)], 3)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.flip()