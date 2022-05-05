import cv2
import os

# 引入库

print("=============================================")
print("=  热键(请在摄像头的窗口使用)：             =")
print("=  z: 更改存储目录                          =")
print("=  x: 拍摄图片                              =")
print("=  q: 退出                                  =")
print("=============================================")
# 提醒用户操作字典

class_name = input("请输入存储目录（python安装目录下才行，如：d:pythonpy_image)：")
while os.path.exists(class_name):
    class_name = input("目录已存在！请输入存储目录：")
os.mkdir(class_name)
# 存储

index = 1
cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
width = 1920
height = 1440
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

print(width, height)
# 设置特定值

while True:
    ret, frame = cap.read()

    # 没理解？

    frame = cv2.flip(frame, 1, dst=None)
    # 镜像显示
    cv2.imshow("capture", frame)
    # 显示

    input = cv2.waitKey(1) & 0xFF
    if input == ord('z'):
        class_name = input("请输入存储目录：")
        while os.path.exists(class_name):
            class_name = input("目录已存在！请输入存储目录：")
        os.mkdir(class_name)
    # 存储

    elif input == ord('x'):
        num=0
        cv2.imwrite("%s/%d.jpeg" % (class_name, index),
                    cv2.resize(frame, (1920, 1080), interpolation=cv2.INTER_AREA))
        print("%s: %d 张图片" % (class_name, index))
        if(num==50):
            print("-------------------------")
            num=0
        index += 1
    # ？
    if input == ord('q'):
        break
    # 退出

cap.release()
cv2.destroyAllWindows()
