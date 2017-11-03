import arcade.key
import arcade.sound
from character import *
import character
 #what wrong
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
check_play_gameover_sound = True
I=0
T=5

class SpaceGameWindow(arcade.Window):
    check_firsttime=False
    Insert_key=False
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture("character/hell.jpg")

        self.baby_sprite = arcade.Sprite('character/babyfly1.png',0.15)

        self.block_sprite = arcade.Sprite('character/fixblock.png',1)
        self.block_cont_sprite = arcade.Sprite('character/fixblock.png',1)
        self.blood_sprite = arcade.Sprite('character/fixblood.png',1)
        self.blood_cont_sprite = arcade.Sprite('character/fixblood.png',1)

        self.hok_sprite = arcade.Sprite('character/hok.png',0.23)
        self.hok2_sprite = arcade.Sprite('character/hok.png',0.23)
        self.hok3_sprite = arcade.Sprite('character/hok.png',0.23)
        self.hok4_sprite = arcade.Sprite('character/hok.png',0.23)
        self.hok5_sprite = arcade.Sprite('character/hok.png',0.23)
        self.hok6_sprite = arcade.Sprite('character/hok.png',0.23)
        self.hok7_sprite = arcade.Sprite('character/hok.png',0.23)

        self.hok_move_sprite = arcade.Sprite('character/hok_move.png',0.35)
        self.hok_move2_sprite = arcade.Sprite('character/hok_move.png',0.35)
        self.hok_move3_sprite = arcade.Sprite('character/hok_move.png',0.35)
        self.hok_move4_sprite = arcade.Sprite('character/hok_move.png',0.35)
        self.hok_move5_sprite = arcade.Sprite('character/hok_move.png',0.35)
        self.hok_move6_sprite = arcade.Sprite('character/hok_move.png',0.35)

        self.killblock_one_sprite = arcade.Sprite('character/killblock1.png',0.23)
        self.killblock_one2_sprite = arcade.Sprite('character/killblock1.png',0.23)
        self.killblock_one3_sprite = arcade.Sprite('character/killblock1.png',0.23)
        self.killblock_one4_sprite = arcade.Sprite('character/killblock1.png',0.23)
        self.killblock_one5_sprite = arcade.Sprite('character/killblock1.png',0.23)
        self.killblock_one6_sprite = arcade.Sprite('character/killblock1.png',0.23)

        self.killblock_two_sprite = arcade.Sprite('character/killblock2.png',0.23)
        self.killblock_two2_sprite = arcade.Sprite('character/killblock2.png',0.23)
        self.killblock_two3_sprite = arcade.Sprite('character/killblock2.png',0.23)
        self.killblock_two4_sprite = arcade.Sprite('character/killblock2.png',0.23)
        self.killblock_two5_sprite = arcade.Sprite('character/killblock2.png',0.23)
        self.killblock_two6_sprite = arcade.Sprite('character/killblock2.png',0.23)

        self.bomb_sprite = arcade.Sprite('character/bomb.png',0.23)
        self.bomb2_sprite = arcade.Sprite('character/bomb.png',0.23)
        self.bomb3_sprite = arcade.Sprite('character/bomb.png',0.23)

        self.ghost_sprite = arcade.Sprite('character/eye.png',0.1)
        self.ghost_two_sprite = arcade.Sprite('character/ghost.png',0.1)

        self.scoreboard_sprite = arcade.Sprite('character/scoreboard.png',0.5)
        self.sound_gameover = arcade.sound.load_sound('sound/gameover.wav')

        self.world = World(width, height)
 
    def on_draw(self):
        arcade.start_render()
        global check_play_gameover_sound
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)        
        self.baby_sprite.draw()

        self.block_sprite.draw()
        self.block_cont_sprite.draw()
        self.blood_sprite.draw()
        self.blood_cont_sprite.draw()

        self.hok_sprite.draw()
        self.hok2_sprite.draw()
        self.hok3_sprite.draw()
        self.hok4_sprite.draw()
        self.hok5_sprite.draw()
        self.hok6_sprite.draw()
        self.hok7_sprite.draw()

        self.hok_move_sprite.draw()
        self.hok_move2_sprite.draw()
        self.hok_move3_sprite.draw()
        self.hok_move4_sprite.draw()
        self.hok_move5_sprite.draw()
        self.hok_move6_sprite.draw()

        self.killblock_one_sprite.draw()
        self.killblock_one2_sprite.draw()
        self.killblock_one3_sprite.draw()
        self.killblock_one4_sprite.draw()
        self.killblock_one5_sprite.draw()
        self.killblock_one6_sprite.draw()

        self.killblock_two_sprite.draw()
        self.killblock_two2_sprite.draw()
        self.killblock_two3_sprite.draw()
        self.killblock_two4_sprite.draw()
        self.killblock_two5_sprite.draw()
        self.killblock_two6_sprite.draw()
            
        self.bomb_sprite.draw()
        self.bomb2_sprite.draw()
        self.bomb3_sprite.draw()

        self.ghost_sprite.draw()
        self.ghost_two_sprite.draw()

        self.scoreboard_sprite.draw()

        arcade.draw_text(str(self.world.score),150, 679,arcade.color.WHITE, 25)
        arcade.draw_text(self.world.txt,50, 680,arcade.color.WHITE, 25)

        if character.check_firsttime and not character.can_control:
            arcade.draw_text(str(self.world.score),595, 355,arcade.color.RED, 40)
        if not character.check_firsttime:
            arcade.draw_text("\"PRESS SPACEBAR TO JUMP\"",550,350,arcade.color.WHITE,30)
       
    def update(self, delta):
        if character.Insert_key and character.check_firsttime:
            self.baby_sprite = arcade.Sprite('character/babyfly2.png',0.15)
        elif not character.Insert_key and character.check_firsttime:
            self.baby_sprite = arcade.Sprite('character/babyfly1.png',0.15)

        self.world.update(60)

        self.baby_sprite.set_position(self.world.baby.x, self.world.baby.y)    # x,y in baby in world
 
        self.block_sprite.set_position(self.world.block.x, self.world.block.y)
        self.block_cont_sprite.set_position(self.world.block_cont.x, self.world.block_cont.y)
        self.blood_sprite.set_position(self.world.blood.x, self.world.blood.y) 
        self.blood_cont_sprite.set_position(self.world.blood_cont.x, self.world.blood_cont.y)

        self.hok_sprite.set_position(self.world.hok.x, self.world.hok.y)
        self.hok2_sprite.set_position(self.world.hok2.x, self.world.hok2.y)
        self.hok3_sprite.set_position(self.world.hok3.x, self.world.hok3.y)
        self.hok4_sprite.set_position(self.world.hok4.x, self.world.hok4.y)
        self.hok5_sprite.set_position(self.world.hok5.x, self.world.hok5.y)
        self.hok6_sprite.set_position(self.world.hok6.x, self.world.hok6.y)
        self.hok7_sprite.set_position(self.world.hok7.x, self.world.hok7.y)

        self.hok_move_sprite.set_position(self.world.hok_move.x, self.world.hok_move.y)
        self.hok_move2_sprite.set_position(self.world.hok_move2.x, self.world.hok_move2.y)
        self.hok_move3_sprite.set_position(self.world.hok_move3.x, self.world.hok_move3.y)
        self.hok_move4_sprite.set_position(self.world.hok_move4.x, self.world.hok_move4.y)
        self.hok_move5_sprite.set_position(self.world.hok_move5.x, self.world.hok_move5.y)
        self.hok_move6_sprite.set_position(self.world.hok_move6.x, self.world.hok_move6.y)
          
        self.killblock_one_sprite.set_position(self.world.killblock_one.x, self.world.killblock_one.y)
        self.killblock_one2_sprite.set_position(self.world.killblock_one2.x, self.world.killblock_one2.y)
        self.killblock_one3_sprite.set_position(self.world.killblock_one3.x, self.world.killblock_one3.y)
        self.killblock_one4_sprite.set_position(self.world.killblock_one4.x, self.world.killblock_one4.y)
        self.killblock_one5_sprite.set_position(self.world.killblock_one5.x, self.world.killblock_one5.y)
        self.killblock_one6_sprite.set_position(self.world.killblock_one6.x, self.world.killblock_one6.y)

        self.killblock_two_sprite.set_position(self.world.killblock_two.x, self.world.killblock_two.y)
        self.killblock_two2_sprite.set_position(self.world.killblock_two2.x, self.world.killblock_two2.y)
        self.killblock_two3_sprite.set_position(self.world.killblock_two3.x, self.world.killblock_two3.y)
        self.killblock_two4_sprite.set_position(self.world.killblock_two4.x, self.world.killblock_two4.y)
        self.killblock_two5_sprite.set_position(self.world.killblock_two5.x, self.world.killblock_two5.y)
        self.killblock_two6_sprite.set_position(self.world.killblock_two6.x, self.world.killblock_two6.y)
                
        self.bomb_sprite.set_position(self.world.bomb.x, self.world.bomb.y)
        self.bomb2_sprite.set_position(self.world.bomb2.x, self.world.bomb2.y)
        self.bomb3_sprite.set_position(self.world.bomb3.x, self.world.bomb3.y)

        self.ghost_sprite.set_position(self.world.ghost.x, self.world.ghost.y)
        self.ghost_two_sprite.set_position(self.world.ghost_two.x, self.world.ghost_two.y)
        
        self.scoreboard_sprite.set_position(self.world.scoreboard.x, self.world.scoreboard.y)
      
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
  