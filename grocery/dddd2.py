import zlib
import pandas as pd


def main():
    df = pd.read_csv('/Users/ning.zhou/Desktop/cognition_question.csv')

def job2():

    data = b"x\x9ck`\x99\xea\xc3\x00\x01\x1a=\x8e\x89y\x899\x95%\x99\xc9\xc5z%\x89\xc5\xd9\xc5z\xc5\xc9\x19\xa9)\xa59\xa9\xf1Y\xf9Iz\xc5\xa5I\xc5\xc9E\x99\x05%\x99\xf9yz\xc5\xa9y)\xf1\xc8\"\xf1\xa9\xb9\x89\x999S\xfc4k\xa7\x94L\xd1\x03\x00\xfd\x17\x1f\xf4"

    # 解压缩数据
    try:
        decompressed_data = zlib.decompress(data)
        print("解压缩后的 data:", decompressed_data)
    except zlib.error as e:
        print(f"解压缩失败: {e}")


if __name__ == "__main__":
    job2()