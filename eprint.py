import pygame
pygame.init()


def printx(screen,text,pos,size=100,smothing=True,color='white'):
	font=pygame.font.SysFont(None,size)
	texte=font.render(text,smothing,color)
	screen.blit(texte,pos)
	
	