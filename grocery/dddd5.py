
import os
import zipfile
import tempfile
from concurrent.futures import ThreadPoolExecutor
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import shutil

class WatermarkProcessor:
    def __init__(self, slack_token):
        self.slack_client = WebClient(token=slack_token)

    def process_all_users(self, zip_path, users, channel):
        """批量处理所有用户"""
        with tempfile.TemporaryDirectory() as master_temp_dir:
            # 一次性解压原始文件
            with zipfile.ZipFile(zip_path, 'r') as src_zip:
                src_zip.extractall(master_temp_dir)

            # 使用线程池并行处理
            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = [
                    executor.submit(
                        self.process_single_user,
                        master_temp_dir,
                        user['name'],
                        user['slack_id'],
                        channel
                    ) for user in users
                ]
                [f.result() for f in futures]  # 等待所有任务完成

    def process_single_user(self, master_temp_dir, username, slack_id, channel):
        """处理单个用户的逻辑"""
        with tempfile.TemporaryDirectory() as user_temp_dir:
            # 复制原始文件到用户临时目录
            self.copy_tree(master_temp_dir, user_temp_dir)

            # 添加水印
            for root, _, files in os.walk(user_temp_dir):
                for file in files:
                    if file.lower().endswith('.png'):
                        file_path = os.path.join(root, file)
                        self.add_watermark_to_image(file_path, username)

            # 创建带水印的ZIP
            output_zip = os.path.join(user_temp_dir, "processed_files.zip")
            with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as dst_zip:
                for root, _, files in os.walk(user_temp_dir):
                    for file in files:
                        if file != "processed_files.zip":  # 排除自身
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, user_temp_dir)
                            dst_zip.write(file_path, arcname)

            # 上传到Slack
            self.upload_to_slack(output_zip, slack_id, channel)

    def copy_tree(self, src, dst):
        """安全复制目录树"""
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks=True)
            else:
                shutil.copy2(s, d)

    def add_watermark_to_image(self, image_path, watermark_text):
        """添加图片水印的具体实现"""
        # 这里需要实现实际的水印添加逻辑
        # 例如使用Pillow库操作图片
        pass

    def upload_to_slack(self, zip_path, user_id, channel):
        """上传文件到Slack"""
        try:
            response = self.slack_client.files_upload(
                channels=channel,
                file=zip_path,
                initial_comment=f"<@{user_id}> 您的水印文件已就绪！",
                title="带水印的文件包"
            )
            print(f"成功上传文件给用户 {user_id}")
        except SlackApiError as e:
            print(f"Slack上传错误: {e.response['error']}")

# 使用示例
if __name__ == "__main__":
    SLACK_TOKEN = "xoxb-your-token"
    USERS = [
        {"name": "张三", "slack_id": "U12345"},
        {"name": "李四", "slack_id": "U23456"},
        # 添加其他3个用户...
    ]

    processor = WatermarkProcessor(SLACK_TOKEN)
    processor.process_all_users(
        zip_path="original_files.zip",
        users=USERS,
        channel="#watermark-files"
    )
