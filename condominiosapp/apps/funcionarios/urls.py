from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'funcionarios'

router = routers.DefaultRouter()
router.register('', views.FuncionarioViewSet, basename='funcionarios')

urlpatterns = [
    path('', include(router.urls))
]
