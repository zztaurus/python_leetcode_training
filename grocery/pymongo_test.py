
import pymongo
import pandas as pd

def main():
    # 连接到 MongoDB
    myclient = pymongo.MongoClient('mongodb://10.0.161.151:27017')
    mydb = myclient["fastgear"]
    collection = mydb["work_calendar"]

    # 从 MongoDB 中查询数据
    filter_condition = {
        "date": "2024-12-07",  # 例如，查找 user_id 为 "12345" 的文档
        "workspace_id": "1"  # 例如，查找打卡日期为 "2023-10-01" 的文档
    }
    cursor = collection.find(filter_condition)

    # 将数据转换为 Pandas DataFrame
    df = pd.DataFrame(list(cursor))

    # 显示 DataFrame

    wc_obj = df.iloc[0]
    print(wc_obj.date_type)

    # 关闭连接
    myclient.close()


if __name__ == '__main__':
    main()

app_names = [
    'amma2023',
    'APP1',
    'APP101',
    'APP2',
    'avatoon',
    'avatoona',
    'Awild_A',
    'BiblePuzzle01A',
    'BiblePuzzle01G',
    'Brainy_A',
    'Ceres',
    'Chopin01A',
    'Chopin01G',
    'Chopin02G',
    'Chopin03A',
    'Chopin03G',
    'Chopin05A',
    'Chopin05G',
    'Chopin06A',
    'Chopin06G',
    'Citylucky',
    'City_A',
    'Classic_A',
    'Companion_A',
    'Companion_G',
    'fnnf2022',
    'Genius_A',
    'Genius_G',
    'iamma2021',
    'ieaae2024',
    'ifaaf2022',
    'ifnnf2021',
    'ikki_gp',
    'ikki_ip',
    'imttm2020',
    'ispps2019',
    'iwllw2022',
    'Jewelblockpuzzle_A',
    'Jewelpuzzle_A',
    'Jewelsliding',
    'Mini',
    'Music_A',
    'photoeditora',
    'Piggymatch_A',
    'Piggymatch_G',
    'Puzzlepool2',
    'Puzzlepool_A',
    'Security',
    'Slideadv_A',
    'Spin',
    'spps2022',
    'Superwin_A',
    'Tattoo_A',
    'Tile01A',
    'Tile01G',
    'Tile02G',
    'Triple02G',
    'Venus',
    'Washer',
    'WaterSort02G',
    'Wild',
    'Wild_A',
    'Zeus'
]

# Convert to a list of tuples
app_tuples = [(name,) for name in app_names]

print(app_tuples)