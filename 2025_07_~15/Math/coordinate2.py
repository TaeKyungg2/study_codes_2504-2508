import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))         # 그림 크기 설정 (옵션)
plt.xlim(-10, 10)                    # x축 범위: 0~10
plt.ylim(-10, 10)                    # y축 범위: 0~10
plt.gca().set_aspect('equal')     # x, y 비율 1:1
plt.grid(True)                    # 격자선 보이기
plt.xticks(range(-10,11,1))             # x축 눈금 0~10
plt.yticks(range(-10,11,1))             # y축 눈금 0~10
plt.axhline(0, color='black', linewidth=1)  # x축 기준선
plt.axvline(0, color='black', linewidth=1)  # y축 기준선
ax = plt.gca()
ax.spines['left'].set_position('zero')   # y축을 x=0에
ax.spines['bottom'].set_position('zero') # x축을 y=0에

plt.text(10.2, 0.2, 'x', fontsize=12, color='black')  # x축 오른쪽
plt.text(0.2, 10.2, 'y', fontsize=12, color='black')  # y축 위쪽
plt.savefig("2Dcoordinate.png", transparent=True)
plt.show()