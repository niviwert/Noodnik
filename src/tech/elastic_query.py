from elasticsearch import Elasticsearch, AuthenticationException

CA_CERT_PATH = "/home/mtmn15/http_ca.crt"
enrolment_token = 'eyJ2ZXIiOiI4LjE0LjAiLCJhZHIiOlsiMTcyLjIwLjAuMjo5MjAwIl0sImZnciI6IjZkZjA0NWRkNjgzMjk0NmU0YWE3NjVmNzJmZDgwNGI1ODI4ODFjMjEzZGFiZGU0ZjU4NmJhMDhhYzZiZjI2ODEiLCJrZXkiOiJWRUpFOXB3QlZ3NjBPaVVQTlJENDpIRnJ4TTdKNWVzMXBHMFg0NDdjaFhBIn0='
es = Elasticsearch(
    "https://localhost:9200",
    # api_key="ZmFBUjhwd0JHNW9pWWxIaS1lTUQ6VnROSlpHaTEyN29YQUwxbUM0QzVxZw==",
    verify_certs=False,
    ca_certs=CA_CERT_PATH,
    basic_auth=('elastic', 'V2zL1ApSGEuss24*pP6='),
)


def query_match(field: str, value: str):
    res = es.search(index='md',
                    query={
                        'match': {
                            field: value
                        }
                    }
                    )
    print("hi")
    hits = res['hits']['hits']
    for hit in hits:
        print(f"Score: {hit['_score']}, Source: {hit['_source']}")
    return res


def query_range(field: str, gte, lte):
    res = es.search(index='md',
                    query={
                        "range": {
                            field: {
                                "gte": gte,
                                "lte": lte
                            }
                        }
                    }
                    )
    hits = res['hits']['hits']
    for hit in hits:
        print(f"Score: {hit['_score']}, Source: {hit['_source']}")
    return res


def query_geo_poligon(filed: str, lon1, lat1, lon2, lat2):
    res = es.search(index='md',
                    query={
                        "geo_polygon": {
                            filed: {
                                "points": [
                                    {
                                        "lat": lat1,
                                        "lon": lon1
                                    },
                                    {
                                        "lat": lat2,
                                        "lon": lon2
                                    }
                                ]
                            }
                        }
                    })
    hits = res['hits']['hits']
    for hit in hits:
        print(f"Score: {hit['_score']}, Source: {hit['_source']}")
    return res

