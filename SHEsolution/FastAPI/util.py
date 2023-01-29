import torch
from PIL import Image
import io

def get_yolov5():
    model = torch.hub.load('./yolov5', 'custom', path='./model/best.pt', source='local')
    model.conf = 0.5
    return model

def get_image_from_bytes(binary_image):
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
    width, height = input_image.size
    resized_image = input_image.resize((640, 640))

    return resized_image