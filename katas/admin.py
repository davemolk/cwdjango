from django.contrib import admin
from .models import Exercise, Tag

# Register your models here.
admin.site(Exercise)
admin.site(Tag)