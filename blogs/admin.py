from django.contrib import admin

from .models import BlogPost, BlogText

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(BlogText)