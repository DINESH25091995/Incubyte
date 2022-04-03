from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Content
from rest_framework.decorators import api_view

from firstApp.serializers import ContentSerializers
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def Contentlist(request):
    if request.method=='GET':
        contents=Content.objects.all()
        serializer=ContentSerializers(contents,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=ContentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def Content_details(request,pk):
    try:
        contents=Content.objects.get(pk=pk)
    except Content.DoesNnotExist:
        return Response(status=status.HTTP_404_NOT_FOUNT)
    if request.method=='GET':
        serializer=ContentSerializers(contents)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=ContentSerializers(contents,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        contents.delete()
        return Response()
