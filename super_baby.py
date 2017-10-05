import arcade
import arcade.key 
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCALE = 0.23
 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):   # justify shape of obj
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)

        self.baby = arcade.Sprite('character/babyfly1.png',SCALE)
        self.baby.set_position(250,360)  # baby w = 150 ,h=?

        self.block =arcade.Sprite('character/block1.png',SCALE)
        self.block.set_position(92,660) # block w=92 , h =60
 

    def on_draw(self):
        arcade.start_render()
        self.baby.draw()
        self.block.draw()

    def on_key_press(self, key, key_modifiers):
        self.baby.on_key_press(key, key_modifiers)
        self.baby.set_position(250,self.baby.y+30)
            
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()