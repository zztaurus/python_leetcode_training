
import requests
from msal import ConfidentialClientApplication

# 配置参数 - 需要替换为您的实际值
CLIENT_ID = "your_client_id"          # Azure应用注册的客户端ID
CLIENT_SECRET = "your_client_secret"  # Azure应用注册的客户端机密
TENANT_ID = "your_tenant_id"          # Azure租户ID
WORKSPACE_ID = "your_workspace_id"    # Power BI工作区ID
REPORT_ID = "your_report_id"          # Power BI报表ID
AUTHORITY_URL = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://analysis.windows.net/powerbi/api/.default"]
API_URL = "https://api.powerbi.com/v1.0/myorg/"

def get_access_token():
    """使用MSAL获取访问令牌"""
    app = ConfidentialClientApplication(
        client_id=CLIENT_ID,
        client_credential=CLIENT_SECRET,
        authority=AUTHORITY_URL
    )

    result = app.acquire_token_for_client(scopes=SCOPE)
    return result["access_token"]

def get_embed_token(access_token, workspace_id, report_id):
    """生成嵌入令牌"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    embed_url = f"{API_URL}groups/{workspace_id}/reports/{report_id}/GenerateToken"

    # 请求体参数配置
    body = {
        "accessLevel": "View",
        "allowSaveAs": False,
        "identities": [{
            "reports": [report_id],
            "datasets": ["your_dataset_id"]  # 替换为实际数据集ID
        }]
    }

    response = requests.post(embed_url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()["token"]

def generate_embed_url(workspace_id, report_id, embed_token):
    """生成嵌入URL"""
    return f"https://app.powerbi.com/reportEmbed?reportId={report_id}&groupId={workspace_id}&config=embed%3Dtrue%26accessToken={embed_token}"

# 主流程
if __name__ == "__main__":
    try:
        # 步骤1：获取访问令牌
        access_token = get_access_token()
        print("Access token acquired successfully")

        # 步骤2：生成嵌入令牌
        embed_token = get_embed_token(access_token, WORKSPACE_ID, REPORT_ID)
        print("Embed token generated successfully")

        # 步骤3：生成嵌入URL
        embed_url = generate_embed_url(WORKSPACE_ID, REPORT_ID, embed_token)
        print(f"Embed URL:\n{embed_url}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

