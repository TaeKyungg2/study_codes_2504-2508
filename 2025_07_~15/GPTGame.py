from ursina import *

# 간단한 미로 배열(1=벽, 0=길)
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,1,1],
    [1,0,1,0,1,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,1,0,1],
    [1,1,1,1,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

app = Ursina()

# 미로 생성
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 1:
            wall = Entity(model='cube', color=color.azure, collider='box',
                          position=(x,0,y), scale=(1,2,1))
        else:
            floor = Entity(model='cube', color=color.light_gray, collider=None,
                           position=(x,-1,y), scale=(1,0.1,1))

# 플레이어(공)
player = Entity(model='sphere', color=color.orange, scale=0.5,
                position=(1,0,1), collider='sphere')

camera.parent = player
camera.position = (0, 2, -5)
camera.rotation = (15, 0, 0)

speed = 4

def update():
    move = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['s'] - held_keys['w']
    ) * time.dt * speed
    player.position += move
    # 벽 충돌 감지
    hit_info = player.intersects()
    if hit_info.hit:
        player.position -= move

app.run()
