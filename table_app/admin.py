from django.contrib import admin
from .models import TableData


class TableAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'distance', 'date')

admin.site.register(TableData, TableAdmin)
