import time
from brave_search import brave_search


def search_web(queries, count=5):
    results = {}
    for query in queries:
        time.sleep(1)
        results[query] = brave_search(query, count=count)

    final_results = {}
    for key, value in results.items():
        final_results[key] = []
        for res in value:
            url = res["url"]
            title = res["title"]
            final_results[key].append({"url": url, "title": title})
    return final_results
