from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse
import model_interface
import os
from fastapi.middleware.cors import CORSMiddleware
import uuid
import random

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


def random_str(num=6):
    uln = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    rs = random.sample(uln, num)  # 生成一个指定位数的随机字符串
    a = uuid.uuid1()  # 根据时间戳生成 uuid, 保证全球唯一
    b = ''.join(rs + str(a).split("-"))  # 生成将随机字符串与 uuid 拼接
    return b  # 返回随机字符串


@app.get('/')
async def root():
    return {'message': "Hello World"}


@app.post('/upload')
async def upload_input_file(file: UploadFile, token: str = Form()):
    task_id = random_str()
    input_file_name = f'{task_id}.npz'
    img_name = f'{task_id}.png'
    base_save_dir = './input/'
    input_file_path = os.path.join(base_save_dir, input_file_name)
    save_dir = './output/'

    content = await file.read()
    with open(input_file_path, 'wb') as f:
        f.write(content)
    model_interface.inference(input_file_path, save_dir, save_dir)
    return {
        'filename': input_file_name,
        'imgname': img_name
    }


@app.get("/download")
async def download_output_file(filename: str):
    base_download_dir = './output/'
    output_path = os.path.join(base_download_dir, filename)

    if not os.path.exists(output_path):
        return {
            'code': 0,
            'error': "File doesn't exists"
        }

    return FileResponse(path=output_path, filename=filename)