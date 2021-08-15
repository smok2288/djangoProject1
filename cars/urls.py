from django.urls import path

from cars import views
from .views import CarsView, FactoryView, ProductionView, BuyerView, TechPasportView

app_name = 'list_factory'

urlpatterns = [
    path('cars/', CarsView.as_view(), name='cars'),
    path('factory/', FactoryView.as_view(), name='factory'),
    path('prod/', ProductionView.as_view(), name='prod'),
    path('buyer/', BuyerView.as_view(), name='buyer'),
    path('techpasport/', TechPasportView.as_view(), name='techpasport'),
]