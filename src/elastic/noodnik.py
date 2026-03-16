import os
from elasticsearch import Elasticsearch, AuthenticationException

CA_CERT_PATH = "/home/mtmn15/http_ca.crt"
es = Elasticsearch(
    "https://localhost:9200",
    # api_key="ZmFBUjhwd0JHNW9pWWxIaS1lTUQ6VnROSlpHaTEyN29YQUwxbUM0QzVxZw==",
    verify_certs=False,
    ca_certs=CA_CERT_PATH,
    basic_auth=('elastic', 'tTbf=KETa_reglC3*LnJ'),
)
def query_match(field: str, value: str):
    res = es.search(index='noodnik',
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

def main():
    meta_data: dict = {
        "asset_id": "550e8400-e29b-41d4-a716-446655440067",
        "asset_type": "Artistic Photograph",
        "object_details": {
            "title": "Urban Solitude",
            "artist": "Elena Rossi",
        },
        "capture_gps": {
            "type": "Sensor Location (Point)",
            "latitude": 48.8640,
            "longitude": 2.3250
        },
        "digital_capture":
            {
                "photographer": "Elena Rossi"
            }
    }
    print(query_match('asset_type', meta_data['asset_type']))
    #resp = es.search(
    #    index="metadata",
    #    from_=40,
    #    size=20,
    #    query={
    #        "term": {
    #            "asset_type": "Artistic Photograph"
    #        }
    #    },
    #)
    #print(resp)


if __name__ == "__main__":
    main()