from fastapi import FastAPI, File
from util import get_yolov5, get_image_from_bytes
from starlette.responses import Response
import io
from PIL import Image
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

model = get_yolov5()
'''
# Cross-Origin Resource Sharing (CORS)
HTTP 헤더를 통해 한 Origin에서 실행 중인 웹 어플리케이션이 다른 Origin의 리소스에 접근할 수 있도록 브라우저에 권한을 부여하는 정책
'''
origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://docs.ultralytics.com/tutorials/pytorch-hub/ 참조

@app.post("/object-to-image")
async def detect_return_image(file: bytes = File(...)):
    input_image = get_image_from_bytes(file)
    results = model(input_image)    # inference
    results.ims  # array of original images (as np array) passed to model for inference
    results.render()    # updates results.ims with boxes and labels
    for im in results.ims:
        buffered = io.BytesIO()
        im_base64 = Image.fromarray(im)
        im_base64.save(buffered, format="jpeg")

    return Response(content=buffered.getvalue(), media_type="image/jpeg")


@app.post("/object-to-json")
async def detect_return_json(file: bytes = File(...)):
    input_image = get_image_from_bytes(file)
    results = model(input_image)

    json_res = results.pandas().xyxy[0].to_json(orient="records")
    json_res = json.loads(json_res)

    return {"result": json_res}

'''
    1. Yolov5 Inference Sample Example
    results.pandas().xyxy[0]
    #      xmin    ymin    xmax   ymax  confidence  class    name
    # 0  749.50   43.50  1148.0  704.5    0.874023      0  person
    # 1  433.50  433.50   517.5  714.5    0.687988     27     tie
    # 2  114.75  195.75  1095.0  708.0    0.624512      0  person
    # 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
    
    2. Convert Dataframe to JSON
    Encoding/decoding a Dataframe using 'records' formatted JSON. 
    [
        {
            "col 1": "a",
            "col 2": "b"
        },
        {
             "col 1": "c",
            "col 2": "d"
        }
    ]
'''