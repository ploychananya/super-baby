import arcade.key
import time
from random import randint
Random_Number= randint(0,100)
check_play_fly_sound=False
check_play_hok_sound=True
check_play_brick_sound=True
check_play_ghost_sound=True
check_play_bomb_sound=True
check_play_margin_sound=True
check_play_gameover_sound =True
check_play_open_sound =True
count_hok_move = 0
count_hok_move2 = 0
count_hok_move3 = 0
count_hok_move4 = 0
count_hok_move5 = 0
count_hok_move6 = 0
count_ghost_move = 0
count_ghost2_move = 0
check_state_ghost=False
check_state_ghost2=False
fixed_thing_velocity = 2
mod_hok_killblock=120
mod_ghost=120
#Monster_velocity = 3
check_firsttime=False
check_inwindow=False
Insert_key=False
can_control=False
jump_down=0
jump_up=2
count_time=0
class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def hit(self, other, hit_size_x,hit_size_y):
        return (abs(self.x - other.x) <= hit_size_x) and (abs(self.y - other.y) <= hit_size_y)
    
    def touch_margin(self):
        global check_play_margin_sound,can_control
        if self.y>620 or self.y<90 :
            if can_control and check_play_margin_sound:
                if self.y>620:
                    arcade.sound.play_sound(self.world.sound_brick)
                    check_play_margin_sound=False
                elif self.y<90:
                    arcade.sound.play_sound(self.world.sound_blood)
                    check_play_margin_sound=False
            return True

    def fixed_thing_move(self,specify):
        global fixed_thing_velocity,check_firsttime
        if check_firsttime:
            if specify ==1:
                if self.world.block.x-640 <=0:
                    self.world.block2.x=self.world.block.x+640
                if self.world.block2.x-640 <=0:
                    self.world.block.x=self.world.block2.x+640
            elif specify ==2:
                if self.world.blood.x-640 <=0:
                    self.world.blood2.x=self.world.blood.x+640
                if self.world.blood2.x-640 <=0:
                    self.world.blood.x=self.world.blood2.x+640
    def Move(self,extra_velocity):
        global fixed_thing_velocity
        velocity= (fixed_thing_velocity*extra_velocity)
        if(self.x<-100):
            self.x=self.world.width+400
        if check_firsttime:
            self.x -= velocity
            #self.x -= fixed_thing_velocity
    def Monster_Movement(self,specify):
        global count_time,check_state_ghost,check_state_ghost2
        if specify==1:
            if not check_state_ghost and count_time%30==0:
                self.y+=70
                check_state_ghost=True
            elif check_state_ghost and count_time%30==0:
                self.y-=70
                check_state_ghost=False
        elif specify==2:
            if not check_state_ghost2 and count_time%30==0:
                self.y+=80
                check_state_ghost2=True
            elif check_state_ghost2 and count_time%30==0:
                self.y-=80
                check_state_ghost2=False
    def Hok_Movement(self,specify):
        global count_hok_move,count_hok_move2,count_hok_move3,count_hok_move4,count_hok_move5,count_hok_move6
        if specify ==1 :    
            if count_hok_move%2==0:
                self.y+=3
                if self.y >=140:
                    count_hok_move+=1
            elif count_hok_move%2==1:
                self.y-=1
                if(self.y<=-200):
                    count_hok_move+=1    
        elif specify ==2 :    
            if count_hok_move2%2==0:
                self.y+=2
                if self.y >=130:
                    count_hok_move2+=1
            elif count_hok_move2%2==1:
                self.y-=0.5
                if(self.y<=-200):
                    count_hok_move2+=1     
        elif specify ==3 :    
            if count_hok_move3%2==0:
                self.y+=2.5
                if self.y >=135:
                    count_hok_move3+=1
            elif count_hok_move3%2==1:
                self.y-=1
                if(self.y<=-200):
                    count_hok_move3+=1    
        elif specify ==4 :    
            if count_hok_move4%2==0:
                self.y+=1
                if self.y >=120:
                    count_hok_move4+=1
            elif count_hok_move4%2==1:
                self.y-=0.5
                if(self.y<=-200):
                    count_hok_move4+=1    
        elif specify ==5 :    
            if count_hok_move5%2==0:
                self.y+=2
                if self.y >=90:
                    count_hok_move5+=1
            elif count_hok_move5%2==1:
                self.y-=1
                if(self.y<=-200):
                    count_hok_move5+=1    
        elif specify ==6 :    
            if count_hok_move6%2==0:
                self.y+=3
                if self.y >=100:
                    count_hok_move6+=1
            elif count_hok_move6%2==1:
                self.y-=1
                if(self.y<=-200):
                    count_hok_move6+=1     
    def Check_performance(self):
        if (self.x > self.world.width+300 or self.x < -100):
            self.check_inwindow=False
            return False
        else:
            self.check_inwindow=True
            return True
    def obstacle_random_performance(self):
        #global count_time,check_firsttime
        #if(count_time%120==0 and check_firsttime):
        #if(not self.check_inwindow):
        #print("can perform")
        if not self.check_inwindow:
            self.x = self.world.width+300

class Baby(Model):
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world

        self.x = x
        self.y = y
 
    def update(self, delta):
        global jump_up,jump_down,Insert_key,check_firsttime,can_control,check_play_open_sound,Insert_key_time
        if(self.x<150):
            self.x+=3
            if(self.x>=150):
                can_control=True
            if check_play_open_sound:
                arcade.sound.play_sound(self.world.sound_open)
                check_play_open_sound=False
            
        print(Insert_key,check_firsttime)
        if(Insert_key and check_firsttime):#JUMP
            jump_down=0
            self.y+=(jump_up*jump_up)
            jump_up+=0.2
            if(jump_up>4):
                Insert_key=False

        elif(not Insert_key and check_firsttime):#DOWN
            jump_up=0.3
            self.y-=(jump_down*jump_down)
            jump_down+=0.1
         #firsttime_key เอา ไว้เช็คการกดครั้งแรกเพื่อให้เบบี้เริ่มขยับ
         
class Block(Model):  #fixed_thing
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world
        self.x = x
        self.y = y
        self.check_inwindow =False
 
    def update(self, delta):
        global fixed_thing_velocity,check_firsttime
        
        if check_firsttime:
            #self.x-=fixed_thing_velocity
            self.world.block.fixed_thing_move(1)
            self.world.block2.fixed_thing_move(1)
            self.world.block.Move(0.5)
            self.world.block2.Move(0.5)

class Blood(Model): #fixed_thing  ทำลูกคลื่นถ้ามีเวลาว่าง ขยับได้
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world
        
        self.x = x
        self.y = y
        self.check_inwindow =False
 
    def update(self, delta):
        global fixed_thing_velocity,check_firsttime
        
        if check_firsttime:
            #self.x-=fixed_thing_velocity
            self.world.blood.fixed_thing_move(2)
            self.world.blood2.fixed_thing_move(2)
            self.world.blood.Move(0.5)
            self.world.blood2.Move(0.5)

class Hok(Model):  
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world
        
        self.x = x
        self.y = y
        self.check_inwindow =False

    def update(self, delta):
        global can_control,check_firsttime,check_play_hok_sound,fixed_thing_velocity
        if self.world.hok.Check_performance():
            self.world.hok.Move(1/7)
        if self.world.hok2.Check_performance():
            self.world.hok2.Move(1/7)
        if self.world.hok3.Check_performance():
            self.world.hok3.Move(1/7)
        if self.world.hok4.Check_performance():
            self.world.hok4.Move(1/7)
        if self.world.hok5.Check_performance():
            self.world.hok5.Move(1/7)
        if self.world.hok6.Check_performance():
            self.world.hok6.Move(1/7)
        if self.world.hok7.Check_performance():
            self.world.hok7.Move(1/7)
        if self.world.baby.hit(self,120,100):
            print("hit hok!")
            if check_play_hok_sound and  can_control:
                arcade.sound.play_sound(self.world.sound_hok)
                check_play_hok_sound=False
            can_control=False

class Hok_Move(Model):  
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world
        
        self.x = x
        self.y = y
        self.check_inwindow =False

    def update(self, delta):
                    #0
        global can_control,check_play_hok_sound,fixed_thing_velocity
        if self.world.hok_move.Check_performance():
            self.world.hok_move.Move(1/6)
        if self.world.hok_move2.Check_performance():
            self.world.hok_move2.Move(1/6)
        if self.world.hok_move3.Check_performance():
            self.world.hok_move3.Move(1/6)
        if self.world.hok_move4.Check_performance():
            self.world.hok_move4.Move(1/6)
        if self.world.hok_move5.Check_performance():
            self.world.hok_move5.Move(1/6)
        if self.world.hok_move6.Check_performance():
            self.world.hok_move6.Move(1/6)
        

        if self.world.baby.hit(self,100,220):
            print("hit hok_move!")
            if check_play_hok_sound and can_control:
                arcade.sound.play_sound(self.world.sound_hok)
                check_play_hok_sound=False
            can_control=False
       
        if(check_firsttime):
            self.world.hok_move.Hok_Movement(1)
            self.world.hok_move2.Hok_Movement(2)
            self.world.hok_move3.Hok_Movement(3)
            self.world.hok_move4.Hok_Movement(4)
            self.world.hok_move5.Hok_Movement(5)
            self.world.hok_move6.Hok_Movement(6)
  
class Killblock_One(Model):  
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world
        
        self.x = x
        self.y = y
        self.check_inwindow =False
        
    def update(self, delta):
        global can_control,check_play_brick_sound,fixed_thing_velocity
        if self.world.killblock_one.Check_performance():
            self.world.killblock_one.Move(1/6)
        if self.world.killblock_one2.Check_performance():
            self.world.killblock_one2.Move(1/6)
        if self.world.killblock_one3.Check_performance():
            self.world.killblock_one3.Move(1/6)
        if self.world.killblock_one4.Check_performance():
            self.world.killblock_one4.Move(1/6)
        if self.world.killblock_one5.Check_performance():
            self.world.killblock_one5.Move(1/6)
        if self.world.killblock_one6.Check_performance():
            self.world.killblock_one6.Move(1/6)

        if self.world.baby.hit(self,100,70):
            print("hit kill 1!")
            if check_play_brick_sound and can_control:
                arcade.sound.play_sound(self.world.sound_brick)
                check_play_brick_sound=False
            can_control=False

class Killblock_Two(Model):  
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world
        
        self.x = x
        self.y = y
        self.check_inwindow =False
        
    def update(self, delta):
        global can_control,check_play_brick_sound,fixed_thing_velocity
        if self.world.killblock_two.Check_performance():
            self.world.killblock_two.Move(1/6)
        if self.world.killblock_two2.Check_performance():
            self.world.killblock_two2.Move(1/6)
        if self.world.killblock_two3.Check_performance():
            self.world.killblock_two3.Move(1/6)
        if self.world.killblock_two4.Check_performance():
            self.world.killblock_two4.Move(1/6)
        if self.world.killblock_two5.Check_performance():
            self.world.killblock_two5.Move(1/6)
        if self.world.killblock_two6.Check_performance():
            self.world.killblock_two6.Move(1/6)
        
        if self.world.baby.hit(self,100,70):
            print("hit kill 2!")
            if check_play_brick_sound and can_control:
                arcade.sound.play_sound(self.world.sound_brick)
                check_play_brick_sound=False
            can_control=False

class Bomb(Model):  
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world
        
        self.x = x
        self.y = y
        self.check_inwindow =False

    def update(self, delta):
        global can_control,check_play_bomb_sound,fixed_thing_velocity
        if self.world.bomb.Check_performance():
            self.world.bomb.Move(1/3)
        if self.world.bomb2.Check_performance():
            self.world.bomb2.Move(1/3)
        if self.world.bomb3.Check_performance():
            self.world.bomb3.Move(1/3)
        
        if self.world.baby.hit(self,100,50):
            print("hit BOMB!")
            if check_play_bomb_sound and can_control:
                arcade.sound.play_sound(self.world.sound_bomb)
                check_play_bomb_sound=False
            can_control=False

class Ghost(Model):  
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world
        
        self.x = x
        self.y = y
        self.check_inwindow =False
        
    def update(self, delta):
        global count_time,check_firsttime,can_control,check_play_ghost_sound,fixed_thing_velocity
        
        if(not self.check_inwindow):
            self.y=randint(50,self.world.height-130)
            
        if self.world.ghost.Check_performance():
            self.world.ghost.Move(2)
            self.world.ghost.Monster_Movement(1)

        if self.world.baby.hit(self,70,50):
            print("hit ghost 1!")
            if check_play_ghost_sound and can_control:
                arcade.sound.play_sound(self.world.sound_monster)
                check_play_ghost_sound=False
            can_control=False

class Ghost_Two(Model):  
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world
        
        self.x = x
        self.y = y
        self.check_inwindow =False

    def update(self, delta):
        global count_time,check_firsttime,can_control,check_play_ghost_sound,fixed_thing_velocity
        if( not self.check_inwindow):
            self.y=randint(50,self.world.height-130)
           
        if self.world.ghost_two.Check_performance():
            self.world.ghost_two.Move(2)  
            self.world.ghost_two.Monster_Movement(2)
        
        if self.world.baby.hit(self,70,50):
            print("hit ghost 2!")
            if check_play_ghost_sound and can_control:
                arcade.sound.play_sound(self.world.sound_monster)
                check_play_ghost_sound=False
            can_control=False

class Scoreboard(Model):  
    #def __init__(self, x, y):
    def __init__(self, world, x, y): #แก้ปัญหาการเรียกความกว้างความสูงของหน้าจอ โดยเรียกจากworldมาแทน
        self.world = world
        
        self.x = x
        self.y = y
    def update(self, delta):
        global can_control,check_firsttime
        if not can_control and check_firsttime:
            self.x=640
            self.y=355
 
class World:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

        #self.baby = Baby(250,300)  function นี้ เราเพิ่มworld เข้าไปเปนพารามิเตอร์อีกตัวแล้ว เลยต้องมาแก้
        self.baby = Baby(self,-20,355)

        self.block = Block(self,641,460)
        self.block2 = Block(self,1920,460)
        self.blood = Blood(self,641,355)
        self.blood2 = Blood(self,1920,355)

        self.hok = Hok(self,1700,100)
        self.hok2 = Hok(self,1700,100)
        self.hok3 = Hok(self,1700,100)   #PASS
        self.hok4 = Hok(self,1700,100)
        self.hok5 = Hok(self,1700,100)
        self.hok6 = Hok(self,1700,100)
        self.hok7 = Hok(self,1700,100)

        self.hok_move = Hok_Move(self,1700,-200)
        self.hok_move2 = Hok_Move(self,1700,-200)
        self.hok_move3 = Hok_Move(self,1700,-200)
        self.hok_move4 = Hok_Move(self,1700,-200)  #PASS
        self.hok_move5 = Hok_Move(self,1700,-200)
        self.hok_move6 = Hok_Move(self,1700,-200)

        self.killblock_one = Killblock_One(self,1600,579)
        self.killblock_one2 = Killblock_One(self,1600,579)
        self.killblock_one3 = Killblock_One(self,1600,579)
        self.killblock_one4 = Killblock_One(self,1600,579)
        self.killblock_one5 = Killblock_One(self,1600,579)
        self.killblock_one6 = Killblock_One(self,1600,579)

        self.killblock_two = Killblock_Two(self,1600,579)
        self.killblock_two2 = Killblock_Two(self,1600,579)
        self.killblock_two3 = Killblock_Two(self,1600,579)
        self.killblock_two4 = Killblock_Two(self,1600,579)
        self.killblock_two5 = Killblock_Two(self,1600,579)
        self.killblock_two6 = Killblock_Two(self,1600,579)

        self.bomb = Bomb(self,2000,602)
        self.bomb2 = Bomb(self,2000,602)
        self.bomb3 = Bomb(self,2000,602)

        self.ghost = Ghost(self,1600,355)
        self.ghost_two = Ghost_Two(self,1600,400)

        self.scoreboard = Scoreboard(self,355,1920)

        self.txt = "Score :"
        self.score = 0

        self.sound_blood = arcade.sound.load_sound('sound/blood.wav')
        self.sound_bomb = arcade.sound.load_sound('sound/bomb.wav')
        self.sound_jump = arcade.sound.load_sound('sound/jump.wav')
        self.sound_hok = arcade.sound.load_sound('sound/hok.wav')
        self.sound_monster = arcade.sound.load_sound('sound/monster.wav')
        self.sound_brick = arcade.sound.load_sound('sound/brick.wav')
        self.sound_bg = arcade.sound.load_sound('sound/bg.wav')
        self.sound_open = arcade.sound.load_sound('sound/open.wav')

    def update(self, delta):
        global can_control,count_time,check_firsttime,fixed_thing_velocity,mod_hok_killblock,mod_ghost,check_play_fly_sound,Insert_key
        if check_firsttime and can_control:
            count_time+=1 
            if (count_time==1 or count_time%2100==0): # เพลงแบลคกราวจบแล้วเล่นต่อ ประมาณ 36 วินาที
                if can_control:
                    arcade.sound.play_sound(self.sound_bg)
            print(count_time)
            if(count_time%30==0 and can_control):
                self.score+=1
                print("Score : ")
                print(self.score)
        if check_play_fly_sound:
            arcade.sound.play_sound(self.sound_jump)
            check_play_fly_sound=False
            
        self.baby.update(delta)

        self.block.update(delta)
        self.block2.update(delta)
        self.blood.update(delta)
        self.blood2.update(delta)

        self.hok.update(delta)
        self.hok2.update(delta)
        self.hok3.update(delta)
        self.hok4.update(delta)
        self.hok5.update(delta)
        self.hok6.update(delta)
        self.hok7.update(delta)

        self.hok_move.update(delta)
        self.hok_move2.update(delta)
        self.hok_move3.update(delta)
        self.hok_move4.update(delta)
        self.hok_move5.update(delta)
        self.hok_move6.update(delta)

        self.killblock_one.update(delta)
        self.killblock_one2.update(delta)
        self.killblock_one3.update(delta)
        self.killblock_one4.update(delta)
        self.killblock_one5.update(delta)
        self.killblock_one6.update(delta)

        self.killblock_two.update(delta)
        self.killblock_two2.update(delta)
        self.killblock_two3.update(delta)
        self.killblock_two4.update(delta)
        self.killblock_two5.update(delta)
        self.killblock_two6.update(delta)

        self.bomb.update(delta)
        self.bomb2.update(delta)
        self.bomb3.update(delta)

        self.ghost.update(delta)
        self.ghost_two.update(delta)

        self.scoreboard.update(delta)

        self.Random_Perform_Hok()
        self.Random_Perform_Hok_Move()
        self.Random_Perform_Killblock_bomb()
        self.Random_Perform_Ghost()

        if self.baby.touch_margin():
            print("touch margin!")
            can_control=False
        if(can_control):
            fixed_thing_velocity+= self.faster_interface()
            if(not mod_hok_killblock==0):
                mod_hok_killblock-=20*self.faster_interface()
            if(not mod_ghost==0):
                mod_ghost-=20*self.faster_interface()

    def faster_interface(self):
        global count_time
        if(count_time%600==0 and not self.score == 0):
            if(self.score>=60):
                return 0
            else:
                return 2
        else:
             return 0
    def on_key_press(self, key, key_modifiers):
        global check_firsttime,Insert_key,can_control,check_play_fly_sound
        if key == arcade.key.SPACE and can_control:
            print("JUMP!")
            check_firsttime=True
            Insert_key=True 
            check_play_fly_sound=True
    def Random_Perform_Hok(self):
        global count_time,check_firsttime,mod_hok_killblock# เวลาผ่านไป 2 วิ ค่อยสุ่มใหม่
        if (count_time%mod_hok_killblock==0 and check_firsttime):
            Random_Number = randint(0,7)  #0 = emty
            print("Can Random")
            if Random_Number == 1:
                self.hok.obstacle_random_performance()
            elif Random_Number == 2:
                self.hok2.obstacle_random_performance()
            elif Random_Number == 3:
                self.hok3.obstacle_random_performance()
            elif Random_Number == 4:
                self.hok4.obstacle_random_performance()
            elif Random_Number == 5:
                self.hok5.obstacle_random_performance()
            elif Random_Number == 6:
                self.hok6.obstacle_random_performance()
            elif Random_Number == 7:
                self.hok7.obstacle_random_performance()
            else:
                print("cannot perform HOK!")

    def Random_Perform_Hok_Move(self):
        global count_time,check_firsttime,mod_hok_killblock# เวลาผ่านไป 2 วิ ค่อยสุ่มใหม่
        if (count_time%mod_hok_killblock==0 and check_firsttime):
            Random_Number = randint(0,6)  #0 = emty
            print("Can Random")
            if Random_Number == 0:
                self.hok_move.obstacle_random_performance()
            elif Random_Number == 1:
                self.hok_move2.obstacle_random_performance()
            elif Random_Number == 2:
                self.hok_move3.obstacle_random_performance()
            elif Random_Number == 3:
                self.hok_move4.obstacle_random_performance()
            elif Random_Number == 4:
                self.hok_move5.obstacle_random_performance()
            elif Random_Number == 5:
                self.hok_move6.obstacle_random_performance()
            else:
                print("cannot perform HOK_MOVE!")
    
    def Random_Perform_Killblock_bomb(self):
        global can_control,count_time,check_firsttime,mod_hok_killblock# เวลาผ่านไป 2 วิ ค่อยสุ่มใหม่
        if (count_time%mod_hok_killblock==0 and check_firsttime):
            if(can_control):
                Random_Number = randint(0,16)  #0 = emty
                print("Can Random")
                if Random_Number == 1:
                    self.killblock_one.obstacle_random_performance()
                elif Random_Number == 2:
                    self.killblock_one2.obstacle_random_performance()
                elif Random_Number == 3:
                    self.killblock_one3.obstacle_random_performance()
                elif Random_Number == 4:
                    self.killblock_one4.obstacle_random_performance()
                elif Random_Number == 5:
                    self.killblock_one5.obstacle_random_performance()
                elif Random_Number == 6:
                    self.killblock_one6.obstacle_random_performance()

                elif Random_Number == 7:
                    self.killblock_two.obstacle_random_performance()
                elif Random_Number == 8:
                    self.killblock_two2.obstacle_random_performance()
                elif Random_Number == 9:
                    self.killblock_two3.obstacle_random_performance()
                elif Random_Number == 10:
                    self.killblock_two4.obstacle_random_performance()
                elif Random_Number == 11:
                    self.killblock_two5.obstacle_random_performance()
                elif Random_Number == 12:
                    self.killblock_two6.obstacle_random_performance()

                elif Random_Number == 13:
                    self.bomb.obstacle_random_performance()
                elif Random_Number == 14:
                    self.bomb2.obstacle_random_performance()
                elif Random_Number == 15:
                    self.bomb3.obstacle_random_performance()
                else:
                    print("cannot perform killblock or bomb!")
    def Random_Perform_Ghost(self):
        global can_control,count_time,check_firsttime,mod_ghost# เวลาผ่านไป 2 วิ ค่อยสุ่มใหม่
        if (count_time%mod_ghost==0 and check_firsttime):
             if(can_control):
                Random_Number = randint(0,4)  #0 = emty
                print("Can Random")
                if Random_Number == 1:
                    self.ghost.obstacle_random_performance()
                elif Random_Number == 2:
                    self.ghost_two.obstacle_random_performance()
                else:
                    print("cannot perform GHOST!")