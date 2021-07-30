from django.db import models
from django.shortcuts import render

from .models import Person
#
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
from .serializer import *

from django.views.generic import ListView

#Generic API Views
class ListaPersonas(ListView):
    template_name = 'persona/personas.html'
    context_object_name = 'personas'
    model = Person

    def get_queryset(self):
        return self.model.objects.all()

class PersonaListApi(ListAPIView):
    serializer_class = PersonSerializer
    pagination_class = PersonPagination
    def get_queryset(self):
        return Person.objects.all()

class PersonaCreateApi(CreateAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Person.objects.all()

class PersonaGetApi(RetrieveAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Person.objects.all()

class PersonaUpdateApi(UpdateAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Person.objects.all()

class PersonaGetUpdateApi(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Person.objects.all()

class PersonaDeleteApi(DestroyAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Person.objects.all()
    
    #Custome Serializer
class PersonaListApiCustom(ListAPIView):
    serializer_class = PersonaSerializer
    pagination_class = PersonPagination
    def get_queryset(self):
        return Person.objects.all()

class PersonaListApiCustom2(ListAPIView):
    serializer_class = PersonSerializer2
    pagination_class = PersonPagination
    def get_queryset(self):
        return Person.objects.all()

#Meeting Api Views
class MeetingListApiCustom(ListAPIView):
    serializer_class = MeetSerializer
    pagination_class = PersonPagination
    def get_queryset(self):
        return Meet.objects.all()

class MeetingByPersonJobListApiCustom(ListAPIView):
    serializer_class = MeetByJobSerializer
    pagination_class = PersonPagination
    def get_queryset(self):
        return Meet.objects.cantidad_reuniones_job()

class MeetingListApiCustom2(ListAPIView):
    serializer_class = MeetSerializerLink
    pagination_class = PersonPagination
    def get_queryset(self):
        return Meet.objects.all()