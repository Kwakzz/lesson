from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from lesson.serializers import LessonSerializer
from lesson.models import Lesson


@api_view(['POST'])
def create(request):
    serializer = LessonSerializer(data=request.data)
    if serializer.is_valid():
        lesson_obj = serializer.save()
        lesson_json = LessonSerializer(lesson_obj)
        return Response(lesson_json.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET'])
def get(request, id):
    try:
        lesson = Lesson.objects.get(id=id)
    except Lesson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = LessonSerializer(lesson)
    return Response(serializer.data)
        

@api_view(['GET'])
def get_all(request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)