import requests


table_name = 'campaign_daily_report'
field_name = 'platform'
value = 'android'
app_name = 'Genius_G'
reportId = "6ba19260-1539-405e-adc3-28653068176d"
exportId = "Mi9CbG9iSWRWMi03ZDVlMDM1Ny1mODg3LTQwZDctYWUxOC1iOGJmNzA5MzhiYWNwWkJJRWJtdkdpdFE3SWVDNVFnSjZBWlU3NGNZMlM4WDV5bFRVRzk0LXZzPS4="

Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyIsImtpZCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvYWE1ODIyZjUtODk4ZS00MzEwLTkyYmItNTY0ODg1MGJhMGUyLyIsImlhdCI6MTczNzQ0NDA5NCwibmJmIjoxNzM3NDQ0MDk0LCJleHAiOjE3Mzc0NDkzMjYsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84WkFBQUE3UGlvMEdFdnRHZTBTc3ZKTStWeWNJTGRWRG5aZTQrUm5BdWw5ZXBWR3lOUDExQUhSSzdBWDE5RmlCTkpFeXlhc2w4endqOS9SR0xncGpJSk43cjJFaWh0R0dHb0J0Q3JCK3MxS0lUc1ZsYz0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiMThmYmNhMTYtMjIyNC00NWY2LTg1YjAtZjdiZjJiMzliM2YzIiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJaaG91IiwiZ2l2ZW5fbmFtZSI6Ik5pbmciLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMDMuMTAwLjY0LjEyMiIsIm5hbWUiOiJOaW5nIFpob3UiLCJvaWQiOiJhZjZlNWNlMi1mNGE5LTQ3YTUtYjkwNS00OWFkYWUwYzc5Y2YiLCJwdWlkIjoiMTAwMzIwMDA3QzJBNzA2OSIsInJoIjoiMS5BVWtBOVNKWXFvNkpFRU9TdTFaSWhRdWc0Z2tBQUFBQUFBQUF3QUFBQUFBQUFBQW9BWE5KQUEuIiwic2NwIjoiQXBwLlJlYWQuQWxsIENhcGFjaXR5LlJlYWQuQWxsIENhcGFjaXR5LlJlYWRXcml0ZS5BbGwgQ29ubmVjdGlvbi5SZWFkLkFsbCBDb25uZWN0aW9uLlJlYWRXcml0ZS5BbGwgQ29udGVudC5DcmVhdGUgRGFzaGJvYXJkLlJlYWQuQWxsIERhc2hib2FyZC5SZWFkV3JpdGUuQWxsIERhdGFmbG93LlJlYWQuQWxsIERhdGFmbG93LlJlYWRXcml0ZS5BbGwgRGF0YXNldC5SZWFkLkFsbCBEYXRhc2V0LlJlYWRXcml0ZS5BbGwgR2F0ZXdheS5SZWFkLkFsbCBHYXRld2F5LlJlYWRXcml0ZS5BbGwgSXRlbS5FeGVjdXRlLkFsbCBJdGVtLkV4dGVybmFsRGF0YVNoYXJlLkFsbCBJdGVtLlJlYWRXcml0ZS5BbGwgSXRlbS5SZXNoYXJlLkFsbCBPbmVMYWtlLlJlYWQuQWxsIE9uZUxha2UuUmVhZFdyaXRlLkFsbCBQaXBlbGluZS5EZXBsb3kgUGlwZWxpbmUuUmVhZC5BbGwgUGlwZWxpbmUuUmVhZFdyaXRlLkFsbCBSZXBvcnQuUmVhZFdyaXRlLkFsbCBSZXBydC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkV3JpdGUuQWxsIFRlbmFudC5SZWFkLkFsbCBUZW5hbnQuUmVhZFdyaXRlLkFsbCBVc2VyU3RhdGUuUmVhZFdyaXRlLkFsbCBXb3Jrc3BhY2UuR2l0Q29tbWl0LkFsbCBXb3Jrc3BhY2UuR2l0VXBkYXRlLkFsbCBXb3Jrc3BhY2UuUmVhZC5BbGwgV29ya3NwYWNlLlJlYWRXcml0ZS5BbGwiLCJzaWQiOiJkNDQ0ZThhNy05ZDI4LTRhOGUtYjk3ZC1hZmY1ZjdmMWRlNjEiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiIxTEFxck1wUGpaaHlBOGc5WkNQRHpXSzV1dVN4TjVDRnVjYl9vanI4RVFzIiwidGlkIjoiYWE1ODIyZjUtODk4ZS00MzEwLTkyYmItNTY0ODg1MGJhMGUyIiwidW5pcXVlX25hbWUiOiJuaW5nLnpob3VAZXdwLWdyb3VwLmNvbSIsInVwbiI6Im5pbmcuemhvdUBld3AtZ3JvdXAuY29tIiwidXRpIjoiOVhEd1VwdW40a0tvVk9zTnlvLWZBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19pZHJlbCI6IjEgMjQifQ.Yul8oKJlH3g20uTDO1jCnuXjCaW06wlsQe4a0zMn7RtX89ONwxMYIzn0M3jiNaR6SkLKGkAaWcRHIy1TV6882MwhfXaqoCVzbYokG4ef1DCnGTibs5KCJyrXP5sQrEK_cONX5cN7vIxwBNB9mKhpG46nYfZhATjf1uPo_vdrzkw3HZ_i1Dha9jAU_NMWCHqqeRHyPJzTU1XrZ1-HB5DfrevfmtlfPnkbNqnEHR5hb6rGJX7kBkoGQkhFzp_jxhOmwEs-s0axzsrRhv4dzNIp8n_MOVyhLT15M34LCeAgYX-rVP-Qs-hRQzLPVcHaCRSN9_SCzgwOZmXMqVsMRaz6wA"

def main():

    # 设置请求的 URL

    url = f"https://api.powerbi.com/v1.0/myorg/reports/{reportId}/ExportTo"
    # 设置请求头，包括授权信息, filter信息
    headers = {
        "Authorization": Authorization
    }
    body = {
        "format": "PDF",
        "powerBIReportConfiguration": {
            "reportLevelFilters": [
                {
                    "filter": f"{table_name}/{field_name} eq '{value}'" + " and " +  f"{table_name}/spend gt 1000"
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


def get_status():
    headers = {
        "Authorization": Authorization
    }
    url = f"https://api.powerbi.com/v1.0/myorg/reports/{reportId}/exports/{exportId}"
    response = requests.get(url, headers=headers)
    print(response.json())

def exportToFile():
    headers = {
        "Authorization": Authorization
    }
    url = f"https://api.powerbi.com/v1.0/myorg/reports/{reportId}/exports/{exportId}/file"
    response = requests.get(url, headers=headers)
    # print(response.text)
    content_type = response.headers.get('Content-Type', '')
    print(content_type)
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
    # main()
    # get_status()
    exportToFile()

blks = [
    {
        "type": "divider",
        "block_id": "ctdHw"
    },
    {
        "type": "section",
        "block_id": "HOxjG",
        "text": {
            "type": "mrkdwn",
            "text": "*:two: 在游戏剧情类素材中，背景过于空旷可能导致什么问题？*\nA. 增强画面的故事性\nB. 使画面内容显得分散\nC. 提升玩家的代入感\nD. 增加画面的细节感",
            "verbatim": False
        }
    },
    {
        "type": "section",
        "block_id": "xujY9",
        "text": {
            "type": "mrkdwn",
            "text": ":x:，答案： *B* \n*认知：* <https://ihandy-debug-08.infastgear.com/insight/list/detail/236977649249?page=1|【认知】背景不要太空，会显得画面内容很散>",
            "verbatim": False
        }
    },
    {
        "type": "section",
        "block_id": "baIcW",
        "text": {
            "type": "mrkdwn",
            "text": ":please: *答完请随手给每道题来个“速评”*",
            "verbatim": False
        }
    },
    {
        "type": "actions",
        "block_id": "n8Zzc",
        "elements": [
            {
                "type": "button",
                "action_id": "question_answer_feedback_action.insight_1",
                "text": {
                    "type": "plain_text",
                    "text": ":+1:题目超赞！",
                    "emoji": True
                },
                "value": "{\"session_id\": \"589455451730\", \"feedback_id\": \"566780871264\", \"feedback_type\": \"insight\", \"feedback_value\": \"题目超赞\"}"
            },
            {
                "type": "button",
                "action_id": "question_answer_feedback_action.insight_2",
                "text": {
                    "type": "plain_text",
                    "text": ":+1:题目还行",
                    "emoji": True
                },
                "value": "{\"session_id\": \"589455451730\", \"feedback_id\": \"566780871264\", \"feedback_type\": \"insight\", \"feedback_value\": \"题目还行\"}"
            },
            {
                "type": "button",
                "action_id": "question_answer_feedback_action.insight_3",
                "text": {
                    "type": "plain_text",
                    "text": ":-1:题目待改进",
                    "emoji": True
                },
                "value": "{\"session_id\": \"589455451730\", \"feedback_id\": \"566780871264\", \"feedback_type\": \"insight\", \"feedback_value\": \"题目待改进\"}"
            }
        ]
    },
    {
        "type": "actions",
        "block_id": "gq6D+",
        "elements": [
            {
                "type": "button",
                "action_id": "question_answer_feedback_action.confidence_1",
                "text": {
                    "type": "plain_text",
                    "text": ":+1:认知超赞！",
                    "emoji": True
                },
                "value": "{\"session_id\": \"589455451730\", \"feedback_id\": \"566780871264\", \"feedback_type\": \"confidence\", \"feedback_value\": \"认知超赞！\"}"
            },
            {
                "type": "button",
                "action_id": "question_answer_feedback_action.confidence_2",
                "text": {
                    "type": "plain_text",
                    "text": ":+1:认知还行",
                    "emoji": True
                },
                "value": "{\"session_id\": \"589455451730\", \"feedback_id\": \"566780871264\", \"feedback_type\": \"confidence\", \"feedback_value\": \"认知还行\"}"
            },
            {
                "type": "button",
                "action_id": "question_answer_feedback_action.confidence_3",
                "text": {
                    "type": "plain_text",
                    "text": ":-1:认知待改进",
                    "emoji": True
                },
                "value": "{\"session_id\": \"589455451730\", \"feedback_id\": \"566780871264\", \"feedback_type\": \"confidence\", \"feedback_value\": \"认知待改进\"}"
            }
        ]
    }
]