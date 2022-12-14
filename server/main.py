#  загрузка переменных окружения
import lesson_env 

# модуль логгирования
from lesson_lib import logger

# модуль распознавания
from lesson_lib.predict_number import predict_number

# загрузка библиотек сервера
from fastapi import FastAPI, File
from fastapi.responses import Response
from requests_toolbelt import MultipartEncoder

log = logger.get(__name__)

app = FastAPI()

@app.post("/predict",
    # Prevent FastAPI from adding "application/json" as an additional
    # response media type in the autogenerated OpenAPI specification.
    # https://github.com/tiangolo/fastapi/issues/3258
    response_class=Response,
)
async def create_file(file: bytes = File(...)):

    # предсказание
    result = predict_number(file)

    print('test api message')

    # подготовка ответа, содержащего:
    # - предсказанную цифру
    # - вероятность предсказания
    # - обработанное изображение, на основе которого было сделано предсказание
    log.debug(f'Перед MultipartEncoder')
    m = MultipartEncoder(
        fields={
            'number': str(result['number']),
            'probability': str(result['probability']), 
            'image': ('image.jpg', result['image'], 'image/jpeg')}
        )
    log.debug(f'content_type: {m.content_type}')
    return Response(m.to_string(), media_type=m.content_type)

@app.get("/test")
def read_root():
    return {"Hello": "World"}    
