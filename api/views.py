from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .config import CLIENT_ID, CLIENT_SECRET

# Biến toán cục
client_id = CLIENT_ID
client_secret = CLIENT_SECRET


# Create your views here.
@api_view(['POST'])
def age(request):
    # Kiểm tra xem file có được tải lên không
    if 'image' not in request.FILES:
        return Response({"error": "No image file provided."}, status=400)

    image = request.FILES['image']

    try:
        # Gửi file ảnh trong yêu cầu POST
        files = {'data': image.read()}
        quality = requests.post('https://api.everypixel.com/v1/faces', files=files,
                                auth=(client_id, client_secret)).json()
        return Response(quality)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=400)


@api_view(['GET'])
def get_age(request):
    image_path = 'D:/test.jpg'

    try:
        # Gửi file ảnh trong yêu cầu POST
        with open(image_path, 'rb') as image:
            data = {'data': image}
            quality = requests.post('https://api.everypixel.com/v1/faces', files=data,
                                    auth=(client_id, client_secret)).json()
        return Response(quality)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=400)


@api_view(['GET'])
def sample_data(request):
    data = {
        "faces": [
            {
                "bbox": [498.8294668128431, 310.14473464167986, 679.9473669843536, 585.3291222675277],
                "score": 0.9999926090240479,
                "age": 69.0,
                "class": "Age - Senior Adult"
            },
            {
                "bbox": [673.2380907601397, 419.22049272243726, 856.7915110646504, 630.1551627844635],
                "score": 0.9999024868011475,
                "age": 60.0,
                "class": "Age - Senior Adult"
            }
        ],
        "status": "ok"
    }
    return Response(data)


@api_view(['POST'])
def quality_ugc(request):
    # Kiểm tra xem file có được tải lên không
    if 'image' not in request.FILES:
        return Response({"error": "No image file provided."}, status=400)

    image = request.FILES['image']

    try:
        # Gửi file ảnh trong yêu cầu POST
        data = {'data': image.read()}
        quality = requests.post('https://api.everypixel.com/v1/quality_ugc', files=data, auth=(client_id, client_secret)).json()
        return Response(quality)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=400)


@api_view(['GET'])
def get_quality_ugc(request):
    image_path = 'D:/test.jpg'

    try:
        # Gửi file ảnh trong yêu cầu POST
        with open(image_path, 'rb') as image:
            data = {'data': image}
            quality = requests.post('https://api.everypixel.com/v1/quality_ugc', files=data, auth=(client_id, client_secret)).json()
        return Response(quality)
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=400)



