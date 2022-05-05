import os
from PIL import Image


def resize(old_path, new_path, size, resample):
    """
     通过指定的resample方式调整old_path下所有的jpg图片为指定的size，并保存到new_path下
    """
    if os.path.isdir(old_path):
        for child in os.listdir(old_path):

            if child.find('.jpeg') > 0:
                im = Image.open(old_path + child)
                im_crop =im.crop((520,0,1544,1024))
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                print(child, 'resize successfully!')
                im_crop.save(new_path + child, im.format)
            child_path = old_path + child + '/'

            resize(child_path, new_path, size, resample)


if __name__ == "__main__":
    old_path = "D:/Yolov3/yolo3-pytorch/zero/"
    new_path = "D:/photocrop/zero/"
    size = (1664,1664)
    resample = Image.BILINEAR # 使用线性插值法重采样
    resize(old_path, new_path, size, resample)