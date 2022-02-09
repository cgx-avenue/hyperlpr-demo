from flask import Flask, request
from hyperlpr import *
import json
import cv2

app = Flask(__name__)

# 只接受post方法访问


@app.route("/",methods=["POST"])
def check():
    # 默认返回内容
    return_dict= {'code': '0', 'info': 'SUCCESS', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['code'] = '403'
        return_dict['info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    post_data=request.form.to_dict()
    img=post_data.get('img')
    # 对参数进行操作
    return_dict['result']=scanImage(img)
 
    return json.dumps(return_dict, ensure_ascii=False)
 
# 功能函数
def scanImage(img):
    image = cv2.imread(img)
    return HyperLPR_plate_recognition(image)
 
if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=False)