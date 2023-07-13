'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-04-21 11:00:12
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-07-13 17:42:44
FilePath: \QsPilUtils\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-10-14 16:24:11
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2023-07-13 17:37:12
FilePath: \QsPilUtils\__init__.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from payload import dao

# 测试长文本转图片（必输项：文本）
dao.text_to_image('Hello World\nPICSENCE\n\nFUCKfuck\nAmbivalent\nVision123')

# 测试长文本转图片（可选项：字号大小、左右上下的间距）
dao.text_to_image('Hello World\nPICSENCE\n\nFUCKfuck\nAmbivalent\nVision123', 35, (20,50))
