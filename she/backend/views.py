from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .serializer import  TypeSerializer, CheckListSerializer, ListInputSerializer
from .models import Type, CheckList, ListInput
# Create your views here.

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class CheckListViewSet(viewsets.ModelViewSet):
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer

class ListInputViewSet(viewsets.ModelViewSet):
    queryset = ListInput.objects.all()
    serializer_class = ListInputSerializer

# class HistoryViewSet(viewsets.ModelViewSet):
#     queryset = History.objects.all()
#     serializer_class = HistorySerializer
