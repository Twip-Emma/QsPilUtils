'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-10-14 16:25:19
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-10-15 13:23:58
FilePath: \QsPilUtils\handler.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PIL import Image, ImageFont, ImageDraw, ImageMath


# 【粘贴】图片A放到图片B上面
def picture_paste_normal(image_A_path:str, image_B_path:str) -> Image:
    """
        说明:图片A放到图片B上面
        对齐:左上角对齐
        支持:支持有透明区域的png格式
    """
    img1 = Image.open(image_A_path).convert('RGBA')
    img2 = Image.open(image_B_path).convert('RGBA')
    return Image.alpha_composite(img1, img2)

# 定位粘贴
def picture_paste_location(image_A_path:str, image_B_path:str, location:tuple) -> Image:
    """
        说明:图片A放到图片B上面
        对齐:根据location对齐
        支持:支持有透明区域的png格式
    """
    img1 = Image.open(image_A_path).convert('RGBA')
    bg = Image.open(image_B_path).convert('RGBA')
    bg.paste(img1, location, img1)
    return bg

# 调整图片大小定位粘贴
def picture_paste_size(image_A_path:str, image_B_path:str, location:tuple, A_size:tuple, B_size:tuple) -> Image:
    """
        说明:图片A放到图片B上面
        对齐:根据location对齐,根据size调整两张图片大小
        支持:支持有透明区域的png格式
    """
    img1 = Image.open(image_A_path).convert('RGBA').resize(A_size)
    bg = Image.open(image_B_path).convert('RGBA').resize(B_size)
    bg.paste(img1, location, img1)
    return bg