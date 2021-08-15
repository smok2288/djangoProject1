from django.urls import path

from prod.views import FactorysView
# from prod.views import product_list

app_name = 'prod'

urlpatterns = [
    path('', FactorysView.as_view(), name='list_factory'),
    # path('', product_list, name='list_factory'),
]