from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse
import model_interface
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {'message': "Hello World"}


@app.post('/upload')
async def upload_input_file(file: UploadFile, token: str = Form()):
    input_file_name = 'test.npz'
    base_save_dir = './'
    input_file_path = os.path.join(base_save_dir, input_file_name)
    save_dir = './'

    content = await file.read()
    with open(input_file_path, 'wb') as f:
        f.write(content)
    model_interface.inference(input_file_path, save_dir, save_dir)
    return {
        'filename': input_file_name
    }


@app.get("/download")
async def download_output_file(filename: str):
    base_download_dir = './'
    output_path = os.path.join(base_download_dir, filename)

    if not os.path.exists(output_path):
        return {
            'code': 0,
            'error': "File doesn't exists"
        }

    return FileResponse(path=output_path, filename=filename)