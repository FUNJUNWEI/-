# -*- coding: utf-8 -*-
#将目录下的'jpg','png''jpeg'图片批量圆角化

from PIL import Image, ImageDraw
import os


#圆角处理函数
def circle_corner(img):
    """
    圆角处理
    :param img: 源图象。
    :param radii: 半径，如：30。
    :return: 返回一个圆角处理后的图象。
    """
    # 原图属性
    img = img.convert("RGBA")
    w, h = img.size

    if w <= 1000:
        radii = 60
    else:
        radii = 120


    # 画圆（用于分离4个角）
    circle = Image.new('LA', (radii * 2, radii * 2), 0)  # 创建一个黑色背景的画布
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radii * 2, radii * 2), fill=255) # 画白色圆形



    # 画4个角（将整圆分离为4个部分）
    alpha = Image.new('L', img.size, 255)
    alpha.paste(circle.crop((0, 0, radii, radii)), (0, 0))  # 左上角
    alpha.paste(circle.crop((radii, 0, radii * 2, radii)), (w - radii, 0))  # 右上角
    alpha.paste(circle.crop((radii, radii, radii * 2, radii * 2)), (w - radii, h - radii))  # 右下角
    alpha.paste(circle.crop((0, radii, radii, radii * 2)), (0, h - radii))  # 左下角

    img.putalpha(alpha)  # 白色区域透明可见，黑色区域不可见
    return img

path = os.getcwd()
listdir = os.listdir(path)
image_extension=('jpg','png''jpeg')
for file in listdir:
    Filename_Extension = file.split('.')[-1]
    Filename = file.split('.')[0]
    if  Filename_Extension in image_extension:
        img = Image.open(file)
        img = circle_corner(img)
        img.save(path + '\\' + Filename + '.png',format = 'PNG')
