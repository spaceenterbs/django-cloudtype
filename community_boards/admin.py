from django.contrib import admin
from .models import Community_Board


@admin.register(Community_Board)
class Community_Board(admin.ModelAdmin):
    pass
