
import requests
import json


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
def my_python_tool():
    url = "https://dify.infastgear.com//v1/workflows/run"
    payload = json.dumps({
        "inputs": {
            "insight_type": "后期健身",
            "insight": "【认知】针对老年人用户，脚本简洁话术简单，社会属性加强。"
        },
        "user": "zztaurus"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer app-5ad5xWrowd8OU4hSZdXxlOlh'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = response.json()
    resp = {}
    if result['data']['status'] == 'succeeded':
        outputs = result['data']['outputs']
        if 'result' in outputs:
            resp.update(json.loads(outputs['result']))
            outputs.pop('result')
        resp.update(outputs)

    return resp


if __name__ == '__main__':
    res = my_python_tool()
    print(res['question_text'])

