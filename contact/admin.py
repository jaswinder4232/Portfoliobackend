# admin.py

from django.contrib import admin
from .models import ContactMessage, Category, Stack, ProjectImage, Project

# Customizing the admin for the ContactMessage model
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)

# Customizing the admin for the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Customizing the admin for the Stack model
class StackAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Customizing the admin for the ProjectImage model
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'link')
    search_fields = ('title', 'file')
    list_filter = ('file',)

# Customizing the admin for the Project model
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'live_link', 'git_hub_link')
    search_fields = ('name', 'description', 'live_link', 'git_hub_link')
    list_filter = ('category', 'stacks')
    filter_horizontal = ('stacks', 'images')  # To make ManyToMany fields look nicer

# Register models with customized admin classes
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Stack, StackAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(Project, ProjectAdmin)
