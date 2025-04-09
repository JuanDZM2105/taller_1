from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import csv
from qta.services.statistics_service import StatisticsService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def exit(request):
    logout(request)
    return redirect('home')
 
 #Esta es la actividad número 4 para el taller 1 de Topicos en ing. software. Se escogió el patrón de diseño: CRUD para controladores
class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'mainscreen.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        queryset = super().get_queryset()
        searchState = self.request.GET.get('searchState')

        if searchState:
            queryset = queryset.filter(state__icontains=searchState)

        with open('ticketData.csv', "w") as f:
            f.write(", ".join(['id', 'support', 'person', 'number person', 'place', 'equipment', 'state', 'priority', 'discussion', '1', '2', '3']) + "; \n")
            for ticket in queryset:
                f.write(", ".join([
                    ticket.ticket_number, ticket.Support_name, ticket.contact_name,
                    ticket.contact_number, ticket.place, ticket.equipment,
                    ticket.state, ticket.priority, ticket.discussion,
                    ticket.first_follow_up, ticket.second_follow_up, ticket.third_follow_up
                ]) + "; \n")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searchState'] = self.request.GET.get('searchState', '')
        return context

class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    template_name = 'more_info.html'
    fields = ['Support_name',
        'first_follow_up',
        'second_follow_up',
        'third_follow_up',
        'state',
    ]
    context_object_name = 'ticket'
    slug_field = 'id_unico'
    slug_url_kwarg = 'id_unico'
    success_url = reverse_lazy('mainscreen')

    def form_valid(self, form):
        ticket = form.save(commit=False)

        if ticket.state == 'Completed':
            ticket.time_finish = timezone.now()
            ticket.call_time_finish = timezone.now()

        ticket.save()

        return redirect(self.success_url)

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'ticket.html'
    fields = ['call_time', 'priority', 'discussion', 'state', 'place',
              'equipment', 'contact_number', 'contact_name']
    success_url = reverse_lazy('mainscreen')

    def form_valid(self, form):
        # Asignar ticket_number automáticamente
        form.instance.ticket_number = Ticket.objects.count() + 1

        return super().form_valid(form)

@login_required
def stadistics(request):
    service = StatisticsService()
    stats = service.generate_statistics()

    return render(request, 'stadistics.html', stats)