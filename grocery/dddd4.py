以下是使用 ** 主用户（Master
User） ** 进行
Power
BI
嵌入的
Python
脚本示例，包含获取
`access_token`
和
`embed_token`
的完整流程：

---

### Python 脚本示例

```python
import requests
from msal import PublicClientApplication

# 配置参数 - 替换为实际值
CLIENT_ID = "your_client_id"  # Azure应用注册的客户端ID
USERNAME = "your_master_user@domain.com"  # Power BI主用户邮箱
PASSWORD = "your_master_user_password"  # Power BI主用户密码
TENANT_ID = "your_tenant_id"  # Azure租户ID
WORKSPACE_ID = "your_workspace_id"  # Power BI工作区ID
REPORT_ID = "your_report_id"  # Power BI报表ID

# API 配置
AUTHORITY_URL = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://analysis.windows.net/powerbi/api/.default"]
API_URL = "https://api.powerbi.com/v1.0/myorg/"


def get_access_token():
    """通过主用户凭据获取访问令牌 (ROPC Flow)"""
    app = PublicClientApplication(
        client_id=CLIENT_ID,
        authority=AUTHORITY_URL
    )

    result = app.acquire_token_by_username_password(
        username=USERNAME,
        password=PASSWORD,
        scopes=SCOPE
    )
    return result["access_token"]


def get_embed_token(access_token, workspace_id, report_id):
    """生成嵌入令牌"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    embed_url = f"{API_URL}groups/{workspace_id}/reports/{report_id}/GenerateToken"

    # 请求体配置
    body = {
        "accessLevel": "View",
        "allowSaveAs": False
        # 主用户模式下通常不需要显式指定数据集权限
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
```

---

### 关键配置说明

1. ** Azure
应用注册 **:
- `CLIENT_ID`: 在
Azure
门户注册的应用程序的客户端
ID。
- 不需要
`CLIENT_SECRET`，但需确保应用已启用 ** 公共客户端流 **（在应用注册的“身份验证”中启用）。

2. ** 主用户权限 **:
- 主用户需要是
Power
BI
工作区的管理员或拥有报表的访问权限。
- 确保主用户在
Power
BI
服务中有权访问报表和工作区。

3. ** API
权限配置 **:
- 在
Azure
应用注册中，添加以下 ** 委托权限 **：
- `Report.Read.All`（读取报表）
- `Dataset.Read.All`（读取数据集）
- 管理员需同意这些权限。

---

### 使用流程

1. ** 替换参数 **:
- 修改脚本中的
`CLIENT_ID`, `USERNAME`, `PASSWORD`, `TENANT_ID`, `WORKSPACE_ID`, `REPORT_ID`。

2. ** 安装依赖 **:
```bash
pip
install
msal
requests
```

3. ** 运行脚本 **:
```bash
python
powerbi_embed_master_user.py
```

---

### 注意事项

1. ** 安全性警告 **:
- 明文存储密码存在安全风险！生产环境中应使用 ** Azure
Key
Vault ** 或环境变量加密存储凭据。
- ROPC
流（用户名密码流）不推荐用于生产环境，建议优先使用服务主体或交互式登录。

2. ** 权限要求 **:
- 主用户需要是
Power
BI
Pro
或
Premium
许可证持有者。
- 在
Power
BI
管理门户启用 **“允许嵌入报表” ** 选项。

3. ** 错误处理 **:
- 如果主用户启用了
MFA（多因素认证），此脚本将失败。
- 检查网络是否能访问
`login.microsoftonline.com`
和
`api.powerbi.com`。

---

此示例展示了通过主用户直接认证的流程，适用于快速测试或内部工具场景。生产环境建议使用服务主体或更安全的认证方式。