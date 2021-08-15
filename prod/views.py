from django.shortcuts import render, get_object_or_404
from django.views import generic

from cars.models import Production, Cars, Factory


class FactorysView(generic.ListView):
    model = Factory
    template_name = "base.html"











# def product_list(request, model=None):
#     cars = Cars.objects.all()
#     facts = Factory.objects.filter(available=True)
#     if model:
#         car = get_object_or_404(Cars)
#         fact = facts.filter(model=model)
#     context = {'cars': cars, 'facts': facts}
#     return render(request, 'base.html', context)
#
#
# def product_detail(request, id, title):
#     fact = get_object_or_404(Factory, id=id, title=title, available=True)
#     context = {'fact': fact}
#     return render(request,'detail.html', context)