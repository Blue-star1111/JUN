from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('type', views.TypeViewSet, basename='type')
router.register('checklist', views.CheckListViewSet, basename='list')
router.register('listinput', views.ListInputViewSet, basename='input')
# router.register('history', views.HistoryViewSet, basename='history')

urlpatterns = [
    path("", include(router.urls)),
]