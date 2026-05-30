# Game is in development.
# If you have problems, please send the problem into this email: tinhoctre847@gmail.com.
# Always update.
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from datetime import datetime
from typing import Any
main = Ursina()
player = FirstPersonController(model="cube", y=2, color=color.clear)
Sky()
list_log = [
    f"[{datetime.now()}][INFO] Game initialized.\n", 
    f"[{datetime.now()}][INFO] Ursina Engine initialized.\n", 
    f"[{datetime.now()}][INFO] Game Server initialized.\n",
    f"[{datetime.now()}][INFO] Exception server initialized.\n", 
    f"[{datetime.now()}][INFO] Third and First person initialized.\n", 
    f"[{datetime.now()}][INFO] Webhook server initialized.\n"
    f"[{datetime.now()}][from ursina]info: Using primary monitor: Monitor(x=0, y=0, width=1920, height=1080, width_mm=293, height_mm=165, name='\\\\.\\DISPLAY1', is_primary=True.\n)",
    f"[{datetime.now()}][from ursina]:prc(warning): Invalid integer value for ConfigVariable win-size: 864.0.\n",
    f"[{datetime.now()}][from ursina]:prc(warning): Invalid integer value for ConfigVariable win-size: 1536.0.\n",
    f"[{datetime.now()}][from ursina]Known pipe types: wglGraphicsPipe (3 aux display modules not yet loaded.\n)",
    f"[{datetime.now()}][from ursina]set window position: Vec2(192, 108)"
    f"[{datetime.now()}][from ursina]:prc(warning): changing default value for ConfigVariable paste-emit-keystrokes from '1' to '0'.\n",
    f"[{datetime.now()}][from ursina]:pnmimage:png(warning): iCCP: known incorrect sRGB profile"
    f"[{datetime.now()}][from ursina]package_folder: C://Users//Python Developer//AppData//Local//Programs//Python//Python311//Lib//site-packages//ursina.\n",
    f"[{datetime.now()}][from ursina]asset_folder: d:\Minecraft.\n",
    f"[{datetime.now()}][from ursina]os: Windows.\n",
    f"[{datetime.now()}][from ursina]development mode: True.\n",
    f"[{datetime.now()}][from ursina]application successfully started.\n",
    f"[{datetime.now()}][from ursina]info: changed aspect ratio: 1.778 -> 1.778.\n",
]
file=open("log.txt", "w")

hovered = None
a = -0.5
player_visual = Entity(
    parent=player,           # Attach to your FirstPersonController
    model='Assets/Player/Player.gltf',     # Load the geometry from your file 
    color=color.white,       # This makes it a solid white/gray color
    scale=0.5,
    origin_y=-0.5,
    enabled=True,
    rotation_y=-90,
    y=1.0,
    
)
mining_time = int(0)
break_speed = 0.5
grid_floor = Entity(
    model='plane',
    scale=100,       # 1000x1000 size!
    texture='Assets_Blocks/grass.png',
    texture_scale=(1000, 1000), # Makes the grass texture repeat so it doesn't look blurry
    collider='box',
    color=color.clear,
    position=(0, a, 0)
)

grid_floor_2 = Entity(
    model='plane',
    scale=100,
    texture="Assets_Blocks/netherite.png",
    texture_scale=(1000, 1000),
    collider='box',
    color=color.clear,
    position=(2000, -0.5, 0)
)
portal1 = Entity(model='cube', color=color.white, scale=(2, 3, 1), 
                 position=(5, 1, 5), collider='box')
Text(parent=portal1, origin=(0, -0.5))

# Portal in World 2 (leads back to World 1)
portal2 = Entity(model='cube', color=color.white, scale=(2, 3, 1), 
                 position=(2005, 1, 5), collider='box')
Text(parent=portal2, origin=(0, -0.5))
boxes = []

def world_1():
    for z in range(30):
        for x in range(30):
            box = Button(color=color.white, model="cube", position=(x, 0, z)
                        , texture="grass.png", parent=scene, origin_y=1.5)
            boxes.append(box)
def world_2():
    for z in range(30):
        for x in range(30):
            # We add 2000 to the X position to match your portal teleport
            box = Button(
                color=color.white, 
                model="cube", 
                position=(x + 2000, 0, z),
                texture="netherite.png", 
                parent=scene, 
                origin_y=1.5,
                collider='box'
            )
            boxes.append(box)
def log(file, list_file, s=str()) -> str:
    if s not in list_log:
        list_log.append(s)


    for i in range(len(list_file)):
        print(list_file[i], file=file, end="")

def input(key):
    # Check if the mouse is touching ANYTHING with a collider
  if mouse.hovered_entity:
        
        # ADD BLOCK
    if key == "middle mouse down":  
        new_pos = mouse.world_point + mouse.normal * 0.5  
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
            
            # Use 'Button' because it has an automatic collider
        new = Button(
                parent=scene,
                model='cube',
                texture='Assets_Blocks/grass.png',
                color=color.white,
                highlight_color=color.light_gray,
                position=grid_pos,
                origin_y=0.5,
                collider='box' # Explicitly ensure it has a collider
            )
        boxes.append(new)
    if key == "1":
        new_pos = mouse.world_point + mouse.normal * 0.5 
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
        
        # 1. The Main Dirt Block
        new = Button(
            parent=scene,
            model='cube',
            color=color.white,
            texture='Assets_Blocks/diamond.png',
            highlight_color=color.light_gray,
            position=grid_pos,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(new)
    elif key == "2":
        new_pos = mouse.world_point + mouse.normal * 0.5 
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
        
        # 1. The Main Dirt Block
        new = Button(
            parent=scene,
            model='cube',
            color=color.white,
            texture='Assets_Blocks/copper.png',
            highlight_color=color.light_gray,
            position=grid_pos,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(new)
    elif key == "3":
        new_pos = mouse.world_point + mouse.normal * 0.5 
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
        
        # 1. The Main Dirt Block
        new = Button(
            parent=scene,
            model='cube',
            color=color.white,
            texture='Assets_Blocks/coal.png',
            highlight_color=color.light_gray,
            position=grid_pos,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(new)
    elif key == "4":
        new_pos = mouse.world_point + mouse.normal * 0.5 
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
        
        # 1. The Main Dirt Block
        new = Button(
            parent=scene,
            model='cube',
            color=color.white,
            texture='Assets_Blocks/gold.png',
            highlight_color=color.light_gray,
            position=grid_pos,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(new)
    elif key == "5":
        new_pos = mouse.world_point + mouse.normal * 0.5 
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
        
        # 1. The Main Dirt Block
        new = Button(
            parent=scene,
            model='cube',
            color=color.white,
            texture='Assets_Blocks/netherite.png',
            highlight_color=color.light_gray,
            position=grid_pos,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(new)
    elif key == "6":
        new_pos = mouse.world_point + mouse.normal * 0.5 
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
        
        # 1. The Main Dirt Block
        new = Button(
            parent=scene,
            model='cube',
            color=color.white,
            texture='Assets_Blocks/emerald.png',
            highlight_color=color.light_gray,
            position=grid_pos,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(new)
    elif key == "7":
        new_pos = mouse.world_point + mouse.normal * 0.5 
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
        
        # 1. The Main Dirt Block
        new = Button(
            parent=scene,
            model='cube',
            color=color.white,
            texture='Assets_Blocks/stone1.png',
            highlight_color=color.light_gray,
            position=grid_pos,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(new)
    elif key == "8":
        new_pos = mouse.world_point + mouse.normal * 0.5 
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
        
        # 1. The Main Dirt Block
        new = Button(
            parent=scene,
            model='cube',
            color=color.white,
            texture='Assets_Blocks/stone2.png',
            highlight_color=color.light_gray,
            position=grid_pos,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(new)
    elif key == "9":
        new_pos = mouse.world_point + mouse.normal * 0.5 
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
        
        # 1. The Main Dirt Block
        new = Button(
            parent=scene,
            model='cube',
            color=color.white,
            texture='Assets_Blocks/stone3.png',
            highlight_color=color.light_gray,
            position=grid_pos,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(new)
    elif key == "0":
        new_pos = mouse.world_point + mouse.normal * 0.5 
        grid_pos = (round(new_pos.x), round(new_pos.y), round(new_pos.z))
        
        # 1. The Main Dirt Block
        new = Button(
            parent=scene,
            model='cube',
            color=color.white, 
            texture='Assets_Blocks/stone4.png',
            highlight_color=color.light_gray,
            position=grid_pos,
            origin_y=0.5,
            collider='box',
        )
        boxes.append(new)
    elif key == "m":
        if camera.z == 0:
            # Switch to Third Person
            camera.z = -10
            camera.y = 2
            player.cursor.enabled = True
            player.cursor.enable()
            print(f"[{datetime.now()}][INFO] Switched to Third Person", file=file, end=".\n")
        else:
            # Switch to First Person
            camera.z = 0
            camera.y = 0
            player.cursor.enabled = True
            print(f"[{datetime.now()}][INFO] Switched to First Person", file=file, end=".\n")

    elif key == "right mouse down":
        if mouse.hovered_entity in boxes:
            target = mouse.hovered_entity
            boxes.remove(target) # Remove from list FIRST
            destroy(target)
    else:
        pass
def reset():
    player.position = (0, 0, 0) 

def update():
    # 1. Check Portal 1 -> World 2
    if distance(player, portal1) < 2:
        player.position = (2000, 2, 0) # Teleport to center of World 2

    # 2. Check Portal 2 -> World 1
    if distance(player, portal2) < 2:
        player.position = (0, 2, 0) # Teleport back to World 1
    # 3. Fall detection (Reset based on which world you are in)
    if player.y < -10:
        if player.x > 1000:
            player.position = (2000, 5, 0)
        else:
            player.position = (0, 5, 0)
    global mining_time
    # 1. Check if Left Mouse is held down
    if mouse.left:
        
        if mouse.hovered_entity in boxes:
            
            mining_time += time.dt # Add the time passed since last frame          
            # 3. If held long enough, destroy it
            if mining_time >= break_speed:
                target = mouse.hovered_entity
                boxes.remove(target)
                destroy(target)
                mining_time = 0 # Reset timer
    else:
        mining_time = int(0)
   
# Runtime
log(file, list_log)
world_1()
world_2()
main.run()
