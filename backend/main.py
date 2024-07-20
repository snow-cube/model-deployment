# from typing import Optional
# from sympy import content
# import uvicorn

from fastapi import FastAPI, File, UploadFile
# from io import BytesIO
# from ml.predict import load_model,Features,predict

#创建FastAPI实例
app = FastAPI()

#创建访问路径
@app.get('/')
def read_root():
    return {'message': 'Hello World'}

# # 加载模型
# models = load_model()
# def test(file):
# 	feature = Features(file)
# 	return model.predict(feature)

#调用模型接口
@app.post('/detect/v2')
async def detect2(file: UploadFile):
    f = file.file
    # content = await file.read()
    # res = test(content)
    return {
        'filename': file.filename,
        'attributes': str(type(f))
        # 'result': res
    }
