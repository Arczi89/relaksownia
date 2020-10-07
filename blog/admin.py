from django.contrib import admin

from .models import BlogPost, BlogConfiguration


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(BlogConfiguration)
class BlogConfigurationAdmin(admin.ModelAdmin):
    save_as = True
