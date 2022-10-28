'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-10-14 16:24:11
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-10-28 21:21:11
FilePath: \QsPilUtils\__init__.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from handler import *
from Entity import FontEntity, BackgroundImage
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw, ImageMath


BASE_PATH: str = Path(__file__).absolute().parents[0]
print(BASE_PATH)

# test1 = Image.open(f"{BASE_PATH}\\test_image\\A.jpg")
# test2 = Image.open(f"{BASE_PATH}\\test_image\\B.jpg")

test1 = Image.open(Path(BASE_PATH)/"test_image"/"A.jpg")
test2 = Image.open(Path(BASE_PATH)/"test_image"/"B.jpg")

# a = Path(BASE_PATH)/"ttf"/"华文新魏.ttf"
# a = str(Path(BASE_PATH,"test_image/B.jpg"))


# image = picture_paste_path(f"{base_path}\\test_image\\A.jpg",f"{base_path}\\test_image\\B.jpg",location=(50,50),A_size=(100,100),B_size=(100,100))

# image = picture_paste_img(test1, test2, (50,50), (50,50), (150,150))
# 华文新魏.ttf


# font_entity = FontEntity(fsize=30)


# image = write_sh(font_entity=font_entity, img=test2, text="肯德基疯狂星期四V我50肯德基疯狂星期四V我50",
#                  mode="Center", img_size=(600, 600), dis=(100, 100))


# image.show()


long_txt = """
肯德基疯狂星\n期四V我50肯德基疯狂星期\n\n四V我50\n肯德基疯狂星期四V我5\n0肯德\n基疯狂星期四V我50肯\n\n\n德基疯狂
"""


# text = long_txt.strip().split("\n")
# print(text)

bg = BackgroundImage(500, 500)
ft = FontEntity(20)
img = write_longsh(font_entity=ft, bg=bg, text=long_txt, mode="L", dis=(150,300))
img.show()