
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

def main():
    df = pd.read_csv('/Users/ning.zhou/Desktop/question.csv')
    df['type'] = 1
    df['created_at'] = datetime.utcnow()
    df['updated_at'] = datetime.utcnow()
    df.drop(columns=['test'], inplace=True)

    # 创建数据库连接
    engine = create_engine('mysql+pymysql://fastgear_root:X0FZuJY8kHAr@fastgear-cluster.cluster-cnu8rzokdecb.us-east-1.rds.amazonaws.com:2306/fastgear?charset=utf8mb4')

    # 将数据写入 MySQL 数据表
    table_name = 'cognition_question'
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

    print("Data written to MySQL successfully.")



if __name__ == '__main__':
    main()