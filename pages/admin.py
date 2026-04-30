from django.contrib import admin
from .models import Project, Component
from .models import Profile
admin.site.register(Project)
admin.site.register(Component)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_approved']
    list_filter = ['is_approved']
    list_editable = ['is_approved'] # يسمح للمدير بالتعديل مباشرة من القائمة