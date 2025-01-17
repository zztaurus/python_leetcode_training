
import time
import requests

reportId="1c5f078e-6399-4278-b990-0d3c75450d9a"
table_name='campaign_daily_report'
field_name='platform'
value='android'
output_directory='/Users/ning.zhou/Desktop'
token =  "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InoxcnNZSEhKOS04bWdndDRIc1p1OEJLa0JQdyIsImtpZCI6InoxcnNZSEhKOS04bWdndDRIc1p1OEJLa0JQdyJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvYWE1ODIyZjUtODk4ZS00MzEwLTkyYmItNTY0ODg1MGJhMGUyLyIsImlhdCI6MTczNzAxOTM3NSwibmJmIjoxNzM3MDE5Mzc1LCJleHAiOjE3MzcwMjQyMzMsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84WkFBQUE3YjhlZVRHbE9OREhKNFpxclA2QUJyNzBDQzBNTmVUZlk3TUtpdGdjNnhmclcvVXo2NXQwR0gxNWdBcmZMUWhGQlpHcnY4SElRWVNoaVA4M1ZXSXNjZDN6NW5qZklxTXB4SUpuUXRkVER5Zz0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiMThmYmNhMTYtMjIyNC00NWY2LTg1YjAtZjdiZjJiMzliM2YzIiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJaaG91IiwiZ2l2ZW5fbmFtZSI6Ik5pbmciLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMDMuMTAwLjY0LjEyMiIsIm5hbWUiOiJOaW5nIFpob3UiLCJvaWQiOiJhZjZlNWNlMi1mNGE5LTQ3YTUtYjkwNS00OWFkYWUwYzc5Y2YiLCJwdWlkIjoiMTAwMzIwMDA3QzJBNzA2OSIsInJoIjoiMS5BVWtBOVNKWXFvNkpFRU9TdTFaSWhRdWc0Z2tBQUFBQUFBQUF3QUFBQUFBQUFBQW9BWE5KQUEuIiwic2NwIjoiQXBwLlJlYWQuQWxsIENhcGFjaXR5LlJlYWQuQWxsIENhcGFjaXR5LlJlYWRXcml0ZS5BbGwgQ29ubmVjdGlvbi5SZWFkLkFsbCBDb25uZWN0aW9uLlJlYWRXcml0ZS5BbGwgQ29udGVudC5DcmVhdGUgRGFzaGJvYXJkLlJlYWQuQWxsIERhc2hib2FyZC5SZWFkV3JpdGUuQWxsIERhdGFmbG93LlJlYWQuQWxsIERhdGFmbG93LlJlYWRXcml0ZS5BbGwgRGF0YXNldC5SZWFkLkFsbCBEYXRhc2V0LlJlYWRXcml0ZS5BbGwgR2F0ZXdheS5SZWFkLkFsbCBHYXRld2F5LlJlYWRXcml0ZS5BbGwgSXRlbS5FeGVjdXRlLkFsbCBJdGVtLkV4dGVybmFsRGF0YVNoYXJlLkFsbCBJdGVtLlJlYWRXcml0ZS5BbGwgSXRlbS5SZXNoYXJlLkFsbCBPbmVMYWtlLlJlYWQuQWxsIE9uZUxha2UuUmVhZFdyaXRlLkFsbCBQaXBlbGluZS5EZXBsb3kgUGlwZWxpbmUuUmVhZC5BbGwgUGlwZWxpbmUuUmVhZFdyaXRlLkFsbCBSZXBvcnQuUmVhZFdyaXRlLkFsbCBSZXBydC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkV3JpdGUuQWxsIFRlbmFudC5SZWFkLkFsbCBUZW5hbnQuUmVhZFdyaXRlLkFsbCBVc2VyU3RhdGUuUmVhZFdyaXRlLkFsbCBXb3Jrc3BhY2UuR2l0Q29tbWl0LkFsbCBXb3Jrc3BhY2UuR2l0VXBkYXRlLkFsbCBXb3Jrc3BhY2UuUmVhZC5BbGwgV29ya3NwYWNlLlJlYWRXcml0ZS5BbGwiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiIxTEFxck1wUGpaaHlBOGc5WkNQRHpXSzV1dVN4TjVDRnVjYl9vanI4RVFzIiwidGlkIjoiYWE1ODIyZjUtODk4ZS00MzEwLTkyYmItNTY0ODg1MGJhMGUyIiwidW5pcXVlX25hbWUiOiJuaW5nLnpob3VAZXdwLWdyb3VwLmNvbSIsInVwbiI6Im5pbmcuemhvdUBld3AtZ3JvdXAuY29tIiwidXRpIjoiR2ZSR1VPUFVXVVdSVkc5X1hYdGFBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19pZHJlbCI6IjEgMTQifQ.j6CY0Qu4ftw_eaeJBXAua4NFVqCuInG38_q1FP_DUsj2IKkW6NuknJAStuAHQTgOM31khzEktTNLBcAHt2W4mw9oRDmeflknAilF6mHaPGFvr5_sfSoTbQX42bJ59iYHIHgBTcOKesl12159EdACy-KdLhMGLJCzMWV9DQKJ5IqHtqMoib5-oSTXVx0dvcMmqVRLCV6zFoKaWqrdqBC58tvLTBXKCDER85duRXH3Ghp5UdYS3L_1lvD0weYqE-pOcOfyE6-Z3RPtF5VaSPOd4l3sAAA0Wr3AMcL9qauLRb2mzm3h4subBq4jW3T4NFfIOAAS6z5C_G60pGEWXJW6nA"


def export_powerbi_report():
    # Set up the authorization header
    headers = {
        "Authorization": f"Bearer {token}"
    }
    # Define the export request body
    body = {
        "format": "PDF",
        "powerBIReportConfiguration": {
            "reportLevelFilters": [
                {
                    "filter": f"{table_name}/{field_name} eq '{value}' and {table_name}/spend gt 1000"
                }
            ]
        }
    }

    # Send the export request
    url = f"https://api.powerbi.com/v1.0/myorg/reports/{reportId}/ExportTo"
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    exportId = response.json().get("id")
    if not exportId:
        raise Exception("Failed to get export ID")

    for i in range(10):
        # get export status
        url = f"https://api.powerbi.com/v1.0/myorg/reports/{reportId}/exports/{exportId}"
        response = requests.get(url, headers=headers)
        resp = response.json()
        print(resp)
        if resp['status'] == "Succeeded":
            break
        else:
            time.sleep(3)

    #download the file
    url = f"https://api.powerbi.com/v1.0/myorg/reports/{reportId}/exports/{exportId}/file"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    # Determine the file extension based on the content type
    content_type = response.headers.get('Content-Type', '')
    if 'application/zip' in content_type:
        file_extension = '.zip'
    elif 'application/pdf' in content_type:
        file_extension = '.pdf'
    elif 'image/' in content_type:
        file_extension = '.png'
    elif 'text/csv' in content_type:
        file_extension = '.csv'
    elif 'text/xml' in content_type:
        file_extension = '.xml'
    else:
        file_extension = '.dat'

    # Define the file path
    file_name = f"{output_directory}/exported_file{file_extension}"

    # Write the file to disk
    with open(file_name, 'wb') as file:
        file.write(response.content)

    print(f"File exported successfully to {file_name}")


if __name__ == '__main__':
    export_powerbi_report()