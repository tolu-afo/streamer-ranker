from django.contrib import admin
from .models import Streamer, Viewer, Category, Trait, Language
# Register your models here.
admin.site.register(Streamer)
admin.site.register(Viewer)
admin.site.register(Category)
admin.site.register(Trait)
admin.site.register(Language)