from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Solicitante


class SolicitanteList(ListView):
    model = Solicitante


class SolicitanteCreate(CreateView):
    model = Solicitante
    fields = '__all__'
    success_url = reverse_lazy('solicitante_list')
