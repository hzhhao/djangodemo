from django.contrib import admin
from .models import Type1

# Register your models here.
class Type1Admin(admin.ModelAdmin):
    pass



admin.site.register(Type1, Type1Admin)
