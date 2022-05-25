from ursina import *
from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
emerald_block = load_texture('block\\emerald_block.png')
dirt_block = load_texture('block\\dirt.png')
pumpkin_block = load_texture('block\\carved_pumpkin.png')
coal_block = load_texture('block\\coal_ore.png')
cobblestone_block = load_texture('block\\cobblestone.png')
diamond_block = load_texture('block\\diamond_block.png')
obsidian_block = load_texture('block\\crying_obsidian.png')
sky_texture = load_texture('sky-blue-day-summer-white-texture.png')
leaves_block = load_texture('block\\azalea_leaves.png')
wood_block = load_texture('wood.jpg')
interact_sound = Audio('drop.mp3', loop= False, autoplay=False)
block_pick = 1

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'hand.obj',
            texture = 'block\\cactus_bottom.png',
            rotation = Vec3(150,-10,0),
            scale = 0.1,
            position = Vec2(0.6,-0.5)
        )
    def active(self):
       self.position = Vec2(0.5,-0.3)

    def passive(self):
        self.position = Vec2(0.6,-0.5)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 300,
            double_sided = True

        )
    

def update():
    global block_pick
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else: hand.passive()
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['7']: block_pick = 7
    if held_keys['8']: block_pick = 8
    if held_keys['9']: block_pick = 9
    


class Voxel(Button):
    def __init__(self,position = (0,0,0), texture= dirt_block):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.5,1)),
            highlight_color = color.yellow
            
        )
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                interact_sound.play()
                if block_pick==1:voxel= Voxel(position = self.position + mouse.normal, texture = dirt_block)
                if block_pick==2:voxel= Voxel(position = self.position + mouse.normal, texture = emerald_block)
                if block_pick==3:voxel= Voxel(position = self.position + mouse.normal, texture = diamond_block)
                if block_pick==4:voxel= Voxel(position = self.position + mouse.normal, texture = cobblestone_block)
                if block_pick==5:voxel= Voxel(position = self.position + mouse.normal, texture = obsidian_block)
                if block_pick==6:voxel= Voxel(position = self.position + mouse.normal, texture = coal_block)
                if block_pick==7:voxel= Voxel(position = self.position + mouse.normal, texture = pumpkin_block)
                if block_pick==8:voxel= Voxel(position = self.position + mouse.normal, texture = leaves_block)
                if block_pick==9:voxel= Voxel(position = self.position + mouse.normal, texture = wood_block)

            if key == 'right mouse down':
                interact_sound.play()
                destroy(self)


for z in range(20):
    for y in range(2):
        for x in range(20):
            voxel = Voxel(position = (x,y,z))

player = FirstPersonController(position = (10,y,10))

sky = Sky()

hand = Hand()

app.run()