from pathlib import Path
BASE_PATH: str = Path(__file__).absolute().parents[0]
import re

from PIL import Image, ImageDraw, ImageFont

def text_to_image(text: str, font_size: int = 20, spacing: tuple = (0, 0)):
    """
    文本转图像
    text:str 文本
    font_size:int = 20 字体大小
    spacing:tuple = (0,0) 上下左右间距
    """
    # 设置字体、字号、行高
    font_path = f'{BASE_PATH}\\ttf\\zh-cn.ttf'
    font = ImageFont.truetype(font_path, font_size)
    line_spacing = font.getsize('A')[1] + 8  # 行高比字体高度多8个像素

    # 计算文本宽度和高度
    lines = text.strip().split('\n')
    width = max(font.getsize(line)[0] for line in lines) + spacing[0] * 2
    height = line_spacing * len(lines) + spacing[1] * 2

    # 创建空白的图片对象
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # 在图片上绘制文本
    draw = ImageDraw.Draw(image)
    x, y = spacing[0], spacing[1]
    for line in lines:
        draw.text((x, y), line, font=font, fill=(0, 0, 0))
        y += line_spacing

    # 保存图片
    image.save(f'{BASE_PATH}\\cache\\long_text.jpg')


# 内部函数-获取颜色文本
def match_sentences_with_colors(input_string):
    pattern = r"<(\w+)>(.*?)</\w+>"
    matches = re.findall(pattern, input_string)
    color_dict = {}
    result = []

    for match in matches:
        color = match[0]
        sentence = match[1]

        if color not in color_dict:
            color_dict[color] = []
        
        color_dict[color].append(sentence)

    for color, sentences in color_dict.items():
        sentence_with_color = {color: ' '.join(sentences)}
        result.append(sentence_with_color)

    default_text = re.sub(pattern, lambda m: '' * len(m.group()), input_string)
    default_sentence = {'default': default_text}
    result.insert(0, default_sentence)

    return result


def generate_colored_text_image(input_text):
    # 配置参数
    font_size = 20  # 字体大小
    padding = 10  # 图像边缘留白
    tag_pattern = r"<(\w+)>(.*?)</\w+>"  # 标签匹配正则表达式
    default_color = (0, 0, 0)  # 默认颜色为黑色

    # 处理标签和文本
    matches = re.findall(tag_pattern, input_text)
    parts = re.split(tag_pattern, input_text)

    # 计算图像尺寸
    image_width = max([len(part) for part in parts]) * (font_size // 2) + padding * 2
    num_lines = input_text.count('\n') + 1
    line_height = font_size + padding  # 行高
    image_height = num_lines * line_height + padding * 2

    # 创建图像
    image = Image.new('RGB', (image_width, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', font_size)

    # 渲染默认文本
    y = padding
    for part in parts:
        lines = part.split('\n')
        for line in lines:
            draw.text((padding, y), line, font=font, fill=default_color)
            y += line_height

    # 渲染标签文本
    for match in matches:
        tag = match[0]
        text = match[1]
        color = default_color
        if tag == 'red':
            color = (255, 0, 0)  # 红色
        elif tag == 'green':
            color = (0, 255, 0)  # 绿色
        elif tag == 'blue':
            color = (0, 0, 255)  # 蓝色

        # 在图像上绘制标签文本
        start_x = input_text.index(text)
        start_y = input_text[:start_x].count('\n') * line_height + padding
        end_x = start_x + len(text)
        end_y = start_y + line_height
        draw.rectangle((start_x, start_y, end_x, end_y), fill=color)
        draw.text((start_x, start_y), text, font=font, fill=default_color)
    
    image.save(f'{BASE_PATH}\\cache\\long_text2.jpg')
    return image