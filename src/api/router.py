from fastapi import APIRouter, UploadFile, File, HTTPException

import logging

main_router = APIRouter()

@main_router.post("/upload-image/")
async def upload_image():
    return