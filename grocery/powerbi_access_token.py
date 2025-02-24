import requests

def get_access_token(tenant_id, client_id, client_secret):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://analysis.windows.net/powerbi/api/.default"
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json().get("access_token")


def get_embed_token(access_token, report_id, group_id):
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/reports/{report_id}/GenerateToken"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "accessLevel": "View"  # 或者 "Edit" 根据需要
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json().get("token")



def job1(token):
    import requests
    def get_reports(token):
        url = "https://api.powerbi.com/v1.0/myorg/reports"
        url = "https://api.powerbi.com/v1.0/myorg/reports/ea3ee973-f102-460a-b510-e7e50afd49d1"

        url = "https://api.powerbi.com/v1.0/myorg/groups/a97b1994-25c6-4e95-829b-a830c991fa74/reports"
        # url = "https://api.powerbi.com/v1.0/myorg/groups/a97b1994-25c6-4e95-829b-a830c991fa74/reports/ea3ee973-f102-460a-b510-e7e50afd49d1"

        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)
        print(response.json())
        # response.raise_for_status()  # 检查请求是否成功
        return response

    # 使用示例
    resp = get_reports(token)
    print(resp)



if __name__ == "__main__":
    # 获取 access_token
    tenant_id = "your_tenant_id"
    client_id = "your_client_id"
    client_secret = "your_client_secret"
    token = get_access_token(tenant_id, client_id, client_secret)
    print(token)
    get_access_token()

    # 获取 embed_token
    access_token = "your_access_token"
    report_id = "your_report_id"
    group_id = "your_group_id"
    embed_token = get_embed_token(access_token, report_id, group_id)
    print(embed_token)





