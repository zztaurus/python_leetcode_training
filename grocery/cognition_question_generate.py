import json
import requests
import pandas as pd


def question_bot(insight_type, insight):
    url = "https://dify.infastgear.com//v1/workflows/run"
    payload = json.dumps({
        "inputs": {
            "insight_type": insight_type,
            "insight": insight
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


def cognition_question_init():
    cache = []
    df = pd.read_csv('/Users/ning.zhou/Desktop/出题的认知 .csv')
    df = df[['cognitive_ai_analysis.origin_id', 'ai_text', 'category']]
    df = df.rename(columns={"cognitive_ai_analysis.origin_id": "cog_id"})
    res = df.to_dict('records')
    for i in range(3):
        for item in res:
            cog_id = item['cog_id']
            ai_text = item['ai_text']
            category = item['category']
            resp = question_bot(category, ai_text)
            print(resp)
            question = resp['question_text']
            answer = resp['answer']
            question_format = resp['question_format']
            qus_item = {
                "cog_id": cog_id,
                "question": question,
                "answer": answer,
                "tags": question_format,
                "type": 1
            }
            print(qus_item)
            cache.append(qus_item)
            print(" == " * 100)

    qus_df = pd.DataFrame(cache)
    print(qus_df.columns.tolist())
    qus_df.to_csv("/Users/ning.zhou/Desktop/cognitive_question.csv")


if __name__ == '__main__':
    cognition_question_init()
