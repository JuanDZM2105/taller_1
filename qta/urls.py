from django.urls import path
from .views import home,exit,about, stadistics, TicketCreateView, TicketListView, TicketUpdateView
urlpatterns = [
    path('', home, name='home'),
    path('mainscreen/', TicketListView.as_view(),name='mainscreen'),
    path('about/', about, name='about'),
    path('mainscreen/<slug:id_unico>/edit/', TicketUpdateView.as_view(), name='more_info'),
    path('mainscreen/new/', TicketCreateView.as_view(), name='ticket'),
    path('mainscreen/stadistics/',stadistics, name='stadistics'),
    path('logout/',exit, name='exit'),
    
]