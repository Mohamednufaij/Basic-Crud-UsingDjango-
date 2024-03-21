from django.contrib import admin
from .models import Regmodel
# Register your models here.
class RegAdmin(admin.ModelAdmin):
    list_display="firstname","lastname","country"
    
admin.site.register(Regmodel,RegAdmin)