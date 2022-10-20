'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-10-14 16:24:11
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-10-20 15:14:05
FilePath: \QsPilUtils\__init__.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from handler import *
from os import path
from PIL import Image, ImageFont, ImageDraw, ImageMath


base_path:str = path.join(path.dirname(__file__))

test1 = Image.open(f"{base_path}\\test_image\\A.jpg")
test2 = Image.open(f"{base_path}\\test_image\\B.jpg")


# image = picture_paste_path(f"{base_path}\\test_image\\A.jpg",f"{base_path}\\test_image\\B.jpg",location=(50,50),A_size=(100,100),B_size=(100,100))

# image = picture_paste_img(test1, test2, (50,50), (50,50), (150,150))
# 华文新魏.ttf

image = write_sh(img = test2, text="肯德基疯狂星期四V我50", \
fsize=10,mode="AlignLeft",img_size=(200,200), dis=(100,100), ttf_path = base_path + "\\ttf\\华文新魏.ttf")



image.show()