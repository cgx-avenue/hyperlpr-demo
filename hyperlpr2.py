#导入包
from hyperlpr import *
#导入OpenCV库
import cv2
#读入图片
image = cv2.imread("./imgs/ori/3.jpg")
#打印识别结果
print(HyperLPR_plate_recognition(image))