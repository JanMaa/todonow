from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, CustomTaskSerializer

# Create your views here.

from .models import *

# @api_view(['GET'])
# def taskList(request):
# 	tasks = Task.objects.all().order_by('-id')
# 	serializer = TaskSerializer(tasks, many=True)
# 	return Response(serializer.data)

@api_view(['GET'])
def taskList(request):
	tasks = request.user.task_set.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = CustomTaskSerializer(data=request.data, user=request.user)
	
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')
