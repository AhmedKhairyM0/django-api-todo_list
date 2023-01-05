from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
# Register your models here.
admin.site.register(Todo, TodoAdmin)