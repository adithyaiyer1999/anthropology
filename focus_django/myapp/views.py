from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def destroy(self, request, *args, **kwargs):
        if not request.data:
            return Response({"detail": "No project IDs provided."}, status=status.HTTP_400_BAD_REQUEST)

        project_ids = request.data.get("ids", [])
        projects_to_delete = Project.objects.filter(id__in=project_ids)
        projects_to_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
from django.http import JsonResponse
import json

# def my_view(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             # Perform operations on the data
#             result = do_something_with_data(data)
#             return JsonResponse({'result': result})
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data'}, status=400)
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)

# def do_something_with_data(data):
#     # Your logic to perform operations on the data
#     # ...
#     return 'success'
