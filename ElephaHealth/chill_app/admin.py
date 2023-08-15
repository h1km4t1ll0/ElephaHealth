from django.contrib import admin
from .models import User


@admin.register(User)
class SourceAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "phone_number",
        "company",
        "date_of_birth",
        "gender",
        "height",
        "weight",
        "avg_heart_rate"
    ]
