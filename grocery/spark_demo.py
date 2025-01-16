from pyspark import spark
from datetime import datetime, timedelta

def split_date_range(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d') if isinstance(start_date, str) else start_date
    end_date = datetime.strptime(end_date, '%Y-%m-%d') if isinstance(end_date, str) else end_date
    date_list = []
    while end_date >= start_date:
        date_list.append(start_date.strftime('%Y-%m-%d'))
        start_date += timedelta(days=1)
    return date_list


def main():
    files = []
    from datetime import datetime
    current_date = datetime.utcnow().strftime("%Y-%m-%d")
    print(current_date)
    for date in split_date_range('2024-10-01', '2025-01-14'):
        files.append(f"Files/4495-datalake-servicedata/hamburger/media_region_user_roas/date={date}/global/*.parquet")
        files.append(f"Files/4495-datalake-servicedata/hamburger/media_region_user_roas/date={date}/cn/*.parquet")
    # df1 = spark.read.parquet("Files/4495-datalake-servicedata/hamburger/media_region_user_roas/date=2025-01-11/global")
    # df2 = spark.read.parquet("Files/4495-datalake-servicedata/hamburger/media_region_user_roas/date=2025-01-11/cn")
    df = spark.read.parquet(*files)
    # df now is a Spark DataFrame containing parquet data from "Files/4495-datalake-servicedata/hamburger/media_region_user_roas/date=2025-01-11/".
    print(df)
    spark.sql("DROP TABLE IF EXISTS campaign_daily_report")
    df.write.format('delta').saveAsTable('campaign_daily_report')