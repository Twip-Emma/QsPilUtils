'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-10-24 22:04:48
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-10-28 20:15:37
FilePath: \QsPilUtils\Entity.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw, ImageMath
BASE_PATH: str = Path(__file__).absolute().parents[0]


class FontEntity:
    def __init__(self, fsize: int = 12, color: str = "#000000", ttf_path: str = str(Path(BASE_PATH)/r"ttf"/r"zh-cn.ttf")) -> None:
        self.fsize = fsize
        self.color = color
        self.ttf_path = ttf_path

    def setColor(self, new_color):
        if new_color == None:
            raise RuntimeError("new_color cannot be empty")
        else:
            self.color = new_color


class BackgroundImage:
    def __init__(self, width: int, height: int, color: str = "#ffffff") -> None:
        self.width = width
        self.height = height
        self.color = color

    def getBg(self):
        return Image.new(mode="RGBA", size=(self.width, self.height), color=self.color)

    def changeBg(self, width: int = None, height: int = None, color: str = None) -> None:
        if not width:
            self.width = width
        if not height:
            self.height = height
        if not color:
            self.color = color
