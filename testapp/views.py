from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Person
from testapp.serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.generics import (
            ListAPIView,
            CreateAPIView,
            RetrieveAPIView,
            UpdateAPIView,
            DestroyAPIView,
    )

class PersonListAPIView(ListAPIView):
    # queryset = Person.objects.all()
    serializer_class = PersonSerializer
    def get_queryset(self):
        qs = Person.objects.all()
        name = self.request.GET.get('name')
        if name is not None:
            qs = qs.filter(name__icontains=name)
        return qs

class PersonCreateAPIView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PeopleRetrieveAPIView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonUpdateAPIView(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDestroyAPIView(DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
