# Game is in development.
# If you have problems, please send the problem into this email: tinhoctre847@gmail.com.
# Always update.
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import ctypes
from datetime import datetime
from typing import Any
from keyboard import is_pressed 
from json import dump, load
from socket import socket, AF_INET, SOCK_STREAM
port = 65535
cli = socket(AF_INET, SOCK_STREAM)
main = Ursina(title="Minecraft", icon="Assets/Logo/logo.png") 
window.fullscreen = True
player = FirstPersonController(color=color.white)
Sky()

# Functions for load and save game
def save_game():
    data = []
    for b in boxes:
        # Store the 3D position and the texture name
        # We use b.texture.name to remember if it's grass, diamond, etc.
        data.append({
            'position': (b.x, b.y, b.z),
            'texture': b.texture.name if b.texture else 'white_cube'
        })
    
    with open('savegame.json', 'w') as f:
        dump(data, f)
    print("World Saved!")
def load_game():
    # 1. Clear current world
    global boxes
    for b in boxes:
        destroy(b)
    boxes = []

    # 2. Open the file and recreate blocks
    try:
        with open('savegame.json', 'r') as f:
            data = load(f)
            for item in data:
                new_block = Button(
                    parent=scene,
                    model='cube',
                    position=item['position'],
                    texture=item['texture'],
                    color=color.white,
                    origin_y=0.5,
                    collider='box'
                )
                boxes.append(new_block)
        print("World Loaded!")
    except FileNotFoundError:
        print("No save file found.")
# Menu UI class 
class MinecraftMenu(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(1.5, 1.5),
            color=color.black66,
            enabled=True
        )

        # Helper to make button creation easier
        def create_mc_button(img, y_pos, click_func=None, func=None, func2=None):
            b = Button(
                parent=self,
                text='',
                model='quad', # <--- FORCE it to be a flat square to stop the warping
                texture=img,
                scale=tuple((0.2, 0.02)),    
                y=y_pos,
                color=color.white,
                highlight_color=color.light_gray,
                pressed_color=color.gray
            )
            if click_func:
                b.on_click = click_func
            return b

        self.start_btn = create_mc_button('play.ico', 0.1, self.start_game)
        self.load_btn = create_mc_button('options.ico', -0.05, load_game)
        self.quit_btn = create_mc_button('quit.ico', -0.2, application.quit, save_game)
    
    
    def start_game(self):
        self.enabled = bool(False)
        mouse.locked = True
        player.enabled = True
# Initialize it
main_menu = MinecraftMenu()
player.enabled = False # Keep player frozen until 'Singleplayer' is clicked
mouse.locked = False
class AdminPanel(Entity):
    def __init__(
            self,
            model:str,
            color:Any,
            position:tuple,
            scale:tuple,
            texture:str = None,
            texture_scale:tuple = (1, 1)
    )-> None:
        super().__init__(
            parent=camera.ui,
            model=model,
            position=position,
            color=color,
            scale=scale,
            texture=texture,
            texture_scale=texture_scale,
            enabled=False
        )
        
    def build_admin(self):
        self.text = Text(
            text="ADMIN PANEL",
            parent=self,
            y=0.45,
            x=-0.4,
            scale=2,
            color=color.hex("#f6ebd4")
        )
   
    def show(self):
        self.enabled=True
        mouse.locked=False
        player.enabled=False
    
    def hide(self):
        self.enabled=False
        mouse.locked=True
        player.enabled=True
admin_panel = AdminPanel("quad", color.hex("#2c221e"), (-0.5, 0), (0.4, 0.9))
admin_panel.build_admin()
player.enabled = False # Keep player frozen until 'Singleplayer' is clicked
mouse.locked = False
Texture.default_filtering = 'nearest'
# Main Game
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
    f"[{datetime.now()}][from ursina]Known pipe types: wglGraphicsPipe (3 aux display modules not yet loaded.).\n",
    f"[{datetime.now()}][from ursina]set window position: Vec2(192, 108)"
    f"[{datetime.now()}][from ursina]:prc(warning): changing default value for ConfigVariable paste-emit-keystrokes from '1' to '0'.\n",
    f"[{datetime.now()}][from ursina]:pnmimage:png(warning): iCCP: known incorrect sRGB profile"
    f"[{datetime.now()}][from ursina]package_folder: C://Users//Python Developer//AppData//Local//Programs//Python//Python311//Lib//site-packages//ursina.\n",
    f"[{datetime.now()}][from ursina]asset_folder: d:\Minecraft.\n",
    f"[{datetime.now()}][from ursina]os: Windows.\n",
    f"[{datetime.now()}][from ursina]development mode: True.\n",
    f"[{datetime.now()}][from ursina]application successfully started.\n",
    f"[{datetime.now()}][from ursina]info: changed aspect ratio: 1.778 -> 1.778.\n",
    "[END LOG]\n"
]
current = str()
file=open("log.txt", "w")
doc=open("documentaries.txt", "w")
hovered = None
a = -0.5
player_visual = Entity(
    parent=player,
    model='Assets/Player/Player.glb',
    scale=0.5,
    y=1.0,
    rotation_y=90,
    color=color.white
)
leg_l = player_visual.find("**/Cube.005") # Left Leg
leg_r = player_visual.find("**/Cube.002")
arm_r = player_visual.find("**/Cube.004")
head = player_visual.find("**/Cube.003")
for c in player_visual.children:
    if c.name == 'Cube.003':
        head = c
        break
if not head:
    head = player_visual.find('Cube.003')
head_x_rotation = 0
head_y_rotation = 0
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
def _(fin):
    print("""This is Minecraft using Python.
The game is in development. 
Always update.
If you have problems, please contact me at tinhoctre847@gmail.com""",
            file=fin)
def walk_cycle():
    # Only animate if they aren't already moving
    if not leg_l.is_animating():
        duration = 0.25
        # Swing legs and arms in opposite directions
        leg_l.animate_rotation((30, 0, 0), duration=duration, curve=curve.linear)
        leg_r.animate_rotation((-30, 0, 0), duration=duration, curve=curve.linear)
        # After the first half, swing them back
        invoke(leg_l.animate_rotation, (-30, 0, 0), duration=duration, delay=duration)
        invoke(leg_r.animate_rotation, (30, 0, 0), duration=duration, delay=duration)

def attack_swing():
    if not arm_r.is_animating():
        # Quick punch/mine animation
        arm_r.animate_rotation((60, 0, 0), duration=0.1)
        invoke(arm_r.animate_rotation, (0, 0, 0), duration=0.1, delay=0.1)	

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
            
            print(f"[{datetime.now()}][INFO] Switched to Third Person", file=file, end=".\n")
        else:
            # Switch to First Person
            camera.z = 0
            camera.y = 0
            player.cursor.enabled = True
            
            print(f"[{datetime.now()}][INFO] Switched to First Person", file=file, end=".\n")
    elif key == "f":
        if is_pressed("f"):
            mouse.locked=True
        elif is_pressed("f"):
            mouse.locked=False
        else:
            pass
    elif key == "right mouse down":
        if mouse.hovered_entity in boxes:
            target = mouse.hovered_entity
            boxes.remove(target) # Remove from list FIRST
            destroy(target)
    elif key == "escape":
        main_menu.enabled = not main_menu.enabled
        mouse.locked = not main_menu.enabled
    elif key == "]" or key == "~":
        if admin_panel.enabled:
            admin_panel.hide()
            print(1)
        else:
            admin_panel.show()
            print(2)
    else:
        pass
def reset():
    player.position = (0, 0, 0) 
def runanim(name):
    global current
    if current != name:
        current = name
        # If your model has internal GLTF animations, Ursina's Entity 
        # can sometimes play them if 'animations' were defined during export.
        if hasattr(player_visual, 'play_animation'):
            player_visual.play_animation(name)
        else:
            return False
def update():
    # 1. Portals & Fall Detection
    if distance(player, portal1) < 2:
        player.position = (2000, 2, 0)
    if distance(player, portal2) < 2:
        player.position = (0, 2, 0)
        
    if player.y < -10:
        player.position = (2000, 5, 0) if player.x > 1000 else (0, 5, 0)

    # 2. Mining Logic
    global mining_time
    if mouse.left and mouse.hovered_entity in boxes:
        mining_time += time.dt
        if mining_time >= break_speed:
            target = mouse.hovered_entity
            if target in boxes:
                boxes.remove(target)
                destroy(target)
            mining_time = 0
    else:
        mining_time = 0

    # 3. FIXED ANIMATION LOGIC
    # We call the strings directly. If your GLB animations don't trigger, 
    # you may need to use player_visual.animate_rotation for blocky movement.
    if held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']:
        runanim("Action1") 
    elif mouse.left:
        runanim('Action2')
    else:
        global current
        current = "" # Reset when standing still

    # 4. FIXED HEAD MOVING STRUCTURE
    global head_x_rotation, head_y_rotation
    if head:
        if mouse.locked:
            sensitivity = -50 
            head_y_rotation += mouse.velocity[0] * sensitivity
            head_x_rotation -= mouse.velocity[1] * sensitivity
        
        head_y_rotation = clamp(head_y_rotation, -60, 60)
        head_x_rotation = clamp(head_x_rotation, -30, 30)

        if mouse.velocity == Vec3(0,0,0):
            head_x_rotation = lerp(head_x_rotation, 0, time.dt * 3)
            head_y_rotation = lerp(head_y_rotation, 0, time.dt * 3)

        # setHpr(Heading/Yaw, Pitch, Roll)
        head.setHpr(head_y_rotation - 90, head_x_rotation, 0)
# Runtime
if __name__ =="__main__":
    win = ctypes.windll.shell32.IsUserAnAdmin()
    if win:
        _(doc)
        log(file, list_log)
        world_1()
        world_2()
        main.run()
