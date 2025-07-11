from tensorflow.keras.models import load_model
import numpy as np
import cv2

# 1. 모델 불러오기
model = load_model('model.h5')

# 2. 이미지 불러와서 전처리
img = cv2.imread('test_image.jpg')
img = cv2.resize(img, (224, 224))  # (Teachable Machine에서 사용한 크기)
img = img.astype('float32') / 255.0
img = np.expand_dims(img, axis=0)

# 3. 예측
pred = model.predict(img)

# 4. 라벨 불러오기(선택)
with open('labels.txt', 'r', encoding='utf-8') as f:
    labels = [line.strip() for line in f]

print("예측 결과:", labels[np.argmax(pred)], "(", pred[0][np.argmax(pred)], ")")
