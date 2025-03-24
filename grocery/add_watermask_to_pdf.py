import os
import tempfile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
import PyPDF2
from PyPDF2 import PdfFileReader,PdfFileWriter


def add_watermark(input_pdf, watermark_text):

    # 读取输入PDF的第一页尺寸
    reader = PdfReader(input_pdf)
    first_page = reader.pages[0]
    width = float(first_page.mediabox.width)
    height = float(first_page.mediabox.height)

    # 创建水印页面
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))
    c.setFont("Helvetica", 50)
    c.setFillColorRGB(0.5, 0.5, 0.5, alpha=0.3)
    # 平移坐标系到页面中心
    c.translate(width/2, height/2)
    c.rotate(45)
    # 计算文本位置使其居中
    text_width = c.stringWidth(watermark_text, "Helvetica", 50)
    c.drawString(-text_width/2, 0, watermark_text)
    c.save()

    packet.seek(0)
    watermark = PdfReader(packet)
    watermark_page = watermark.pages[0]

    # 合并水印到每一页
    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(input_pdf, "wb") as out_file:
        writer.write(out_file)


def add_watermark(pdf_file_in, pdf_file_mark):
    outputfile = PdfWriter()
    inputfile = PdfReader(pdf_file_in)
    markfile = PdfReader(pdf_file_mark)
    for i in range(len(inputfile.pages)):
        page = inputfile.getPage(i)
        page.mergePage(markfile.getPage(0))
        outputfile.addPage(page)
    with open(pdf_file_in, 'wb') as f_out:
        outputfile.write(f_out)



def add_watermark(input_pdf, watermark_text):
    # Read the input PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Create a watermark page
    for page in reader.pages:
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)

        # Create a new PDF with ReportLab
        packet = BytesIO()
        c = canvas.Canvas(packet, pagesize=(width, height))
        c.setFont("Helvetica", 30)
        c.setFillColorRGB(0, 0, 0, alpha=0.2)

        # Rotate and add watermark text
        for x in range(0, int(width), 500):  # Adjust the step value to control horizontal spacing
            for y in range(0, int(height), 300):  # Adjust the step value to control vertical spacing
                c.saveState()
                c.translate(x, y)
                c.rotate(45)
                c.drawString(0, 0, watermark_text)
                c.restoreState()

        c.save()
        packet.seek(0)
        watermark = PdfReader(packet)
        watermark_page = watermark.pages[0]

        # Merge the watermark with the current page
        page.merge_page(watermark_page)
        writer.add_page(page)

    # Write the output PDF
    with open(input_pdf, "wb") as out_file:
        writer.write(out_file)



if __name__ == '__main__':
    add_watermark('/Users/ning.zhou/Desktop/PowerBI优化师业绩排行榜.pdf', 'ning.zhou')

