from django.contrib import admin

from cars.models import Factory, Cars, Buyer, TechPasport, Production

admin.site.register(Factory)
admin.site.register(Cars)
admin.site.register(Buyer)
admin.site.register(TechPasport)
admin.site.register(Production)

