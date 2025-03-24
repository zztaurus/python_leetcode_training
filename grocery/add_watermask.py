import os
import PyPDF2
import zipfile
import platform
import tempfile
from io import BytesIO
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw, ImageFont


class WatermarkUtility:

    def __init__(self):
        if platform.system().lower() == 'linux':
            self.font_ttf = '/usr/share/fonts/truetype/liberation/DejaVuSans-Bold.ttf'
        elif platform.system().lower() == 'darwin':
            self.font_ttf = "/System/Library/Fonts/NewYork.ttf"
        else:
            raise Exception('undefined operation %s' % platform.system())

    def add_watermark_to_pdf(self, input_pdf, output_pdf, watermark_text):
        reader = PyPDF2.PdfReader(input_pdf)
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            packet = BytesIO()
            c = canvas.Canvas(packet, pagesize=(width, height))
            c.setFont("Helvetica", 30)
            c.setFillColorRGB(0, 0, 0, alpha=0.2)
            for x in range(0, int(width), 500):
                for y in range(0, int(height), 300):
                    c.saveState()
                    c.translate(x, y)
                    c.rotate(45)
                    c.drawString(0, 0, watermark_text)
                    c.restoreState()
            c.save()
            packet.seek(0)
            watermark = PyPDF2.PdfReader(packet)
            watermark_page = watermark.pages[0]
            page.merge_page(watermark_page)
            writer.add_page(page)

        with open(output_pdf, "wb") as out_file:
            writer.write(out_file)

    def add_watermark_to_image(self, src_path, output_path, text):
        image = Image.open(src_path)
        font = ImageFont.truetype(self.font_ttf, 40, encoding="utf-8")

        # 添加背景
        new_img = Image.new('RGBA', (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
        new_img.paste(image, image.size)

        # 添加水印
        font_len = len(text)
        rgba_image = new_img.convert('RGBA')
        text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
        image_draw = ImageDraw.Draw(text_overlay)

        for i in range(0, rgba_image.size[0], font_len * 30 + 100):
            for j in range(0, rgba_image.size[1], 500):
                image_draw.text((i, j), text, font=font, fill=(0, 0, 0, 20))
        text_overlay = text_overlay.rotate(45)
        image_with_text = Image.alpha_composite(rgba_image, text_overlay)

        # 裁切图片
        image_with_text = image_with_text.crop((image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2))
        image_with_text.save(output_path)

    def add_watermark_to_file(self, file_path, out_path, watermark_text):
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == '.pdf':
            self.add_watermark_to_pdf(file_path, out_path, watermark_text)
        elif file_extension == '.png':
            self.add_watermark_to_image(file_path, out_path, watermark_text)
        elif file_extension == '.zip':
            self.add_watermark_to_zip(file_path, out_path, watermark_text)
        else:
            raise ValueError("Unsupported file type: %s" % file_extension)

    def add_watermark_to_zip(self, zip_path, out_path, watermark_text):
        with tempfile.TemporaryDirectory() as temp_dir:
            # 将原始压缩包中的所有文件解压到临时目录
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            watermarked_files = []
            # 遍历临时目录中的所有文件
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # 根据文件类型添加水印
                    elems = file_path.split('.')
                    elem_output_path = elems[0] + '_watermarked' + '.' + elems[1]
                    if file.lower().endswith('.png'):
                        self.add_watermark_to_image(file_path, elem_output_path, watermark_text)
                    elif file.lower().endswith('.pdf'):
                        self.add_watermark_to_pdf(file_path, elem_output_path, watermark_text)
                    watermarked_files.append(elem_output_path)

            # 创建一个新的压缩包并添加带水印的文件
            with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
                for root, _, files in os.walk(temp_dir):
                    for file in watermarked_files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file, temp_dir)
                        print("file_path: ", file_path)
                        print("root: ", root, " file: ", file, " file_path: ", file_path, " arcname: ", arcname)
                        # 将文件添加到新的压缩包中，保持目录结构
                        zip_ref.write(file_path, arcname )


if __name__ == '__main__':
    obj = WatermarkUtility()
    obj.add_watermark_to_image('/Users/ning.zhou/Desktop/export_file.png', '/Users/ning.zhou/Desktop/export_file_out.png', 'ning.zhou')
    # obj.add_watermark_to_file('/Users/ning.zhou/Desktop/PowerBI优化师业绩排行榜.zip',  '/Users/ning.zhou/Desktop/PowerBI优化师业绩排行榜_out.zip', 'ning.zhou')

