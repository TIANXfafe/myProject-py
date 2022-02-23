from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'classify', views.ClassifyViewSet)

urlpatterns = [
    path('classify/', views.ClassifyAPIView.as_view()),
]
