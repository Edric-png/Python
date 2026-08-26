import pygame,random
pygame.init();s=pygame.display.set_mode((800,600));p=pygame.Rect(375,275,50,50);e=[pygame.Rect(random.randrange(760),random.randrange(560),40,40) for _ in range(7)];score=0
while 1:
 for x in pygame.event.get():
  if x.type==pygame.QUIT:quit()
 k=pygame.key.get_pressed();p.x+=(k[pygame.K_RIGHT]-k[pygame.K_LEFT])*5;p.y+=(k[pygame.K_DOWN]-k[pygame.K_UP])*5
 for x in e[:]:
  if p.colliderect(x):score+=1;e.remove(x)
 s.fill("white");pygame.draw.rect(s,"blue",p)
 for x in e:pygame.draw.rect(s,"red",x)
 pygame.display.flip()
