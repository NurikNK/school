from django.http import HttpResponse
from rest_framework import generics, viewsets, response
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentViewSet(viewsets.ViewSet):
#     """
#     A viewset for listing or retrieving students
#     """
#     def list(self, request):
#         queryset = Student.objects.all()
#         serializer = StudentSerializer(instance=queryset, many=True)
#         return response.Response(data=serializer.data)
#
#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return response.Response(data=serializer.data, status=201)
#
#     def partial_update(self, request, pk=None):
#         queryset = Student.objects.all()
#         student = get_object_or_404(request, pk=pk)
#         serializer = StudentSerializer(instance=student, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         response.Response(data=serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Student.objects.all()
#         student = get_object_or_404(request, pk=pk)
#         serializer = StudentSerializer(instsnce=student)
#         return response.Response(data=serializer.data)
#
#     def destroy(self, request, pk=None):
#         queryset = Student.objects.all()
#         student = get_object_or_404(request, pk=pk)
#         student.delete()
#         return response.Response(status=204)



# class StudentListCreateView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

