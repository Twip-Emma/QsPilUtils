'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-10-24 22:04:48
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-12-09 19:24:11
FilePath: \QsPilUtils\Entity.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw, ImageMath
BASE_PATH: str = Path(__file__).absolute().parents[0]


# 字体类
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
            return self

    def setSize(self, new_size):
        if new_size == None:
            raise RuntimeError("new_size cannot be empty")
        else:
            self.fsize = new_size
            return self

    def setTTF(self, new_ttf):
        if new_ttf == None:
            raise RuntimeError("new_ttf cannot be empty")
        else:
            self.ttf_path = str(new_ttf)
            return self


# 纯色背景类
class BackgroundImage:
    def __init__(self, width: int, height: int, color: str = "#ffffff") -> None:
        self.width = width
        self.height = height
        self.color = color

    def getBg(self):
        return Image.new(mode="RGBA", size=(self.width, self.height), color=self.color)

    def changeWidth(self, width: int = None):
        if not width:
            self.width = width
        return self

    def changeHeight(self, height: int = None):
        if not height:
            self.height = height
        return self

    def changeColor(self, color: int = None):
        if not color:
            self.color = color
        return self
