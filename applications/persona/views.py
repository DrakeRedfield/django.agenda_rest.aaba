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
    def get_queryset(self):
        return Person.objects.all()    