from django.contrib import admin
from .models import BlogPost

class BlogPostsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp', 'user']

admin.site.register(BlogPost, BlogPostsAdmin)
