from deepface import DeepFace
from deepface.commons import functions, realtime, distance as dst
# import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import os
import cv2
import numpy as np


# 模型名
models_name = ["VGG-Face", "Facenet", "Facenet512", "OpenFace",
               "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace", 'Ensemble']

model_name = models_name[6]
left = 0
top = 0
right = 960
bottom = 960

def detectFace(img):
    result = DeepFace.extract_faces(img, enforce_detection=False,detector_backend='retinaface')
    print(result[0]['facial_area'])
    return  result[0]['confidence']
    #     print("人脸检测成功！")
    # else:
    #     print("未检测到人脸。")
def getFaceEmbedding(img):
    faceEmbedding = DeepFace.represent(img,enforce_detection=False,model_name=model_name,detector_backend='retinaface')
    faceEmbedding = faceEmbedding[0]["embedding"]
    return faceEmbedding

threshold = 0.60#0.68

def getdistance(img1_representation,img2_representation):
    distance = dst.findCosineDistance(img1_representation, img2_representation)
    print(distance)
    return distance < 0.65
# model = DeepFace.build_model(model_name)
# print(model.summary())
if __name__ == '__main__':
    img1_path=r"images\userfaces\111.jpg"
    img2_path=r"images\userfaces\1.jpg"
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
    # embedding_objs = DeepFace.represent(img_path =img1_path)
    # print((embedding_objs))
    # print(len(embedding_objs[0]['embedding']))
    result = DeepFace.verify(img1_path,
                            img2_path,distance_metric = metrics[0],model_name=model_name,\
                                enforce_detection=False,detector_backend='retinaface')
    # 展示结果，两个人不是同一个人
    # result = detectFace(img1_path)
    print(result)
