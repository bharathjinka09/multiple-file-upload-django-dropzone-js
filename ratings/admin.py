from django.contrib import admin
from .models import Rating, Doc
# Register your models here.

admin.site.register([Rating,Doc])
