import time
import requests


groupId = "a97b1994-25c6-4e95-829b-a830c991fa74"
reportId = "196731e1-bde1-442d-adc7-4a336e560fdd"

Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSIsImtpZCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvYWE1ODIyZjUtODk4ZS00MzEwLTkyYmItNTY0ODg1MGJhMGUyLyIsImlhdCI6MTc0NDE2MTQwMSwibmJmIjoxNzQ0MTYxNDAxLCJleHAiOjE3NDQxNjUzMDEsImFpbyI6ImsyUmdZTEE4ZE1QYk5uRGkxUjJKN0hzdmI1Ri9EUUE9IiwiYXBwaWQiOiJhMzY3ZDQ4NC1kMDQyLTQzM2EtYWNlZS1jZjNmNTc3ZWRlZDIiLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9hYTU4MjJmNS04OThlLTQzMTAtOTJiYi01NjQ4ODUwYmEwZTIvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiI3NDA1ZGQzMy0xZjk2LTQxZDEtYTJjOC1kY2U4MmE3M2NhZmMiLCJyaCI6IjEuQVVrQTlTSllxbzZKRUVPU3UxWkloUXVnNGdrQUFBQUFBQUFBd0FBQUFBQUFBQUFvQVFCSkFBLiIsInJvbGVzIjpbIlRlbmFudC5SZWFkV3JpdGUuQWxsIiwiVGVuYW50LlJlYWQuQWxsIl0sInN1YiI6Ijc0MDVkZDMzLTFmOTYtNDFkMS1hMmM4LWRjZTgyYTczY2FmYyIsInRpZCI6ImFhNTgyMmY1LTg5OGUtNDMxMC05MmJiLTU2NDg4NTBiYTBlMiIsInV0aSI6IkhiXzJJSkZIWDBtWEVBMzE3N2VTQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfaWRyZWwiOiI3IDIifQ.aOT79yYVLOO3KTkHY0oDdk7mNbLf_NHuWoNcqcC5YDCAr9dlLcDLzg7NVuX_pHNWG07iz1w11RC_bKlu0jTL9BuaKzuO9poY4KmTcdIWPNYSadC9IvALunKMD9-l0fjoCWhVI1jjt0V-W3shP9jFwRNslzoT-cU7iD0H81IM_RSCclnSmNbkuuQASItnKre3f0AFdLn_NHUD-RzXXXc_SG8Ymp6icxPdU3Bgw37oMNRTEbUvAzAwGcNV-R8VSnl4jbJvq-i__EI5qjSJjXi5PivYzGkJu2MkdqSseq2Gd0He2xiHpA0dVQtQTdVbwRbpW-3YpuYMfYdK6_y24kmObQ"


def main():

    # 设置请求的 URL
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports/{reportId}/ExportTo"
    headers = {
        "Authorization": Authorization
    }
    body = {
        "format": "PNG",
        "powerBIReportConfiguration": {
            "reportLevelFilters": [
                {
                    "filter": "halfyear_optimizer_performance_report/optimizer_name in ('frank', 'alia', 'norine', 'unknown', 'josi', 'tigris', 'Jenny', 'hebe', 'fiona', 'marina', 'zhongju.wang', 'mary', 'alexis', 'pedro.dinis', 'emircan.erdogan', 'nana', 'nacho', 'cassie', 'joseph', 'ying', 'yunhong.tan', 'boxy', 'jillian', 'logan', 'Jillian', 'Chloe', 'alice', 'Howard', 'cindy.dmc', 'lilo', 'brisa')"
                }
            ]
        }
    }

    response = requests.post(url, json=body, headers=headers)
    resp = response.json()
    exportId = resp["id"]
    print(exportId)

    # print(body)
    # # 发送 GET 请求
    # response = requests.post(url, json=body, headers=headers)
    # print(response.json())
    # resp = response.json()
    # exportId = resp["id"]
    # print(exportId)


    # 检查请求是否成功
    # if response.status_code == 200:
    #     # 打印响应内容
    #     print(response.json())
    # else:
    #     print(f"请求失败，状态码: {response.status_code}")

    # url = f"https://api.powerbi.com/v1.0/myorg/reports/{reportId}/exports/{exportId}"
    # response = requests.get(url, headers=headers)
    # print(response.json())

    return exportId


def get_status(exportId):
    headers = {
        "Authorization": Authorization
    }
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports/{reportId}/exports/{exportId}"
    response = requests.get(url, headers=headers)
    print(response.json())

def exportToFile(exportId):
    headers = {
        "Authorization": Authorization
    }

    url = f"https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports/{reportId}/exports/{exportId}/file"
    response = requests.get(url, headers=headers)
    content_type = response.headers.get('Content-Type', '')
    if 'application/zip' in content_type:
        file_extension = '.zip'
    elif 'application/pdf' in content_type:
        file_extension = '.pdf'
    elif 'image/' in content_type:
        file_extension = '.png'  # 假设是 PNG 图片
    elif 'text/csv' in content_type:
        file_extension = '.csv'
    elif 'text/xml' in content_type:
        file_extension = '.xml'
    else:
        file_extension = '.dat'  #

    file_name = f"/Users/ning.zhou/Desktop/exported_file{file_extension}"

    # 将文件写入磁盘
    with open(file_name, 'wb') as file:
        file.write(response.content)



if __name__ == '__main__':
    exportId = main()
    # get_status("Mi9CbG9SWRWMi1hNTEzZTA5NC03Nzk1LTQ1YjUtYWEzOC01MWQ1ZTc1MThkMTU4dHQtVXVuM0g0d1VxY0hTNnlLMmc3MklhQTZmVWgtTEtNZ0ZVaDJjSzVrPS4=")
    time.sleep(120)
    # exportId = "Mi9CbG9iSWRWMi0wMWQxOTRiOC1mYWI5LTQwNmMtYmZkMC0wNGIyZTIyNmZmY2ZUcXY2aExtZzJNVW9Ya3NOc2YtcVRmb2J3Z215RUhxMjl6Lg=="
    exportToFile(exportId)
    # exportToFile("Mi9CbG9iSWRWMi1iNGYyYThiZC04MWQ5LTQ4ZmQtOWYzOC0xNjdjYmIxNzRlMGRHMXVJMlJpRmx5NThYZm1lU1Y4aGwxQlEu")
