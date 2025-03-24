
import json
import requests
# Azure AD and Power BI configuration
TENANT_ID = 'aa5822f5-898e-4310-92bb-5648850ba0e2'
CLIENT_ID = 'a367d484-d042-433a-acee-cf3f577eded2'
CLIENT_SECRET = 'BXwR.LtAjImWm72nFWx3_~qYpfikg~-R7c'
WORKSPACE_ID = 'your-workspace-id'
DATASET_ID = '3d964d99-10d0-406e-af6f-ef7ad048effe'
REPORT_ID = '8b7b0cb3-7325-4fad-96e5-444ae7a4399f'

# OAuth2.0 token endpoint
TOKEN_ENDPOINT = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'

# Power BI REST API endpoint for generating embed token
POWER_BI_API_ENDPOINT = 'https://api.powerbi.com/v1.0/myorg/GenerateToken'

def get_access_token():
    # Request payload for OAuth2.0 token
    payload = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://analysis.windows.net/powerbi/api/.default'
    }

    # Request access token
    response = requests.post(TOKEN_ENDPOINT, data=payload)
    response.raise_for_status()
    return response.json().get('access_token')

def get_report(access_token, report_id):
    url = f"https://api.powerbi.com/v1.0/myorg/reports/{report_id}"

    # Bearer token for authorization

    # Set up the headers
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    resp = json.loads(response.json())
    embedUrl = resp['embedUrl']
    datasetId = resp['datasetId']

    return embedUrl, datasetId


def generate_embed_token(access_token):
    # Request headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Request payload for generating embed token
    payload = {
        "datasets": [
            {
                "id": {DATASET_ID}
            }
        ],
        "reports": [
            {
                "allowEdit": True,
                "id": {REPORT_ID}
            }
        ]
    }

    # Generate embed token
    response = requests.post(POWER_BI_API_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()
    return response.json().get('token')

def main():
    access_token = get_access_token()
    print(access_token)
    embed_token = generate_embed_token(access_token)
    print(f'Embed Token: {embed_token}')

if __name__ == '__main__':
    main()

