'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-10-14 16:25:19
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-10-18 18:36:09
FilePath: \QsPilUtils\handler.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PIL import Image, ImageFont, ImageDraw, ImageMath


def picture_paste_path(image_A_path: str, image_B_path: str, location: tuple = (0, 0), A_size: tuple = None, B_size: tuple = None) -> Image:
    """
    说明:使用图片路径进行粘贴,图片A在上,图片B在下\n
    image_A_path、image_B_path:(必填参数)图片A和图片B的路径\n
    location(可选参数):确定A相对于B的位置在哪\n
    A_size、B_size(可选参数):调整A和B的图片大小
    """
    img1 = Image.open(image_A_path).convert('RGBA')
    img2 = Image.open(image_B_path).convert('RGBA')
    if A_size:
        img1 = img1.resize(A_size)
    if B_size:
        img2 = img2.resize(B_size)
    img2.paste(img1, location, img1)
    return img2


