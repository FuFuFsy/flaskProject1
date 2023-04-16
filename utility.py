'''
这个文件是用来生成图片的
'''
import random
import string
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw

class ImageCode:
    def rand_color(self):
        """生成用于绘制字符串的随机颜色(可以随意指定0-255之间的数字)"""
        red = random.randint(32, 200)
        green = random.randint(22, 255)
        blue = random.randint(0, 200)
        return red, green, blue

    def gen_text(self):
        """生成4位随机字符串"""
        # sample 用于从一个大的列表或字符串中，随机取得N个字符，来构建出一个子列表
        list = random.sample(string.ascii_letters, 4)
        return ''.join(list)

    def draw_verify_code(self):
        """绘制验证码图片"""
        code = self.gen_text()
        width, height = 120, 50  # 设定图片大小，可根据实际需求调整
        im = Image.new('RGB', (width, height), 'white')  # 创建图片对象，并设定背景色为白色
        font = ImageFont.truetype(font='arial.ttf', size=40)  # 选择使用何种字体及字体大小
        draw = ImageDraw.Draw(im)  # 新建ImageDraw对象

        # 绘制字符串
        for i in range(4):
            draw.text((5 + random.randint(-3, 3) + 23 * i, 5 + random.randint(-3, 3)), text=code[i],
                      fill=self.rand_color(), font=font)
            self.draw_lines(draw, 4, width, height)  # 绘制干扰线
        # im.show()  # 如需临时调试，可以直接将生成的图片显示出来
        return im, code

    def draw_lines(self, draw, num, width, height):
        """
        绘制干扰线
        :param draw: 图片对象
        :param num: 干扰线数量
        :param width: 图片的宽
        :param height: 图片的高
        :return:
        """
        for num in range(num):
            x1 = random.randint(0, width / 2)
            y1 = random.randint(0, height / 2)
            x2 = random.randint(0, width)
            y2 = random.randint(height / 2, height)
            draw.line(((x1, y1), (x2, y2)), fill='black', width=2)

code,img=ImageCode().draw_verify_code()
print(img)
