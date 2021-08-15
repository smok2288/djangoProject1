from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView, ListView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import Factory, Cars, Production, Buyer, TechPasport
from cars.serializers import CarsSerializer, FactorySerializer, ProductionSerializer, BuyerSerializer, \
    TechPasportSerializer


class CarsView(APIView):
    def get(self, request, pk=None):
        if not pk:
            cars = Cars.objects.all()
            serializer = CarsSerializer(cars, many=True)
            print(serializer)
        else:
            cars = Cars.objects.get(pk=pk)
            serializer = CarsSerializer(cars)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class FactoryView(ListCreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

class ProductionView(ListCreateAPIView):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer

class BuyerView(ListCreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


class TechPasportView(ListCreateAPIView):
    queryset = TechPasport.objects.all()
    serializer_class = TechPasportSerializer

# class ProductionView(APIView):
#     def get(self, request, pk=None):
#         if not pk:
#             prod = Production.objects.all()
#             serializer = ProductionSerializer(prod, many=True)
#         else:
#             cars = Production.objects.get(pk=pk)
#             serializer = ProductionSerializer(prod)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProductionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


