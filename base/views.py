from django.shortcuts import render
from .models import student
from .serializers import StudentModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class studentAPI(APIView):
    def get(self, request,pk=None, format=None):
        id = pk
        if id is not None:
            stu = student.objects.get(id=pk)
            serializer = StudentModelSerializer(stu)
            return Response(serializer.data)

        stu = student.objects.all()
        serializer = StudentModelSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self,request,format= None):
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def put(self,request,pk, format=None):
        id=pk
        stu = student.objects.get(pk=id)
        serializer = StudentModelSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self,request,pk,fromat=None):
           stu = student.objects.get(id=pk)
           stu.delete()
           return Response({'msg': 'Deleted sucessfully.'})









