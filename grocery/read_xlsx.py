

import pandas as pd



def main():
    # 读取 Excel 文件
    df = pd.read_excel('/Users/ning.zhou/Desktop/question.xlsx', engine='openpyxl')

    df = df.rename(columns={
        "cognitive_bot_ai_message.id": "cognition_id",
        "cognition_question.tags": "tags",
        "cognitive_bot_ai_message.ai_text": "text"
    })

    # 显示数据框的前几行
    print(df.columns)

    df.to_csv('/Users/ning.zhou/Desktop/question.csv', index=False)


def job1():
    df = pd.read_csv('/Users/ning.zhou/Desktop/insight.csv')
    print(len(df))


if __name__ == '__main__':
    job1()