from deepface import DeepFace
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import os
import cv2
import numpy as np


# 模型名
models_name = ["VGG-Face", "Facenet", "Facenet512", "OpenFace",
               "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace", 'Ensemble']

model_name = models_name[1]
left = 0
top = 0
right = 960
bottom = 960
# model = DeepFace.build_model(model_name)
# print(model.summary())
img1_path="images/test/1-1.jpg"
img2_path="images/test/1-2.jpg"
# img_array = img_array.reshape((1, img_array.shape[0], img_array.shape[1], img_array.shape[2]))
# img1 = cv2.imread(img1_path)
# img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
# img1 = img1.resize(3,960,960)
# # # plt.imshow(img1)
# # # plt.show()
# # img1 = cv2.cvtColor(img1,cv2.COLOR_RGB2BGR)
# # # cv2.imwrite('1-1.jpg',img1)
# img2 = cv2.imread(img2_path)
# img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2BGR)
# img2= img2.resize(3,960,960)
# cv2.imwrite('1-2.jpg',img2)
# cropped_image = img1.crop((left, top, right, bottom))
# cropped_image.save(img1_path)
# img2 = Image.open(img2_path)
# img2.convert("BGR")
# img1.save(img1_path)
# img2.save(img2_path)
# print(cropped_image.size)
# print(img2.size)
metrics = ["cosine", "euclidean", "euclidean_l2"]
embedding_objs = DeepFace.represent(img_path =img1_path)
# print((embedding_objs))
print(len(embedding_objs[0]['embedding']))
result = DeepFace.verify(img1_path,
                         img2_path,distance_metric = metrics[0])
# 展示结果，两个人不是同一个人
print(result)
