from django.shortcuts import render
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework import serializers
from .models import Book, Publish, Author
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


# Create your views here.
# ============================ 基于ViewSet ===============================
class ViewSetBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ["title", "price"]


class ViewSetBookView(ViewSet):

    def get_all(self, request):
        return Response("查看所有资源")

    def add_object(self, request):
        return Response("添加单一资源")

    def get_object(self, request, pk):
        return Response("查看单一资源")

    def update_object(self, request, pk):
        return Response("更新单一资源")

    def delete_object(self, request, pk):
        return Response("删除单一资源")


# ============================= 基于GenericViewSet =================================
class ViewSetPublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'
        # fields = ["title", "price"]


class ViewSetPublishView(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Publish.objects.all()
    serializer_class = ViewSetPublishSerializer

