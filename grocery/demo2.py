

import os
import json
import pandas as pd
service_endpoint = 'https://gptkb-thprcst5cpep2.search.windows.net'
index_name = 'cogs_full_info_test'
key = 'oB8UrCegoPQio10kre5lNw1wrFmsJ8tm7Zu6SyQBuhAzSeBTU4H7'

def simple_text_query(creator, keyword, page=1, page_size=15):
    # [START simple_query]
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient

    search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))


    permissions_filter = f"search.ismatch('\"{creator}\"', 'email')"

    results = search_client.search(search_text="混剪", search_mode='all', query_type='simple', include_total_count=True, filter=permissions_filter)
    for res in results:
        print(res)

    counts = 0
    final_data = []

    creator = creator
    keywords = keyword
    permissions_filter = ''
    if creator:
        if permissions_filter:
            permissions_filter += (f" and search.ismatch('\"{creator}\"', 'email')")
        else:
            permissions_filter += (f"search.ismatch('\"{creator}\"', 'email')")

    if permissions_filter:
        results = search_client.search(
            search_text=f"{keywords}", search_mode='all', query_type='simple', include_total_count=True,
            filter=permissions_filter)
    else:
        results = search_client.search(
            search_text=f"{keywords}", search_mode='all', query_type='simple', include_total_count=True)
    counts += results.get_count()

    if not keywords:
        results = search_client.search(search_text="*", search_mode='all', query_type='simple',
                                            include_total_count=True, filter=permissions_filter, top=page_size,
                                            skip=(page - 1) * page_size)
        final_data = [result for result in results]
    else:
        results = search_client.search(search_text=f"\"{keywords}\"", search_mode='all', query_type='simple',
                                            filter=permissions_filter, top=page_size, skip=(page - 1) * page_size)
        print(results)
        final_data = [result for result in results]
    df = pd.DataFrame(final_data)
    print(df)
    df = df[['cogId', 'email_name', 'origin_time', 'importance_score', 'reliability', 'ai_text', 'content']]
    df['content'] = df['content'].apply(lambda x: json.loads(x) if x else None)
    print(counts)
    print(df.to_dict(orient='records'))


if __name__ == '__main__':
    simple_text_query("shuai.liu@rdc-west.com", "混剪")

