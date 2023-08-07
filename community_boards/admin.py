from django.contrib import admin
from .models import Community_Board


@admin.register(Community_Board)
class Review_ReviewAdmin(admin.ModelAdmin):

    """Review_Review Admin Definition"""

    pass
