'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-10-14 16:24:11
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-10-15 13:12:07
FilePath: \QsPilUtils\__init__.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from handler import *
from os import path


base_path:str = path.join(path.dirname(__file__))


image = picture_paste_location(f"{base_path}\\test_image\\A.jpg",f"{base_path}\\test_image\\B.jpg",(100,100))
image.show()