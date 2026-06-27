from django.contrib import admin
from .models import Project, Profile
# إدارة المشاريع (هنا الحل)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # تحويل صندوق الاختيار إلى واجهة اختيار مزدوجة احت
    # تحسين عرض القائمة الرئيسية للمشاريع
    list_display = ['title', 'description_preview']
    search_fields = ['title', 'description']

    # وظيفة لعرض جزء بسيط من الوصف في القائمة
    def description_preview(self, obj):
        return obj.description[:50] + "..."
    description_preview.short_description = "وصف مختصر"

# إدارة الملفات الشخصية
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_approved']
    list_filter = ['is_approved']
    list_editable = ['is_approved'] # تعديل الحالة مباشرة من الجدول
    search_fields = ['user__username']