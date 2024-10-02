
from fastapi import FastAPI
import uvicorn
import os
import json
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response

from src.finetune_bert_model_question_answer.pipeline.prediction import PredictionPipeline

app = FastAPI()

@app.get('/', tags = ['authentication'])

async def index():
    return RedirectResponse(url = '/docs')


@app.get('/train')
async def train():
    try:
        os.system('main.py')
        return {'message': 'Training completed'}
    except Exception as e:
        return Response(f'Error Occured ! {e}')


@app.get('/predict')
async def predict(question):

    try:
        obj = PredictionPipeline()
        result = obj.predict(question)
        return result
    except Exception as e:
        return Response(f'error :: {e}')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)