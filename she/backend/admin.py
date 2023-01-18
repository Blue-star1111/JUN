from django.contrib import admin
from .models import Type, CheckList, ListInput
# Register your models here.

admin.site.register(Type)
admin.site.register(CheckList)
admin.site.register(ListInput)
# admin.site.register(History)