import mss
import mss.tools
import pyautogui
import time
import random
import keyboard

print("연속 캡처할 횟수를 입력하세요:")
repeat_count = int(input())

# print("1. 마우스로 [왼쪽 위] 위치에 커서를 두고 Enter를 누르세요.")
# input()
# left_top = pyautogui.position()
# print(f"왼쪽 위 좌표: {left_top}")

# print("2. 마우스로 [오른쪽 아래] 위치에 커서를 두고 Enter를 누르세요.")
# input()
# right_bottom = pyautogui.position()
# print(f"오른쪽 아래 좌표: {right_bottom}")
left_top =pyautogui.Point(x=2077, y=-487)
right_bottom=pyautogui.Point(x=2787, y=481)
x1, y1 = left_top
x2, y2 = right_bottom

# 좌표 정렬
left = min(x1, x2)
top = min(y1, y2)
width = abs(x2 - x1)
height = abs(y2 - y1)
region = {'left': left, 'top': top, 'width': width, 'height': height}

print(f"\n설정된 영역: {region}")
print("이제 [s] 키를 누르면 캡처가 시작됩니다!")
keyboard.wait('s')
print("캡처를 시작합니다.\n")

with mss.mss() as sct:
    for i in range(1, repeat_count + 1):
        # x_offset = random.randint(-10, 10)
        # y_offset = random.randint(-10, 10)
        # pyautogui.moveTo(pyautogui.position().x + x_offset, pyautogui.position().y + y_offset)
        print(f"{i}번째 캡처 완료!")
        time.sleep(1)
        # 키보드 오른쪽 방향키 누르기(가상 입력)
        keyboard.press_and_release('right')
        # if random.randint(1,10)<3:
        #     pyautogui.click(button='right')#차단피하기
        # if random.randint(1,20)<2:
        #     time.sleep(random.randint(5,14))
        # 바로 영역 캡처
        img = sct.grab(region)
        filename = f"page_{i}.png"
        mss.tools.to_png(img.rgb, img.size, output=filename)
        print(f"{filename} 저장됨!")

print("모든 캡처가 완료되었습니다.")
