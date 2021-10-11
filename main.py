import pygame,os,webbrowser
from pygame import mixer

pygame.init()
pygame.mixer.init()

class Window():
    def __init__(self):
        self.x,self.y = 400,400
        self.window = pygame.display.set_mode((self.x,self.y))
        pygame.display.set_caption("Music Player")
        self.run = True
        self.input_rect = pygame.Rect(50, 200, 300, 32)
        self.musics_rect = pygame.Rect(50,10,300,180)
        self.base_font = pygame.font.SysFont("Arial", 24)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('indianred')
        self.filepath = __file__[0:len(__file__)-len(os.path.basename(__file__))]
        self.infile = os.listdir(self.filepath)
        self.color = self.color_passive
        self.directory,self.songs = [],[]
        self.buttonstat,self.stat,self.pause,self.nowsong,self.user_text = "idle","Boşta...","","",""
        try:
            self.icon = pygame.image.load(self.filepath+"icon.png")
            pygame.display.set_icon(self.icon)
        except:
            pass
    def MusicPlayer(self,name):
        try:
            pygame.mixer.music.load(self.filepath+name)
            self.songs.pop(0)
            pygame.mixer.music.play()
            self.nowsong = name
        except:
            self.user_text = "Hata : Dosya Bulunamadı!"
            self.songs.pop(0)
    def Draw(self):
        mouse = pygame.mouse.get_pos()
        filepath,num,text = 0,0,[]
        lenghtfilepath = len(self.infile)-1
        if not len(self.directory) == lenghtfilepath:
            for i in self.infile:
                if filepath == 6:
                    break
                if i.endswith("py"):
                    continue
                self.directory.append(i) 
        text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        play_button = self.base_font.render("Play",True,(255,255,255))
        if pygame.mixer.music.get_busy() == True:
            self.stat = f"Çalıyor. Şarkı : {self.nowsong}"
        else:
            self.nowsong = ""
            if lenghtfilepath > 6:
                self.stat = "Hata : Fazla Şarkı! Boşta."
        if self.buttonstat == "idle":
            self.pause = "Pause"
        else:
            self.pause = "Unpause"
        stop_button = self.base_font.render(f"{self.pause}",True,(255,255,255))
        skip_button = self.base_font.render("Skip",True,(255,255,255))
        github_button = self.base_font.render("Github",True,(255,255,255))
        stat_button = self.base_font.render(f"Durum : {self.stat}",True,(0,0,0))
        if (self.x/2)-120 <= mouse[0] <= (self.x/2)-20 and (self.y/2)+50 <= mouse[1] <= (self.y/2)+80:
            pygame.draw.rect(self.window,(135, 206, 250),[self.x/2-120,self.y/2+50,100,35])
        else:
            pygame.draw.rect(self.window,(205, 92, 92),[self.x/2-120,self.y/2+50,100,35])
        if (self.x/2)+20 <= mouse[0] <= (self.x/2)+120 and (self.y/2)+50 <= mouse[1] <= (self.y/2)+80:
            pygame.draw.rect(self.window,(135, 206, 250),[self.x/2+20,self.y/2+50,100,35])
        else:
            pygame.draw.rect(self.window,(205, 92, 92),[self.x/2+20,self.y/2+50,100,35])
        if (self.x/2)-120 <= mouse[0] <= (self.x/2)-20 and (self.y/2)+100 <= mouse[1] <= (self.y/2)+130:
            pygame.draw.rect(self.window,(135, 206, 250),[self.x/2+-120,self.y/2+100,100,35])
        else:
            pygame.draw.rect(self.window,(205, 92, 92),[self.x/2+-120,self.y/2+100,100,35])
        if (self.x/2)+20 <= mouse[0] <= (self.x/2)+120 and (self.y/2)+100 <= mouse[1] <= (self.y/2)+130:
            pygame.draw.rect(self.window,(135, 206, 250),[self.x/2+20,self.y/2+100,100,35])
        else:
            pygame.draw.rect(self.window,(205, 92, 92),[self.x/2+20,self.y/2+100,100,35])
        pygame.draw.rect(self.window, self.color, self.input_rect)
        pygame.draw.rect(self.window, (205, 92, 92), self.musics_rect)
        self.window.blit(text_surface, (self.input_rect.x+3, self.input_rect.y))
        self.window.blit(play_button,((self.x/2)-90,self.y/2+51))
        self.window.blit(stop_button,((self.x/2)+35,self.y/2+52))
        self.window.blit(skip_button,((self.x/2)-90,self.y/2+103))
        self.window.blit(github_button,((self.x/2)+40,self.y/2+103))
        self.window.blit(stat_button,((self.x/2)-190,self.y/2+165))
        for i in range(0,6):
            if len(self.directory) == i:
                break
            text.append(self.base_font.render(self.directory[i],True,(255,255,255)))
        for y in range(0,len(text)):
            num += -30
            self.window.blit(text[y], (self.musics_rect.x+3, -10-num-10))
        self.input_rect.w = 300
            
windowManager = Window()

def Music():
    while windowManager.run:
        windowManager.window.fill((255, 255, 224))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                windowManager.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if windowManager.input_rect.collidepoint(event.pos):
                    windowManager.active = True
                else:
                    windowManager.active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    windowManager.user_text = windowManager.user_text[:-1]
                elif event.key == pygame.K_TAB:
                    windowManager.user_text = ""
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if len(windowManager.user_text) <= 4:
                        windowManager.user_text = "Hata : Geçersiz Şarkı!"
                    else:
                        if len(windowManager.nowsong) == 0:
                            windowManager.nowsong = windowManager.user_text
                        windowManager.songs.append(windowManager.user_text)
                        windowManager.MusicPlayer(windowManager.user_text)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    windowManager.user_text = windowManager.user_text[:-1]
                else:
                    windowManager.user_text += event.unicode
                    windowManager.color = windowManager.color_active
            if event.type == pygame.KEYUP:
                windowManager.color = windowManager.color_passive
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if (windowManager.x/2)-120 <= mouse[0] <= (windowManager.x/2)-20 and (windowManager.y/2)+50 <= mouse[1] <= (windowManager.y/2)+80:
                    windowManager.songs.append(windowManager.user_text)
                    windowManager.MusicPlayer(windowManager.user_text)
                elif (windowManager.x/2)+20 <= mouse[0] <= (windowManager.x/2)+120 and (windowManager.y/2)+50 <= mouse[1] <= (windowManager.y/2)+80:
                    if windowManager.buttonstat == "idle":
                        windowManager.buttonstat = "paused"
                        pygame.mixer.music.pause()
                    else:
                        windowManager.buttonstat = "idle"
                        pygame.mixer.music.unpause()
                elif (windowManager.x/2)-120 <= mouse[0] <= (windowManager.x/2)-20 and (windowManager.y/2)+100 <= mouse[1] <= (windowManager.y/2)+130:
                    pygame.mixer.music.stop()
                elif (windowManager.x/2)+20 <= mouse[0] <= (windowManager.x/2)+120 and (windowManager.y/2)+100 <= mouse[1] <= (windowManager.y/2)+130:
                    webbrowser.open_new("https://github.com/ichuusy")
                
            if pygame.mixer.music.get_busy() == False:
                if len(windowManager.songs) >= 1:
                    windowManager.MusicPlayer(windowManager.user_text)
        windowManager.Draw()
        # print(f"Mouse X : {mouse[0]} | Mouse Y : {mouse[1]}")
        pygame.display.flip()
        
Music()
