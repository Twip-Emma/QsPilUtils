'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-10-14 16:25:19
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-10-28 21:21:31
FilePath: \QsPilUtils\handler.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pathlib import Path
from Entity import FontEntity, BackgroundImage
from PIL import Image, ImageFont, ImageDraw, ImageMath

BASE_PATH: str = Path(__file__).absolute().parents[0]


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


def picture_paste_img(img1: Image, img2: Image, location: tuple = (0, 0), A_size: tuple = None, B_size: tuple = None) -> Image:
    """
    说明:使用图片对象进行粘贴,图片A在上,图片B在下\n
    image_A_path、image_B_path:(必填参数)图片A和图片B的路径\n
    location(可选参数):确定A相对于B的位置在哪\n
    A_size、B_size(可选参数):调整A和B的图片大小
    """
    img1 = img1.convert('RGBA')
    img2 = img2.convert('RGBA')
    if A_size:
        img1 = img1.resize(A_size)
    if B_size:
        img2 = img2.resize(B_size)
    img2.paste(img1, location, img1)
    return img2


def write_sh(font_entity: FontEntity, img: Image, text: str, dis: tuple = None, mode: str = "C",
             img_size: tuple = None) -> Image:
    """
    说明: 在图片上写字
    img: 图片对象
    dis: AlignLeft模式中的上下左右边距, Center模式中为None则代表上下左右居中, 不为空则代表上边距
    color: 颜色,十六进制
    mode: 模式,可选模式有AlignLeft、Center
    img_size: 图片大小调整
    ttf_path: ttf文件路径ttf_path,不指定则为默认字体
    """
    if not text:
        raise RuntimeError("Text cannot be empty")

    if img_size:
        img = img.resize(img_size)

    if mode == "L":
        if not dis:
            dis = (0, 0)
        font = ImageFont.truetype(font_entity.ttf_path, font_entity.fsize)
        draw = ImageDraw.Draw(img)
        draw.text(xy=dis, text=text, fill=font_entity.color, font=font)
    elif mode == "C":
        font = ImageFont.truetype(font_entity.ttf_path, font_entity.fsize)
        text_width = font.getsize(text=text)
        draw = ImageDraw.Draw(img)
        text_coordinate = None
        if not dis:
            text_coordinate = int(
                (img.width-text_width[0])/2), int((img.height-text_width[1])/2)
        else:
            text_coordinate = int((img.width-text_width[0])/2), dis[0]
        draw.text(text_coordinate, text, fill=font_entity.color, font=font)
    else:
        raise RuntimeError("There is no such mode, please use \"C\" or \"L\" mode")

    return img


def write_longsh(font_entity: FontEntity, bg: BackgroundImage, text: str, mode: str = "C", dis: tuple = (0, 0)) -> Image:
    font = ImageFont.truetype(font_entity.ttf_path, font_entity.fsize)

    # 文字、图片预处理
    text = text.strip().split("\n")
    img = bg.getBg()
    draw = ImageDraw.Draw(img)

    # 写字
    top_index = dis[0]
    if mode == "C":
        for text_item in text:
            if text_item == "":
                top_index += text_width[1]
                continue
            text_width = font.getsize(text=text_item)
            text_coordinate = int((img.width-text_width[0])/2), top_index
            draw.text(text_coordinate, text_item, fill=font_entity.color, font=font)
            top_index += text_width[1]
    elif mode == "L":
        for text_item in text:
            if text_item == "":
                top_index += text_width[1]
                continue
            text_width = font.getsize(text=text_item)
            text_coordinate = dis[0], top_index
            draw.text(text_coordinate, text_item, fill=font_entity.color, font=font)
            top_index += text_width[1]
    else:
        raise RuntimeError("There is no such mode, please use \"C\" or \"L\" mode")
    return img
