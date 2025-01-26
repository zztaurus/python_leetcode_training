
import time
import requests

reportId="ea3ee973-f102-460a-b510-e7e50afd49d1"
table_name='campaign_daily_report'
field_name='platform'
value='android'
min_spend = 1000
output_directory='/Users/ning.zhou/Desktop'
token =  "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyIsImtpZCI6IllUY2VPNUlKeXlxUjZqekRTNWlBYnBlNDJKdyJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvYWE1ODIyZjUtODk4ZS00MzEwLTkyYmItNTY0ODg1MGJhMGUyLyIsImlhdCI6MTczNzcwNjIxMywibmJmIjoxNzM3NzA2MjEzLCJleHAiOjE3Mzc3MTEzODIsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84WkFBQUFqNDRZZml1U2x5WFVsZzV3aFVyTUtlbGxnNUw5YTJYd0ttckFZZnM0elZqZEwvSUI4Y2YzOEVzZkcyeUlnZSsvSStXaXhOYWk5bVAzcHN0V2MrQXRVY3RVRDhsQzU2eHFqMDBPL3lpU0NnZz0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiMThmYmNhMTYtMjIyNC00NWY2LTg1YjAtZjdiZjJiMzliM2YzIiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJaaG91IiwiZ2l2ZW5fbmFtZSI6Ik5pbmciLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMDMuMTAwLjY0LjEyMiIsIm5hbWUiOiJOaW5nIFpob3UiLCJvaWQiOiJhZjZlNWNlMi1mNGE5LTQ3YTUtYjkwNS00OWFkYWUwYzc5Y2YiLCJwdWlkIjoiMTAwMzIwMDA3QzJBNzA2OSIsInJoIjoiMS5BVWtBOVNKWXFvNkpFRU9TdTFaSWhRdWc0Z2tBQUFBQUFBQUF3QUFBQUFBQUFBQW9BWE5KQUEuIiwic2NwIjoiQXBwLlJlYWQuQWxsIENhcGFjaXR5LlJlYWQuQWxsIENhcGFjaXR5LlJlYWRXcml0ZS5BbGwgQ29ubmVjdGlvbi5SZWFkLkFsbCBDb25uZWN0aW9uLlJlYWRXcml0ZS5BbGwgQ29udGVudC5DcmVhdGUgRGFzaGJvYXJkLlJlYWQuQWxsIERhc2hib2FyZC5SZWFkV3JpdGUuQWxsIERhdGFmbG93LlJlYWQuQWxsIERhdGFmbG93LlJlYWRXcml0ZS5BbGwgRGF0YXNldC5SZWFkLkFsbCBEYXRhc2V0LlJlYWRXcml0ZS5BbGwgR2F0ZXdheS5SZWFkLkFsbCBHYXRld2F5LlJlYWRXcml0ZS5BbGwgSXRlbS5FeGVjdXRlLkFsbCBJdGVtLkV4dGVybmFsRGF0YVNoYXJlLkFsbCBJdGVtLlJlYWRXcml0ZS5BbGwgSXRlbS5SZXNoYXJlLkFsbCBPbmVMYWtlLlJlYWQuQWxsIE9uZUxha2UuUmVhZFdyaXRlLkFsbCBQaXBlbGluZS5EZXBsb3kgUGlwZWxpbmUuUmVhZC5BbGwgUGlwZWxpbmUuUmVhZFdyaXRlLkFsbCBSZXBvcnQuUmVhZFdyaXRlLkFsbCBSZXBydC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkLkFsbCBTdG9yYWdlQWNjb3VudC5SZWFkV3JpdGUuQWxsIFRlbmFudC5SZWFkLkFsbCBUZW5hbnQuUmVhZFdyaXRlLkFsbCBVc2VyU3RhdGUuUmVhZFdyaXRlLkFsbCBXb3Jrc3BhY2UuR2l0Q29tbWl0LkFsbCBXb3Jrc3BhY2UuR2l0VXBkYXRlLkFsbCBXb3Jrc3BhY2UuUmVhZC5BbGwgV29ya3NwYWNlLlJlYWRXcml0ZS5BbGwiLCJzaWQiOiJkNDQ0ZThhNy05ZDI4LTRhOGUtYjk3ZC1hZmY1ZjdmMWRlNjEiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiIxTEFxck1wUGpaaHlBOGc5WkNQRHpXSzV1dVN4TjVDRnVjYl9vanI4RVFzIiwidGlkIjoiYWE1ODIyZjUtODk4ZS00MzEwLTkyYmItNTY0ODg1MGJhMGUyIiwidW5pcXVlX25hbWUiOiJuaW5nLnpob3VAZXdwLWdyb3VwLmNvbSIsInVwbiI6Im5pbmcuemhvdUBld3AtZ3JvdXAuY29tIiwidXRpIjoiQks2Ynl3b3poMFNMRW11TC1YY0JBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19pZHJlbCI6IjEgMjYifQ.NTvRNUJh39pyVEIiD3lGdgdOxFRo0XZcr9_iY8w6nyTlNktRAP2Iz9iNvNq_jGST3Fu75cahjBmyUN_rYWJv-avvxXc8FYw9Wns1iR39qYZTTVfadobrehnJ3GEB3TfqJwOkfOi78quMQ7kob1LBkvwNtDW0M6gapzeO2mDq9LHRdz_Vrh2kZrFCOsqy0anlMTcPQhfid_-bNt7QaovC6wO91mVDgHP9TczJ1JFekTztImmfWFeO5wpidMen401FGFMBJXkwUtClW-xQuOHa-LpY-CTl0-8wEHnAVL2juse5EevhGj0HIKm31J-S6s2ZB-ohfEIU0KBlEUlAO3f69g"

def export_powerbi_report():
    # Set up the authorization header
    headers = {
        "Authorization": f"Bearer {token}"
    }
    # Define the export request body
    # body = {
    #     "format": "PDF",
    #     "powerBIReportConfiguration": {
    #         "reportLevelFilters": [
    #             {
    #                 "filter": f"{table_name}/{field_name} eq '{value}' and {table_name}/spend gt {min_spend}"
    #             }
    #         ]
    #     }
    # }

    body = {
        "format": "PNG",
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
    file_name = f"{output_directory}/powerbi{file_extension}"

    # Write the file to disk
    with open(file_name, 'wb') as file:
        file.write(response.content)

    print(f"File exported successfully to {file_name}")


if __name__ == '__main__':
    export_powerbi_report()