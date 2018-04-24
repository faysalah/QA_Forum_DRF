from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from forum import models
from forum import serializers
# Create your views here.

class ShortThreadList(APIView):

    def get(self, request):
        threads = models.Thread.objects.all()
        serializer = serializers.ShortThreadSerializer(threads, many=True)
        return Response(serializer.data)

class Thread(APIView):

    def get(self, request, pk):
        threads = models.Thread.objects.get(pk=pk)
        serializer = serializers.ThreadSerializer(threads, many=False)
        return Response(serializer.data)


class Add(APIView):

    def post(self, request, *args, **kwargs):
        num1 = request.data.get('num1', None)
        num2 = request.data.get('num2', None)
        if num1 and num2:
            add =  int(num1) + int(num2)
            sub =  int(num1) - int(num2)
            return Response({"add": add, "sub": sub})
        else:
            return Response({"success": False})
        