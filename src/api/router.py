from fastapi import APIRouter, UploadFile, File, HTTPException

from src.api.actions import insert_image
from src.models.requests import InsertRequest
import logging

main_router = APIRouter()

@main_router.post("/upload-image/")
async def upload_image():
    return