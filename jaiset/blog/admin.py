import imp
from django.contrib import admin
from .models import Created_date


class Created_date(admin.ModelAdmin):
    list_display = [
        "Created_date", "Published_date"
    ]
