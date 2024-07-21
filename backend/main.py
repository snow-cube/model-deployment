from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import model_interface
import os


app = FastAPI()


@app.get('/')
async def root():
    return {'message': "Hello World"}


@app.post('/uploadfile')
async def upload_input_file(file: UploadFile):
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


@app.get("/downloadfile/{file_name}")
async def download_output_file(file_name: str):
    base_download_dir = './'
    output_path = os.path.join(base_download_dir, file_name)

    if not os.path.exists(output_path):
        return {
            'code': 0,
            'error': "File doesn't exists"
        }

    return FileResponse(path=output_path, filename=file_name)