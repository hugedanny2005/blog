from django.contrib import admin
from .models import Account, Blog

# Register your models here.
admin.site.register(Account)
admin.site.register(Blog)