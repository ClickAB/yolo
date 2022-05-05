# coding = utf-8
import cv2
from PIL import Image
from PIL import ImageEnhance
from numpy.ma import array
import numpy as np
import os
import os.path
import copy
# 批量处理代码


def high_bright(currentPath, filename, targetPath):
    # 读取图像
    image = Image.open(currentPath)
    image_cv = cv2.imread(currentPath)
    # image.show()
    # 增强亮度 bh_
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 1.25
    image_brightened_h = enh_bri.enhance(brightness)
    # image_brightened_h.show()
    image_brightened_h.save(currentPath+ '1' + filename)  # 保存

def low_bright(currentPath, filename, targetPath):
    image = Image.open(currentPath)
    image_cv = cv2.imread(currentPath)
    # 降低亮度 bl_
    enh_bri_low = ImageEnhance.Brightness(image)
    brightness = 0.80
    image_brightened_low = enh_bri_low.enhance(brightness)
    # image_brightened_low.show()
    image_brightened_low.save(currentPath+ '2' + filename)

def color(currentPath, filename, targetPath):
    image = Image.open(currentPath)
    image_cv = cv2.imread(currentPath)
    # 改变色度 co_
    enh_col = ImageEnhance.Color(image)
    color = 0.8
    image_colored = enh_col.enhance(color)
    # image_colored.show()
    image_colored.save(currentPath + '3' + filename)

def cont(currentPath, filename, targetPath):
    image = Image.open(currentPath)
    image_cv = cv2.imread(currentPath)
    # 改变对比度 cont_
    enh_con = ImageEnhance.Contrast(image)
    contrast = 0.5
    image_contrasted = enh_con.enhance(contrast)
    # image_contrasted.show()
    image_contrasted.save(currentPath+'4' + filename)


def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    # If no rotation center is specified, the center of the image is set as the rotation center
    if center is None:
        center = (w / 2, h / 2)
    m = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, m, (w, h))
    return rotated

def flip(image):
    flipped_image = np.fliplr(image)
    return flipped_image
rootdir = 'D:/photocrop/nine' # 指明被遍历的文件夹
file_dir = rootdir

abc=os.listdir(file_dir)
for  filename in os.listdir(rootdir):

            # print('parent is:' + parent)
            print('filename is: ' + filename)
            # 把文件名添加到一起后输出
            currentPath = os.path.join(rootdir, filename)
            # print('the full name of file is :' + currentPath)
            # 保存处理后的图片的目标文件夹
            targetPath = 'D:/test'
            # 进行处理
            high_bright(currentPath, filename, targetPath)
            low_bright(currentPath, filename, targetPath)
            color(currentPath, filename, targetPath)
            cont(currentPath, filename, targetPath)


for img_name in abc:
        img_path = file_dir + img_name
        img = cv2.imread(img_path)
        # cv2.imshow("1",img)
        # cv2.waitKey(5000)
        # 旋转
        rotated_90 = rotate(img, 90)
        cv2.imwrite(file_dir + img_name[0:-4] + '_r90.jpg', rotated_90)
        rotated_180 = rotate(img, 180)
        cv2.imwrite(file_dir + img_name[0:-4] + '_r180.jpg', rotated_180)
        rotated_270 = rotate(img, 270)
        cv2.imwrite(file_dir + img_name[0:-4] + '_r270.jpg', rotated_270)
        # 镜像
        flipped_img = flip(img)
        cv2.imwrite(file_dir + img_name[0:-4] + '_fli.jpg', flipped_img)