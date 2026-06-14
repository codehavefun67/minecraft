from ursina import *
from ursina.prefabs.animator import Animation, Animator
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from ursina.application import quit
noise=PerlinNoise()
main=Ursina(title="Minecraft")
player=FirstPersonController(
  mouse_sensitivity=Vec2(100, 100),
  position=(0, 5, 0)
)
visual = Entity(
   parent=player,
   model=load_model(name=" Player",path=Path("Assets/Player/Player.glb"), file_types=".glb"),
   scale=0.5,
   y=1.0,
   rotation_y = -90,
   color=color.white
)
selected_block: int = 2
block_type:str = "texture"
block_textures = [ 
  {"name": "ground", "texture": load_texture("Assets_Blocks/Assets/ground.png")}, 
  {"name": "groundcheckered", "texture": load_texture("Assets_Blocks/Assets/groundCheckered.png")}, 
  {"name": "groundearth", "texture": load_texture("Assets_Blocks/Assets/groundEarth.png")}, 
  {"name": "groundearthcheckered", "texture": load_texture("Assets_Blocks/Assets/groundEarthCheckered.png")}, 
  {"name": "groundmud", "texture": load_texture("Assets_Blocks/Assets/groundMud.png")}, 
  {"name": "groundsnow", "texture": load_texture("Assets_Blocks/Assets/groundSnow.png")},
  {"name": "ice01", "texture": load_texture("Assets_Blocks/Assets/ice01.png")},
  {"name": "lava01", "texture": load_texture("Assets_Blocks/Assets/lava01.png")},
  {"name": "stone01", "texture": load_texture("Assets_Blocks/Assets/Stone01.png")},
  {"name": "stone02", "texture": load_texture("Assets_Blocks/Assets/Stone02.png")},
  {"name": "stone03", "texture": load_texture("Assets_Blocks/Assets/Stone03.png")},
  {"name": "stone04", "texture": load_texture("Assets_Blocks/Assets/Stone04.png")},
  {"name": "stone05", "texture": load_texture("Assets_Blocks/Assets/Stone05.png")},
  {"name": "stone06", "texture": load_texture("Assets_Blocks/Assets/Stone06.png")},
  {"name": "stone07", "texture": load_texture("Assets_Blocks/Assets/Stone07.png")}, 
  {"name": "wallbrick01", "texture": load_texture("Assets_Blocks/Assets/wallBrick01.png")},
  {"name": "wallbrick02", "texture": load_texture("Assets_Blocks/Assets/wallBrick02.png")},
  {"name": "wallbrick03", "texture": load_texture("Assets_Blocks/Assets/wallBrick03.png")},
  {"name": "wallbrick04", "texture": load_texture("Assets_Blocks/Assets/wallBrick04.png")},
  {"name": "wallbrick05", "texture": load_texture("Assets_Blocks/Assets/wallBrick05.png")},
  {"name": "wallbrick06", "texture": load_texture("Assets_Blocks/Assets/wallBrick06.png")},
  {"name": "wallstone", "texture": load_texture("Assets_Blocks/Assets/wallStone.png")}, 
  {"name": "water", "texture": load_texture("Assets_Blocks/Assets/water.png")}
]
class Block(Entity):
  def __init__(self, position, sel_block):
    super().__init__(
      position=position,
      model="Assets_Blocks/Model/block_model",
      scale=1,
      origin_y=-0.5,
      texture=block_textures[sel_block]["texture"],
      collider="box"
      )
    self.block_type =sel_block
mini_block = Entity(
    parent=camera,
    model="Assets_Blocks/Model/block_model",
    scale=0.2,
    texture=block_textures[selected_block]["texture"], # Fixed here
    position=(0.35, -0.25, 0.5),
    rotation=(-15, -30, -5)
)

min_height = -5
for x in range(-10, 10):
    for z in range(-10, 10):
        height = noise([x * 0.02, z * 0.02])
        height = math.floor(height * 7.5)
        for y in range(height, min_height - 1, -1):
            if y == min_height:
                block = Block((x, y + min_height, z), 14) # stone07
            elif y == height:
                block = Block((x, y + min_height, z), 2)  # groundearth
            elif height - y > 2:
                block = Block((x, y + min_height, z), 21) # wallstone
            else:
                block = Block((x, y + min_height, z), 4)  # groundmud


def input(key):
        global selected_block
        #place block
        if key == "left mouse down":
            hit_info = raycast(camera.world_position, camera.forward, distance=10)
            if hit_info.hit:
                block = Block(hit_info.entity.position + hit_info.normal, selected_block) # Fixed here
        #delete block
        if key == "right mouse down" and mouse.hovered_entity:
            if not mouse.hovered_entity.block_type == 15:
                destroy(mouse.hovered_entity)
        #change block type
        if key == "1":
            selected_block = 0
        elif key == "2":
            selected_block = 1
        elif key == "3":
            selected_block = 2
        elif key == "4":
            selected_block = 3
        elif key == "5":
            selected_block = 4
        elif key == "6":
            selected_block = 5
        elif key == "7":
            selected_block = 6
        elif key == "8":
            selected_block = 7
        elif key == "9":
            selected_block = 8
        elif key == "0":
            selected_block = 9
        elif key == "q":
            selected_block = 10
        elif key == "e":
            selected_block = 11
        elif key == "r":
            selected_block = 12
        elif key == "t":
            selected_block = 13
        elif key == "y":
            selected_block = 14
        elif key == "u":
            selected_block = 15
        elif key == "i":
            selected_block = 16
        elif key == "o":
            selected_block = 17
        elif key == "p":
            selected_block = 18
        elif key == "f":
            selected_block = 19
        elif key == "g":
            selected_block = 20
        elif key == "h":
            selected_block = 21
        elif key == "j":
            selected_block = 22
        elif key == "m":
            if camera.z == 0:
                camera.z = -10
                camera.y = 2
            else:
                camera.z = 0
                camera.y = 0
        elif key == "escape":
            quit()
        
def update():
    mini_block.texture = block_textures[selected_block][block_type]
    if player.position.y <= -2000:
        player.position = (0, 5, 0)
if __name__ == "__main__":
    main.run()