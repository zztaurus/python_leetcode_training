import json
from os import fdopen
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor



def  workflow_info():
    api_key = 'app-PKQuqTmCyQBHNi1Ce6YIuhox'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    host = "https://api-dify-pro.infastgear.com/v1/parameters"
    res = requests.request("GET", host, headers=headers)
    print(res.json())

def generate_question(insight, insight_type):
    host = "https://api-dify-pro.infastgear.com/v1/workflows/run"
    api_key = 'app-PKQuqTmCyQBHNi1Ce6YIuhox'
    payload = json.dumps({
        "inputs": {
            "insight_type": insight_type,
            "insight": insight
        },
        "user": "cognition_question"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    print("=" * 100)
    print(payload)
    response = requests.request("POST", host, headers=headers, data=payload)
    res = response.json()
    print(res)
    print("+" * 100)
    question_text_str = res['data']['outputs']['question_text']
    question = json.loads(question_text_str)
    answer = res['data']['outputs']['answer']
    print(question, type(question))
    return json.dumps(question), answer


def job1():
    fs = []
    df = pd.read_csv('/Users/ning.zhou/Desktop/question.csv')
    rows = df.to_dict(orient='records')
    for item in rows:
        insight = item['text']
        insight_type = item['tags']
        questinfo, answer = generate_question(insight, insight_type)
        item['question'] = questinfo
        item['answer'] = answer
        fs.append(item)

    df = pd.DataFrame(fs)
    df.to_csv('/Users/ning.zhou/Desktop/cognition_question_2.csv', index=False)

def job2():
    fs = []
    df = pd.read_csv('/Users/ning.zhou/Desktop/insight.csv')
    df = df.rename(columns={
        'cognitive_ai_analysis.origin_id': 'cognition_id',
        'ai_text': 'text',
        'category': 'tags'})
    rows = df.to_dict(orient='records')
    for item in rows:
        insight = item['text']
        insight_type = item['tags']
        questinfo, answer = generate_question(insight, insight_type)
        item['question'] = questinfo
        item['answer'] = answer
        fs.append(item)

    df = pd.DataFrame(fs)
    df.to_csv('/Users/ning.zhou/Desktop/cognition_question_2.csv', index=False)

def process_item(item):
    insight = item['text']
    insight_type = item['tags']
    questinfo, answer = generate_question(insight, insight_type)
    item['question'] = questinfo
    item['answer'] = answer
    return item

def job3():
    df = pd.read_csv('/Users/ning.zhou/Desktop/ai_question.csv')
    rows = df.to_dict(orient='records')

    with ThreadPoolExecutor(max_workers=10) as executor:
        fs = list(executor.map(process_item, rows))

    df = pd.DataFrame(fs)
    df.to_csv('/Users/ning.zhou/Desktop/cognition_question_2.csv', index=False)


if __name__ == '__main__':
    job3()


