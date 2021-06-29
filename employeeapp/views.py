from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import doctorsSerializer,patientsSerializer
from .models import doctor,patient
     
class doctorList(APIView):
    def get(self,request):
        doctor1 = doctor.objects.all()
        serializer = doctorsSerializer(doctor1, many = True)
        return Response(serializer.data)
        
    
    def post(self,request):
        serializer = doctorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class doctorDetail(APIView):
    def get_object(self, pk):
        try:
            return doctor.objects.get(pk=pk)
        except doctor.DoesNotExist:
            print("<h1>Not found</h1>")
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = doctorsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = doctorsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class patientList(APIView):
    def get(self,request):
        doctor1 = patient.objects.all()
        serializer = patientsSerializer(doctor1, many = True)
        return Response(serializer.data)
        
    
    def post(self,request):
        serializer = patientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class patientDetail(APIView):
    def get_object(self, pk):
        try:
            return patient.objects.get(pk=pk)
        except patient.DoesNotExist:
            print("<h1>Not found</h1>")
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = patientsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = patientsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)