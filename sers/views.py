from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from sers.models import Book

# Create your views here.
#  ======================  基于APIView的接口实现 ===========================

# 针对模型设计序列化器
# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#
#     # required=False 该字段可以为空 但是序列化器的约束要和数据库模型的约束一致,否则,后续序列化器验证通过,而数据库的数据插入报错
#     price = serializers.IntegerField(required=False)
#     date = serializers.DateField(source="pub_date")  # 重命名输出的序列化字段
#
#     def create(self, validated_data):
#         # 添加数据逻辑
#         book = Book.objects.create(**validated_data)
#         return book
#
#     def update(self, instance, validated_data):
#         print("instance:", instance)
#         print("validated_data:", validated_data)
#         # 更新逻辑解耦
#         Book.objects.filter(pk=instance.id).update(**validated_data)  # update不同于create 返回的是更新数据的条数, create返回增加的数据
#         updated_book = Book.objects.get(pk=instance.id)
#
#         return updated_book

class BookSerializers(serializers.ModelSerializer):
    date = serializers.DateField(source="pub_date")
    class Meta:
        model = Book
        # fields = "__all__"
        # fields = ["title", "price"]
        exclude = ["pub_date"]  # 排除哪些字段


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

            serializer.save()  # save()方法调用Baseserializer.save, 由于instance未传参 is None,就调用方法调用Baseserializer.create()
            return Response(serializer.data)
        else:
            # 校验失败
            return Response(serializer.errors)


class SersBookDetailView(APIView):

    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        print(book.id)
        '''
        单条数据 many=False 的序列化过程
        d = {}
        d[""] = obj.title
        d[""] = obj.price
        d["date"] = obj.pub_date  当序列化器有sourse参数时
        '''
        serializer = BookSerializers(instance=book, many=False)
        print(serializer.data)
        return Response(serializer.data)

    def put(self, request, book_id):
        update_book = Book.objects.get(pk=book_id)

        # 构建序列化器
        serializer = BookSerializers(instance=update_book, data=request.data)

        # is_valid() 校验提交数据
        if serializer.is_valid():
            # 更新逻辑
            # Book.objects.filter(pk=book_id).update(**serializer.validated_data)  # update不同于create 返回的是更新数据的条数, create返回增加的数据
            # updated_book = Book.objects.get(pk=book_id)
            # serializer.instance = updated_book

            serializer.save()  # save()方法调用Baseserializer.save, 由于instance已传参, is not None,就调用方法调用Baseserializer.update()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self, request, book_id):
        Book.objects.get(pk=book_id).delete()
        return Response


# ======================   基于GenericAPIView的接口实现 =======================
