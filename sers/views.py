from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from sers.models import Book

# Create your views here.


# 针对模型设计序列化器
class BookSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=32)

    # required=False 该字段可以为空 但是序列化器的约束要和数据库模型的约束一致,否则,后续序列化器验证通过,而数据库的数据插入报错
    price = serializers.IntegerField(required=False)
    date = serializers.DateField(source="pub_date")  # 重命名输出的序列化字段

    def create(self, validated_data):
        # 添加数据逻辑
        book = Book.objects.create(**validated_data)
        return book


class SersBookView(APIView):

    def get(self, request):
        # 查看所有的书籍
        book_list = Book.objects.all()  # queryset[book01,book02,...]

        # 构建序列化器对象:
        serializer = BookSerializers(instance=book_list, many=True)
        # instance 是序列化传参
        # data 是反序列化传参
        # 如果是一条数据,一个模型对象,many = False
        # 如果是N条数据,一个queryset对象,many = True

        print(type(serializer.data))

        '''
        serializer.data 的实现
        
        temp = []
        
        for obj in book_list:
            d = {}
            d["title"] = obj.title
            d["price"] = obj.price
            d["pub_date"] = obj.pub_date
            
            temp.append(d)
        '''

        return Response(serializer.data)

    def post(self, request):
        # 获取请求数据
        print("data", request.data)

        # 构建序列化器对象  data 是反序列化传参
        serializer = BookSerializers(data=request.data)

        # 校验数据
        if serializer.is_valid():  # 返回一个bool值
            # serializer._validated_data 存储正确数据
            # serializer._errors 存储错误数据日志
            # book = Book.objects.create(**serializer.validated_data)
            # print(book)

            serializer.save()  # save()方法调用Baseserializer.save,并调用方法调用Baseserializer.create()
            return Response(serializer.data)
        else:
            # 校验失败
            return Response(serializer.errors)


class SersBookDetailView(APIView):

    def get(self, request, id):
        pass

    def put(self, request, id):
        pass

    def delete(self, request, id):
        pass



