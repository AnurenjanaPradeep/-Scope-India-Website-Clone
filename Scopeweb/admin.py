from django.contrib import admin
from .models import Category,Courses,Registration,Country

# Register your models here.
admin.site.register(Category)
admin.site.register(Courses)
admin.site.register(Registration)
admin.site.register(Country)
# admin.site.register(State)
# admin.site.register(City)