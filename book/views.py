from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView


# django原生的View
# @method_decorator(csrf_exempt, name='dispatch')
# class BookView(View):
#     def get(self, request):
#         return HttpResponse("这是一个get请求")
#
#     def post(self, request):
#         return HttpResponse("这是一个post请求")
#
#     def delete(self, request):
#         return HttpResponse("这是一个delete请求")

# drf 的 APIView
@method_decorator(csrf_exempt, name='dispatch')
class BookView(APIView):
    def get(self, request):
        print("query_params:", request.query_params)
        return HttpResponse("这是一个 APIView get请求")

    def post(self, request):
        print("data:", request.data)
        return HttpResponse("这是一个 APIView post请求")

    def delete(self, request):
        return HttpResponse("这是一个 APIView delete请求")