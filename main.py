from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import FileResponse
import os
import mimetypes

app = FastAPI()

IMAGES_DIR = "images"

@app.post("/image")
async def get_image(body: dict = Body(...)):
    image_name = body.get("image_name")
    image_path = os.path.join(IMAGES_DIR, image_name)

    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")

    file_type, _ = mimetypes.guess_type(image_path)

    if file_type is None:
        raise HTTPException(status_code=415, detail="Unsupported file type")

    return FileResponse(image_path, media_type=file_type)
