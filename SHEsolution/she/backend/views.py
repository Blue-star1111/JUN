from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
import requests
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.decorators import api_view, renderer_classes 
from rest_framework.renderers import JSONRenderer
from .serializer import  TypeSerializer, CheckListSerializer, ImageDetectSerializer
from .models import Type, CheckList, ImageDetect
from django.conf import settings

# Create your views here.

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class CheckListViewSet(viewsets.ModelViewSet):
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer

class ImageDetectViewset(viewsets.ModelViewSet):
    print('image1')
    queryset = ImageDetect.objects.all()
    print('image2')
    serializer_class = ImageDetectSerializer

# class SendImage(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         serializer = ImageDetectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             file_path = settings.MEDIA_ROOT + serializer.data['image']
#             files =  {('file', open(file_path, 'r'))}
#             resp = requests.post(url="http://localhost:8001/object-to-image", files=files)
#             print(resp)
#             return resp





# class HistoryViewSet(viewsets.ModelViewSet):
#     queryset = History.objects.all()
#     serializer_class = HistorySerializer