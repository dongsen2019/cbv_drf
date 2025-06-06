from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from GenericAPIView.models import Book, Publish, Author

# Create your views here.

# ======================   基于GenericAPIView的接口实现 =======================


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        # fields = ["title", "price"]


class GenericBookView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request):
        # 构建序列化器对象:
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        # GenericAPIView.get_serializer() 方法 先使用 get_serializer_class() 获取 serializer_class
        # 然后用这个类根据传入的instance和many参数实例化对象,赋值给serializer

        return Response(serializer.data)

    def post(self, request):

        # 构建序列化器对象  data 是反序列化传参
        serializer = self.get_serializer(data=request.data)

        # 校验数据
        if serializer.is_valid():  # 返回一个bool值
            # serializer._validated_data 存储正确数据
            # serializer._errors 存储错误数据日志
            # book = Book.objects.create(**serializer.validated_data)
            # print(book)

            serializer.save()  # save()方法调用Baseserializer.save, 由于instance未传参 is None,就调用方法调用Baseserializer.create()
            return Response(serializer.data)
        else:
            # 校验失败
            return Response(serializer.errors)


class GenericBookDetailView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request, pk):
        # 构建序列化器对象:
        serializer = self.get_serializer(instance=self.get_object(), many=False)
        # GenericAPIView.get_serializer() 方法 先使用 get_serializer_class() 获取 serializer_class
        # 然后用这个类根据传入的instance和many参数实例化对象,赋值给serializer
        # get_object() 会根据传入的pk值循环遍历queryset查找对应的数据
        # !!! 需要注意的是,URL路由处的 'book/<int:pk>' int类型的名称必须要与get_object() 方法中默认的名称 pk

        return Response(serializer.data)

    def put(self, request, pk):
        # 构建序列化器对象:
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)

        # 数据校验
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object().delete()

        return Response("删除成功")


class PublishSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"
        # fields = ["title", "price"]


class GenericPublishView(GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializers

    def get(self, request):
        # 构建序列化器对象:
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        # GenericAPIView.get_serializer() 方法 先使用 get_serializer_class() 获取 serializer_class
        # 然后用这个类根据传入的instance和many参数实例化对象,赋值给serializer

        return Response(serializer.data)

    def post(self, request):

        # 构建序列化器对象  data 是反序列化传参
        serializer = self.get_serializer(data=request.data)

        # 校验数据
        if serializer.is_valid():  # 返回一个bool值
            # serializer._validated_data 存储正确数据
            # serializer._errors 存储错误数据日志
            # book = Book.objects.create(**serializer.validated_data)
            # print(book)

            serializer.save()  # save()方法调用Baseserializer.save, 由于instance未传参 is None,就调用方法调用Baseserializer.create()
            return Response(serializer.data)
        else:
            # 校验失败
            return Response(serializer.errors)


class GenericPublishDetailView(GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializers

    def get(self, request, pk):
        # 构建序列化器对象:
        serializer = self.get_serializer(instance=self.get_object(), many=False)
        # GenericAPIView.get_serializer() 方法 先使用 get_serializer_class() 获取 serializer_class
        # 然后用这个类根据传入的instance和many参数实例化对象,赋值给serializer
        # get_object() 会根据传入的pk值循环遍历queryset查找对应的数据
        # !!! 需要注意的是,URL路由处的 'book/<int:pk>' int类型的名称必须要与get_object() 方法中默认的名称 pk

        return Response(serializer.data)

    def put(self, request, pk):
        # 构建序列化器对象:
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)

        # 数据校验
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object().delete()

        return Response("删除成功")


# =================== 基于Mixins 和 GenericAPIViEw 的接口实现 ========================

class GenericAuthorView(GenericAPIView):
    pass


class GenericAuthorDetailView(GenericAPIView):
    pass

