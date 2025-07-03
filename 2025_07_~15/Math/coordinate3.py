import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 3D 플롯 생성
fig = plt.figure(figsize=(8, 8))
fig.set_facecolor('white')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('white')

# 축 범위 설정 (양수만)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])
ax.patch.set_facecolor('white')

# 격자 설정
ax.grid(True)

# 눈금 설정
ticks = np.arange(0, 11, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_zticks(ticks)

# 축 라벨 설정
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 원점에서의 x, y, z 축 화살표 시각화 (얇은 축)
# ax.quiver(0, 0, 0, 10, 0, 0, color='r', arrow_length_ratio=0.1, linewidth=1)
# ax.quiver(0, 0, 0, 0, 10, 0, color='g', arrow_length_ratio=0.1, linewidth=1)
# ax.quiver(0, 0, 0, 0, 0, 10, color='b', arrow_length_ratio=0.1, linewidth=1)

# x=0, y=0, z=0 면에 해당하는 축 선(두껍게)
ax.plot([0, 10], [0, 0], [0, 0], color='black', linewidth=2)  # x축 선
ax.plot([0, 0], [0, 10], [0, 0], color='black', linewidth=2)  # y축 선
ax.plot([0, 0], [0, 0], [0, 10], color='black', linewidth=2)  # z축 선

# 뷰 각도 설정
ax.view_init(elev=20, azim=30)

plt.savefig("3Dcoordinate.png", transparent=True)
plt.show()
