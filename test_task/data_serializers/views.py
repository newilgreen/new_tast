from rest_framework.response import Response
from datetime import date
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from data_serializers.service import SubdivisionFilter, SubworkerFilter
from rest_framework.views import APIView
from subdivisions.models import Subdivision
from workers.models import Worker, Dismissal_list
from users.models import CustomUser
from data_serializers.serializers import (
    SubdivisionSerializer, 
    SubWorkerSerializer, 
    WorkerDetalSerializer, 
    DismissalSerializer,
    UserSerializer, 
    UserCreatSerializer,
    SubdivisionCreatSerializer, 
    WorkerCreatSerializer, 
    DismissalCreatSerializer
)

class SubdivisionCreatView(generics.CreateAPIView):
    """Создание нового Пользователя"""
    serializer_class = UserCreatSerializer


class UserCreatView(generics.CreateAPIView):
    """Создание нового подразделения"""
    serializer_class = SubdivisionCreatSerializer


class SubdivisionView(generics.ListAPIView): 
    """Ввод списка Подразделений"""
    serializer_class = SubdivisionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SubdivisionFilter
    
    def get_queryset(self):
        subdivision = Subdivision.objects

        return subdivision
    

class WorkerCreateView(generics.CreateAPIView):
    """Создание нового работника"""
    serializer_class = WorkerCreatSerializer


class WorkerDatalView(generics.ListAPIView): 
    """Ввод детальной информации о работниках всех подразделений"""
    serializer_class = WorkerDetalSerializer

    def get_queryset(self):
        worker = Worker.objects

        return worker


class SubWorkerView(generics.ListAPIView): 
    """Ввод списка работников в выбранном подразделении"""
    serializer_class = SubWorkerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SubworkerFilter

    def get_queryset(self):
        worker = Worker.objects

        return worker