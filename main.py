'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-04-21 11:00:12
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-07-21 17:29:16
FilePath: \QsPilUtils\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from __future__ import annotations
from payload import dao

# 测试长文本转图片（必输项：文本）
# dao.text_to_image('Hello World\nPICSENCE\n\nFUCKfuck\nAmbivalent\nVision123')

# 测试长文本转图片（可选项：字号大小、左右上下的间距）
base_img, line_spacing= dao.text_to_image('你的个人信息如下：\n等级数：\n行动点：', 15, (20, 20))

a,_ = dao.text_to_image('30级', 15, color=(255, 0, 0))

b,_ = dao.text_to_image('666', 15, color=(255, 0, 0))

make1 = dao.picture_paste_img(a,base_img, (70,20 + line_spacing * 1))

make2 = dao.picture_paste_img(b,make1, (70,20 + line_spacing * 2))

make2.show()


font = dao.FontEntity()

font.setColor("123").setSize(15)