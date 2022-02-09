from hyperlpr import pipline as  pp
import cv2
# 自行修改文件名
image = cv2.imread("./imgs/pr/1.jpg")
image,res  = pp.SimpleRecognizePlate(image)
print(res)