import cv2
import numpy as np
import os.path
import copy


def SaltAndPepper(src,percetage):
    SP_NoiseImg=src.copy()
    SP_NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(SP_NoiseNum):
        randR=np.random.randint(0,src.shape[0]-1)
        randG=np.random.randint(0,src.shape[1]-1)
        randB=np.random.randint(0,3)
        if np.random.randint(0,1)==0:
            SP_NoiseImg[randR,randG,randB]=0
        else:
            SP_NoiseImg[randR,randG,randB]=255
    return SP_NoiseImg


def addGaussianNoise(image,percetage):
    G_Noiseimg = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    G_NoiseNum=int(percetage*image.shape[0]*image.shape[1])
    for i in range(G_NoiseNum):
        temp_x = np.random.randint(0,h)
        temp_y = np.random.randint(0,w)
        G_Noiseimg[temp_x][temp_y][np.random.randint(3)] = np.random.randn(1)[0]
    return G_Noiseimg


def darker(image,percetage=0.9):
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    #get darker
    for xi in range(0,w):
        for xj in range(0,h):
            image_copy[xj,xi,0] = int(image[xj,xi,0]*percetage)
            image_copy[xj,xi,1] = int(image[xj,xi,1]*percetage)
            image_copy[xj,xi,2] = int(image[xj,xi,2]*percetage)
    return image_copy


def brighter(image, percetage=1.5):
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    #get brighter
    for xi in range(0,w):
        for xj in range(0,h):
            image_copy[xj,xi,0] = np.clip(int(image[xj,xi,0]*percetage),a_max=255,a_min=0)
            image_copy[xj,xi,1] = np.clip(int(image[xj,xi,1]*percetage),a_max=255,a_min=0)
            image_copy[xj,xi,2] = np.clip(int(image[xj,xi,2]*percetage),a_max=255,a_min=0)
    return image_copy

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


file_dir = "one/"
for img_name in os.listdir(file_dir):
    img_path = file_dir + img_name
    img = cv2.imread(img_path)
    # cv2.imshow("1",img)
    # cv2.waitKey(5000)
    # ??????
    rotated_90 = rotate(img, 90)
    cv2.imwrite(file_dir + img_name[0:-4] + '_r90.jpg', rotated_90)
    rotated_180 = rotate(img, 180)
    cv2.imwrite(file_dir + img_name[0:-4] + '_r180.jpg', rotated_180)
    # ??????
    flipped_img = flip(img)
    cv2.imwrite(file_dir +img_name[0:-4] + '_fli.jpg', flipped_img)

    # ????????????
    img_gauss = addGaussianNoise(img, 0.3)
    cv2.imwrite(file_dir + img_name[0:-4] + '_noise.jpg',img_gauss)

    #??????
    img_darker = darker(img)
    cv2.imwrite(file_dir + img_name[0:-4] + '_darker.jpg', img_darker)


    blur = cv2.GaussianBlur(img, (7, 7), 1.5)
    #      cv2.GaussianBlur(?????????????????????????????????
    cv2.imwrite(file_dir + img_name[0:-4] + '_blur.jpg',blur)
