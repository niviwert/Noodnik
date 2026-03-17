import uvicorn
from fastapi import FastAPI
import logging

from api.cassandra_api import cassandra
from src.api.router import main_router

app = FastAPI()
app.include_router(main_router)
app.include_router(cassandra)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    logging.log(20,"listening...")
