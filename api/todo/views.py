#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo import serializers, models


class TodoListApiView(APIView):

    def get(
        self,
        request,
        *args,
        **kwargs
    ):
        try:
            todo_lists = models.ToDoList.objects.all()
            serializer = serializers.ToDoList(todo_lists, many=True)
            return Response(serializer.data)
        except models.ToDoList.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = serializers.ToDoList(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ToDoList(APIView):
    def get(self, request, todo_list_id, *args, **kwargs):
        # queryset =  models.ToDoList.objects.prefetch_related('items').all()
        # todo_lists = models.ToDoList.objects.all()
        try:
            todo_instance = models.ToDoList.objects.get(id=todo_list_id)
            serializer = serializers.ToDoList(todo_instance)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except models.ToDoList.DoesNotExist:
            raise Http404

    def delete(self, request, todo_list_id, format=None):

        try:
            todo_list = models.ToDoList.objects.get(id=todo_list_id)
            todo_list.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.ToDoList.DoesNotExist:
            raise Http404

    def put(self, request, todo_list_id, *args, **kwargs):
        try:
            todo_list = models.ToDoList.objects.get(id=todo_list_id)
            serializer = serializers.ToDoList(todo_list, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except models.ToDoList.DoesNotExist:
            raise Http404

    def post(self, request, todo_list_id, format=None):
        try:
            todo_list = models.ToDoList.objects.get(id=todo_list_id)
            serializer = serializers.ToDoListItem(data=request.data)

            if serializer.is_valid():
                serializer.validated_data['todo_list_id'] = todo_list_id
                serializer.save()
                return Response(serializer.data)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except models.ToDoList.DoesNotExist:
            raise Http404


class ToDoListItem(APIView):

    def get(self, request, todo_list_item_id,format=None, *args, **kwargs):
        todo_instance = models.ToDoListItem.objects.get(id=todo_list_item_id)
        serializer = serializers.ToDoListItem(todo_instance)
        return Response(serializer.data)

    def delete(self, request, todo_list_item_id, format=None, *args, **kwargs):
        """Deletes a ToDoListItem from the database"""
        try:
            item = models.ToDoListItem.objects.get(id=todo_list_item_id)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.ToDoListItem.DoesNotExist:
            return Http404
 

    def put(self, request, todo_list_item_id, *args, **kwargs):

        item = models.ToDoListItem.objects.get(id=todo_list_item_id)
        serializer = serializers.ToDoListItem(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)






























# # from rest_framework import viewsets
# from todo.models import Todo
# from todo.serializers import TodoSerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# # class TodoViewset(viewsets.ModelViewSet):
# #     queryset = Todo.objects.all()
# #     serializer_class = TodoSerializer
# @api_view(['GET', 'POST'])
# def todo_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         todo = Todo.objects.all()
#         serializer = TodoSerializer(todo, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def todo_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         todo.delete()


# def post(self, request, todo_list_id, format=None):
        # try:
        #     todo_list = models.ToDoList.objects.get(id=todo_list_id)
        #     serializer = serializers.ToDoListItem(data=request.data)

        #     if serializer.is_valid():
        #         serializer.validated_data['todo_list_id'] = todo_list_id
        #         serializer.save()
        #         return Response(serializer.data)

        #     else:
        #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # except models.ToDoList.DoesNotExist:
        #     raise Http404


 # def delete(self, request, id, format=None, *args, **kwargs):
    #     try:
    #         item = models.ToDoListItem.objects.get(id=55)
    #         item.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except models.ToDoListItem.DoesNotExist:
    #         raise Http404