from elasticsearch import Elasticsearch
from datetime import datetime

#User can input custum dictionary
def insertData(title, content, url, image, category, who):
    es = Elasticsearch()

    doc = {
        "title": title,
        "contenct": content,
        "imgae": image,
        "url": url,
        "category": category,
        "who": who,
        "@timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }

    es.index(index = "dictionary-test", body = doc)


def searchData(size, who):
    es = Elasticsearch()

    body = {
        "size": size,
        "query": {
            "match": {
                "who": who
            }
        }
    }

    return es.search(index="*", body=body)

#insertData("제목", "내용", "URL", "이미지", "computer", "hazzi")
res = searchData(1,"hazzi")
print(res)


