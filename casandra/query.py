
from cassandra.cluster import Cluster
import logging
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
logging.info("connected to Cassandra")
session.execute("""
CREATE KEYSPACE IF NOT EXISTS funny
WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 }
""")
logging.info("have keyspace")
session.set_keyspace('funny')
logging.info("connected to keyspace")
session.execute(""" CREATE INDEX IF NOT EXISTS ON funny.pic (ENTRIES(object_details));  """)
session.execute(""" CREATE INDEX IF NOT EXISTS ON funny.pic (ENTRIES(location));  """)
session.execute(""" CREATE INDEX IF NOT EXISTS ON funny.pic (ENTRIES(digital_capture));  """)



id_search = session.prepare(""" SELECT * FROM funny.pic WHERE asset_id = ? """)
object_details_search = session.prepare(""" SELECT * FROM funny.pic WHERE object_details[?] = ? """)
location_search = session.prepare(""" SELECT * FROM funny.pic WHERE location[?] = ? """)
digital_capture_search = session.prepare(""" SELECT * FROM funny.pic WHERE digital_capture[?] = ? """)

def search_id(id_find:str):
    bound = id_search.bind([id_find])
    bonded = session.execute(bound)
    result = []
    for row in bonded:
        result.append({'asset_id': row.asset_id,
                       'digital_capture': row.digital_capture,
                       'location': row.location,
                       'object_details': row.object_details, })
    return result


def object_detail_search(ditail:str, value:str):
    bound = object_details_search.bind([ditail, value])
    bonded = session.execute(bound)
    result = []
    for row in bonded:
        result.append({'asset_id': row.asset_id,
                       'digital_capture': row.digital_capture,
                       'location': row.location,
                       'object_details': row.object_details, })
    return result


def locations_search(location:str, value:str):
    bound = location_search.bind([location, value])
    bonded = session.execute(bound)
    result = []
    for row in bonded:
        result.append({'asset_id': row.asset_id,
                       'digital_capture': row.digital_capture,
                       'location': row.location,
                       'object_details': row.object_details, })
    return result


def digital_captures_search(digital_capture:str, value:str):
    bound = digital_capture_search.bind([digital_capture, value])
    bonded = session.execute(bound)
    result = []
    for row in bonded:
        result.append({'asset_id': row.asset_id,
                       'digital_capture': row.digital_capture,
                       'location': row.location,
                       'object_details': row.object_details, })
    return result
