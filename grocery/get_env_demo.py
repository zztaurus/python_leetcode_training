

import os

def main():

    # 获取环境变量的值
    secret_id = os.getenv('SMS_SECRET_ID')
    secret_key = os.getenv('SMS_SECRET_KEY')

    # 检查并输出环境变量的值
    if secret_id is not None:
        print(f'SMS_SECRET_ID: {secret_id}')
    else:
        print('SMS_SECRET_ID is not set.')

    if secret_key is not None:
        print(f'SMS_SECRET_KEY: {secret_key}')
    else:
        print('SMS_SECRET_KEY is not set.')

if __name__ == '__main__':
    main()