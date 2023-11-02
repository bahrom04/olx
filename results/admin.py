from django.contrib import admin
from .models import Students, Regions, Districts, Schools

# Register your models here.

admin.site.register(Students)
admin.site.register(Regions)
admin.site.register(Districts)
admin.site.register(Schools)