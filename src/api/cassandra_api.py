from functools import cache

from fastapi import APIRouter

from tech.cassandra_query import search_id
from tech.s3_image import get_image_from_s3

cassandra = APIRouter()

@cache
@cassandra.get("/metadata_by_id/{id}")
async def metadata_by_id(id_pic: str):
    data =search_id(id_pic)
    answer = data + get_image_from_s3(data[0])
    return answer
