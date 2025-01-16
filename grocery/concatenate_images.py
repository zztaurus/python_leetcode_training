import os
from PIL import Image

def concatenate_images(image_paths, direction='horizontal'):
    # 打开所有图片
    images = [Image.open(image_path) for image_path in image_paths]

    # 确定拼接方向
    if direction == 'horizontal':
        # 计算总宽度和最大高度
        total_width = sum(image.width for image in images)
        max_height = max(image.height for image in images)
        # 创建一个新的空白图像
        new_image = Image.new('RGB', (total_width, max_height))
        # 拼接图片
        x_offset = 0
        for image in images:
            new_image.paste(image, (x_offset, 0))
            x_offset += image.width
    elif direction == 'vertical':
        # 计算总高度和最大宽度
        total_height = sum(image.height for image in images)
        max_width = max(image.width for image in images)
        # 创建一个新的空白图像
        new_image = Image.new('RGB', (max_width, total_height))
        # 拼接图片
        y_offset = 0
        for image in images:
            new_image.paste(image, (0, y_offset))
            y_offset += image.height
    else:
        raise ValueError("Direction must be 'horizontal' or 'vertical'")

    return new_image

def main():
    # 示例图片路径
    # for image_path in os.listdir('images'):
    image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']

    # 拼接图片
    result_image = concatenate_images(image_paths, direction='horizontal')

    # 保存结果
    result_image.save('concatenated_image.jpg')


if __name__ == '__main__':
    main()
