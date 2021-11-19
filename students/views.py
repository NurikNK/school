from django.http import HttpResponse
from rest_framework import status, views, response

from .models import Student
from .serializers import StudentSerializer

"""@csrf_exempt
def student_list(request):
    """"""
    List all courses or create a new course
    """"""
    if request.method == "GET":
        student = Student.objects.all()
        serializer = StudentSerializer(instance=student, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = parsers.JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""""
"""
@csrf_exempt
def students_detail(request, pk):
  
    #Retrieve, update or delete a courses
   
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(instance=student)
        return JsonResponse(data=serializer.data, status=200)
    elif request.method in {'PUT', 'PATCH'}:
        data = parsers.JSONParser().parse(request)
        serializer = StudentSerializer(instance=student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    elif request.method == "DELETE":
        student.delete()
        return HttpResponse(status=204)"""


class StudentListAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        student = Student.objects.all()
        serializer = StudentSerializer(instance=student, many=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)


class StudentDetailAPIView(views.APIView):

    def get_object(self, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return HttpResponse(status=404)
        return student

    def get(self, request, pk):
        student = self.get_object(pk=pk)
        serializer = StudentSerializer(instance=student)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, *args, **kwargs):
        student = self.get_object(pk=pk)
        student.delete()
        return response.Response(status=204)


"""class StudentCreateView(generic.CreateView):
    model = Student
    template_name = 'student.html'
    form_class = StudentForm
    success_url = '/students/create/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context
"""
"""
class StudentCourseCreateView(generic.CreateView):
    model = StudentCourse
    template_name = 'studentcourse.html'
    form_class = StudentCourseForm
    success_url = '/students/student_course_create/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_course'] = StudentCourse.objects.all()
        return context"""