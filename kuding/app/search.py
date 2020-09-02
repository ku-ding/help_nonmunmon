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

    es.index(index = "dictionary-user", body = doc)


def searchDataContent(title, content):
    es = Elasticsearch()
    body = {           
        "query": {
		    "bool": {
		        "should": [{ "match": { "content" : content} }], 
                "must": [{ "match": {"title": title} }]
		    }
	    },
	    "_source": {
		    "includes": ["title", "content", "category", "image", "url", "who"]
	    }
    }

    return es.search(index="dictionary-*", body=body)

def searchDataCategory(title, category):
    es = Elasticsearch()
    body = {           
        "query": {
		    "bool": {
		        "filter": [{ "match": { "category" : category} }], 
                "must": [{ "match": {"title": title} }]
		    }
	    },
	    "_source": {
		    "includes": ["title", "content", "category", "image", "url", "who"]
	    }
    }

    return es.search(index="dictionary-*", body=body)

def searchDataWho(title, who):
    es = Elasticsearch()
    body = {           
        "query": {
		    "bool": {
		        "filter": [{ "match": { "who" : who} }], 
                "must": [{ "match": {"title": title} }]
		    }
	    },
	    "_source": {
		    "includes": ["title", "content", "category", "image", "url", "who"]
	    }
    }

    return es.search(index="dictionary-*", body=body)