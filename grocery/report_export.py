import time

import requests


groupId = "a97b1994-25c6-4e95-829b-a830c991fa74"
reportId = "dd11c055-f0c4-4b34-a2c5-0fec0d11da39"

Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkpETmFfNGk0cjdGZ2lnTDNzSElsSTN4Vi1JVSIsImtpZCI6IkpETmFfNGk0cjdGZ2lnTDNzSElsSTN4Vi1JVSJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvYWE1ODIyZjUtODk4ZS00MzEwLTkyYmItNTY0ODg1MGJhMGUyLyIsImlhdCI6MTc0MTY3NTQxOSwibmJmIjoxNzQxNjc1NDE5LCJleHAiOjE3NDE2NzkzMTksImFpbyI6ImsyUmdZT2lPTy81ZnN2NXVmRkhKaHFDanN3UHNBUT09IiwiYXBwaWQiOiJhMzY3ZDQ4NC1kMDQyLTQzM2EtYWNlZS1jZjNmNTc3ZWRlZDIiLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9hYTU4MjJmNS04OThlLTQzMTAtOTJiYi01NjQ4ODUwYmEwZTIvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiI3NDA1ZGQzMy0xZjk2LTQxZDEtYTJjOC1kY2U4MmE3M2NhZmMiLCJyaCI6IjEuQVVrQTlTSllxbzZKRUVPU3UxWkloUXVnNGdrQUFBQUFBQUFBd0FBQUFBQUFBQUFvQVFCSkFBLiIsInJvbGVzIjpbIlRlbmFudC5SZWFkV3JpdGUuQWxsIiwiVGVuYW50LlJlYWQuQWxsIl0sInN1YiI6Ijc0MDVkZDMzLTFmOTYtNDFkMS1hMmM4LWRjZTgyYTczY2FmYyIsInRpZCI6ImFhNTgyMmY1LTg5OGUtNDMxMC05MmJiLTU2NDg4NTBiYTBlMiIsInV0aSI6IkItamliN1U5MmtlMTlNVzRfVjRlQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfaWRyZWwiOiI3IDMwIn0.ZVffR9z2vgNh3eFX4kAgdL-5obl_iIAh2Ag6GfOg-86smvKm6t4ZwbFfG-0zjYJEd8K6ANaP5bIykO-xrc5bktaeTQZGYVRFQehnq3z-UB2tw9PXUM5bJskVlsp7raLMj_Hpub-CUC3WBMhtSm3hEWbMmvSCDdhdGWCU5SbW4B9XtGlOABar9y-R5gVlSG5_OyvJ7Dixma9rxOqlW-E-d3FvqZopSBlGQQPce7uUDjj31owBatLAbA0zY9pOtaK-YDbdxnGc--hV9UnDgYBNcj3tJ5Mp7ASArHUl3dUuNC7gAXgPq3j_K7x9_TDPGCKfy8Hx40HupLHZEAteoMkqLw"
def main():

    # 设置请求的 URL

    url = f"https://api.powerbi.com/v1.0/myorg/groups/{groupId}/reports/{reportId}/ExportTo"
    print(url)
    # 设置请求头，包括授权信息, filter信息
    headers = {
        "Authorization": Authorization
    }

    body = {
        "format": "PNG",
        "powerBIReportConfiguration": {
            "reportLevelFilters": [
                {
                    "filter": "optimizer_performance_report/optimizer_name in ('alia', 'alice', 'boxy', 'brisa', 'cassie', 'Chloe', 'dylan', 'fiona', 'frank', 'hebe', 'Howard', 'Jenny') and optimizer_performance_report/optimizer_division eq 'F919'"
                }
            ]
        }
    }



    print(body)
    # 发送 GET 请求
    response = requests.post(url, json=body, headers=headers)
    print(response.json())
    resp = response.json()
    exportId = resp["id"]
    print(exportId)


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
    time.sleep(30)
    exportToFile(exportId)
