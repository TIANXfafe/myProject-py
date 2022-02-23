from django.views import View
from django.http import JsonResponse
from .models import *
from rest_framework import viewsets
from .serializers import ClassifySerializer


# Create your views here.
class ClassifyAPIView(View):
    def get(self, request):
        classifies = Classify.objects.all()
        classify_list = []
        for classifyItem in classifies:
            classify_list.append({
                'id': classifyItem.id,
                'parent_id': classifyItem.parent_id,
                'name': classifyItem.name,
                'creator': classifyItem.creator,
                'createdAt': classifyItem.createdAt,
                'image': classifyItem.status
            })
        return JsonResponse(classify_list, safe=False)

class ClassifyViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = Classify.objects.all()
    serializer_class = ClassifySerializer
