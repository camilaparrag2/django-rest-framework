from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tarea', views.TareaViewSet, basename='tarea')

urlpatterns = [
    path("", include(router.urls)),
    
]
