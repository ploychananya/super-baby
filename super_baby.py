import arcade
import arcade.key

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCALE = 0.23
I=0
T=0
Insert_key=False

 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):   # justify shape of obj
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)

        self.baby = arcade.Sprite('character/babyfly1.png',SCALE)
        self.baby.set_position(250,300)  # baby w = 150 ,h=?

        self.block =arcade.Sprite('character/fixblock.png',1)
        self.block.set_position(640,420) # block w=92 , h =60

        self.blood =arcade.Sprite('character/fixblood.png',1)
        self.blood.set_position(640,355) 


        self.hok =arcade.Sprite('character/hok.png',0.35)
        self.hok.set_position(555,150) 

        self.hok_move =arcade.Sprite('character/hok_move.png',0.3)
        self.hok_move.set_position(850,180)

        self.kill_block1 =arcade.Sprite('character/killblock1.png',SCALE)
        self.kill_block1.set_position(990,538) 

        self.kill_block2 =arcade.Sprite('character/killblock2.png',SCALE)
        self.kill_block2.set_position(300,538) 

        self.bomb =arcade.Sprite('character/bomb.png',SCALE)
        self.bomb.set_position(680,560) 
        
        self.eye =arcade.Sprite('character/eye.png',SCALE)
        self.eye.set_position(1200,450)

        self.ghost =arcade.Sprite('character/ghost.png',SCALE)
        self.ghost.set_position(1200,230)

   
    def update(self, delta):
    
        global I,Insert_key,T
    
        if(Insert_key):
            I=0
            self.baby.set_position(self.baby.center_x, self.baby.center_y+(T*T))
            T-=0.5
            if(T<1):
                Insert_key=False
            
         
        elif(not Insert_key):
            self.baby.set_position(self.baby.center_x, self.baby.center_y-(I*I))
            I+=0.07
            T=6
            print(I)

    def on_draw(self):
        arcade.start_render()
        #self.set_update_rate(20)
        self.baby.draw()
        self.block.draw()
        self.blood.draw()
        self.hok.draw()
        self.hok_move.draw()
        self.kill_block1.draw()
        self.kill_block2.draw()
        self.bomb.draw()
        self.eye.draw()
        self.ghost.draw()
   
    def on_key_press(self, key, key_modifiers):
        global Insert_key
        if key == arcade.key.UP:
            #self.on_key_press(key, key_modifiers)
            print("on key Up")
            Insert_key=True
            #global I
     
        
            
           # print("ployloveJJ")
           # self.baby.set_position(self.baby.center_x, self.baby.center_y+150)
            #I=0        
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()