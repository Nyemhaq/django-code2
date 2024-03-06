from django.contrib import admin
from .models import Brand

class brandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name' , )}
    list_display = ['name','slug']
admin.site.register(Brand, brandAdmin)
