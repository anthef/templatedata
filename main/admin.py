from django.contrib import admin
from .models import Category, Link

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'url')
    list_filter = ('category', 'status')
    search_fields = ('title', 'url', 'description')